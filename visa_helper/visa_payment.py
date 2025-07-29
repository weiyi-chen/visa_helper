# visa_payment.py

import streamlit as st
from PIL import Image

st.set_page_config(page_title="支付页面", layout="centered")
st.title("💰 支付后开启签证助手包")

st.markdown("请扫码支付 **¥19.90**，支付完成后上传截图即可开始使用服务。")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🟢 微信支付")
    wechat_img = Image.open("wechat_qr.jpg")  # 你的微信收款码
    st.image(wechat_img, width=200)
with col2:
    st.markdown("### 🔵 支付宝支付")
    alipay_img = Image.open("alipay_qr.jpg")  # 你的支付宝收款码
    st.image(alipay_img, width=200)

st.divider()

st.markdown("✅ **支付完成后，请上传付款截图**")
uploaded = st.file_uploader("📤 上传支付截图", type=["png", "jpg", "jpeg"])

if uploaded:
    st.success("收到上传截图！你可以点击下方按钮开始生成签证助手包。")

    if st.button("🚀 开始生成签证助手包"):
        st.switch_page("visa_generate.py")  # 跳转到生成页
