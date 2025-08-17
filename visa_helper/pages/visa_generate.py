# visa_generate.py

import streamlit as st
import datetime
import base64
import requests
import logging
import json

logging.basicConfig(level=logging.INFO)

def call_ollama_local(prompt):
    url = "http://192.168.1.142:11434/api/generate"
    payload = {
        "model": "mistral:latest",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=200)
        response.raise_for_status()

        # 有些版本 Ollama 返回的是多行 JSON 组成的文本，需要逐行解析
        results = []
        for line in response.text.strip().splitlines():
            data = json.loads(line)
            results.append(data.get("response", ""))

        return "".join(results)

    except requests.exceptions.ConnectionError:
        return "❌ 无法连接 Ollama 服务，请确认你已运行 `ollama serve` 并使用了 `ollama run model_name` 加载模型。"
    except requests.exceptions.HTTPError as e:
        return f"❌ HTTP错误：{e}"
    except Exception as e:
        return f"❌ 本地模型调用失败：{e}"
    
# 设定标题
st.set_page_config(page_title="签证助手生成页")
st.title("🧳 一站式签证助手包生成")

st.markdown("请填写以下信息，我们将为你生成定制化的签证准备清单与行程建议")

# --- 基本信息输入 ---
with st.form("visa_form"):
    col1, col2 = st.columns(2)
    with col1:
        nationality = st.selectbox("你的护照国籍", ["中国", "英国", "美国", "印度", "其他"])
        visa_type = st.selectbox("签证类型", ["旅游签", "学生签", "工作签"])
        budget_level = st.radio("预算水平", ["低", "中", "高"], horizontal=True)
    with col2:
        destination = st.selectbox("目标国家", ["法国", "英国", "日本", "德国", "新加坡", "美国", "澳大利亚"])
        start_date = st.date_input("预计出发时间", datetime.date.today())
        duration = st.slider("计划停留天数", 3, 60, 10)

    # 文件上传（可选）
    uploaded_file = st.file_uploader("📤 上传护照信息页（可选，用于自动填表）", type=["jpg", "png", "pdf"])

    submitted = st.form_submit_button("🚀 生成签证助手包")

# --- 提交后生成内容 ---
if submitted:
    st.success("生成中，请稍等...")

    # 构造 prompt
    prompt = f"""
你是一位签证顾问，请根据以下信息，为用户生成一份详细的签证准备清单和行程建议：
- 护照国籍：{nationality}
- 目标国家：{destination}
- 签证类型：{visa_type}
- 出发时间：{start_date}
- 停留天数：{duration}
- 预算水平：{budget_level}

请输出：
1. 所需签证材料清单（详细）
2. 建议行程安排（按天列出）
3. 可退订的机票/酒店预订建议
4. 其他注意事项
"""

    with st.spinner("🤖 本地模型正在生成中..."):
        result = call_ollama_local(prompt)


    # 展示结果
    st.markdown("### 📋 签证助手包内容如下：")
    st.markdown(result)

    # 下载按钮（保存为 txt，后续可转 Word/PDF）
    st.download_button("📥 下载清单（txt 格式）", data=result, file_name="visa_package.txt", mime="text/plain")

    # 展示上传图片（可选）
    if uploaded_file:
        st.image(uploaded_file, caption="护照信息页（供后续识别使用）", width=300)
