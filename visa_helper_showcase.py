<<<<<<< HEAD

=======
# visa_helper_showcase.py

import streamlit as st

st.set_page_config(page_title="签证助手 AI", layout="centered")

# 页面标题
st.title("✈️ 一站式签证准备助手")
st.markdown("#### 自动生成签证材料清单 · 智能行程规划 · 可退订机票酒店推荐 · 表格自动填写")

st.divider()

# 服务介绍
st.subheader("📋 我们能为你做什么？")
st.markdown("""
- ✅ **个性化签证准备清单**：基于目标国家、签证类型，自动列出所需材料（如护照、银行证明、机票等）。
- ✅ **签证友好的旅行行程规划**：根据出行时间自动规划合理路线。
- ✅ **可退订酒店与机票推荐**：帮你找到签证友好型预订方式，避免经济损失。
- ✅ **自动填写签证表格**：上传护照页，帮你自动填写申请表（支持 PDF/Word）。
- ✅ **支持中英文版本**。
""")

st.divider()

# 收费介绍
st.subheader("💰 服务价格")
st.markdown("""
**一次性支付 ¥19.9 即可获得：**
- 签证材料清单（PDF+Word）
- 自动生成的旅行行程计划
- 预订建议链接（带退订筛选）
- 上传信息后自动生成申请表草稿
""")

st.info("⚠️ 当前为展示页，支付功能开发中。")

st.button("🚀 我想立即使用这个服务（敬请期待）")

st.divider()

# FAQ
st.subheader("❓ 常见问题")

with st.expander("Q: 支持哪些国家和签证类型？"):
    st.write("A: 当前支持旅游签证为主（申根国家、日本、英国、新加坡、美国等），后续会扩展到留学和工作签证。")

with st.expander("Q: 服务内容包括实际代办吗？"):
    st.write("A: 不包含递签服务，仅提供材料准备、辅助生成、内容指导，适合DIY办签用户。")

with st.expander("Q: 付款后如何收到服务内容？"):
    st.write("A: 用户付款后会进入系统界面，输入具体信息后即可生成相关文件并下载。")

with st.expander("Q: 上传护照安全吗？"):
    st.write("A: 本地部署可选，无数据外传。未来也将加入加密上传和数据清除功能。")

st.divider()

# 联系方式
st.subheader("📮 联系我们")
st.markdown("""
- 微信客服：`VisaHelper_Ai`
- 邮箱：`visa-ai@youremail.com`
- 小红书/知乎搜索：“签证助手 AI”
""")

st.caption("© 2025 签证助手 AI - 用 AI 简化签证流程")

