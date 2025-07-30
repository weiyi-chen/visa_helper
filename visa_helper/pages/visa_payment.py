import streamlit as st
from PIL import Image
from pathlib import Path

DIR = Path(__file__).parent          # 当前脚本文件夹
wechat_path = DIR / "wechat_qr.jpg"
alipay_path = DIR / "alipay_qr.jpg"

st.set_page_config(page_title="支付页面", layout="centered")
st.title("💰 支付后开启签证助手包")
st.markdown("请扫码支付 **¥19.90**，支付完成后上传截图即可开始使用服务。")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🟢 微信支付")
    if wechat_path.exists():
        st.image(str(wechat_path), width=200)
    else:
        st.error("未找到 wechat_qr.jpg")

with col2:
    st.markdown("### 🔵 支付宝支付")
    if alipay_path.exists():
        st.image(str(alipay_path), width=200)
    else:
        st.error("未找到 alipay_qr.jpg")



st.markdown(
    """
    <style>
    .next-btn {
        display: inline-block;
        font-size: 1rem;
        font-weight: 600;
        padding: 0.5em 1.2em;
        color: #fff;
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        border: none;
        border-radius: 25px;
        text-decoration: none;
    }
    .next-btn:hover {
        background: linear-gradient(135deg, #2575fc 0%, #6a11cb 100%);
    }
    </style>
    <a href="/visa_generate" target="_self" class="next-btn">🚀 开始生成签证助手包</a>
    """,
    unsafe_allow_html=True,
)

st.divider()