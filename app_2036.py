import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import yfinance as yf
# Cấu hình trang
st.set_page_config(page_title="Lộ trình 2036", page_icon="📈")

# 1. NHẮC NHỞ MỤC TIÊU QUYẾT LIỆT
st.title("🛡️ HÀNH TRÌNH TỰ DO TÀI CHÍNH 2036")
st.sidebar.markdown(f"### 🎯 Mục tiêu: 2036")
st.sidebar.info("Mẹ của 3 con phải mạnh mẽ. Python là vũ khí, không phải rào cản.")
st.sidebar.warning("TUYỆT ĐỐI KHÔNG FUTURE. Chỉ tập trung giá trị dài hạn.")

# 2. LẤY GIÁ THỊ TRƯỜNG
def get_price(symbol):
    try:
        ticker = yf.Ticker(f"{symbol}-USD")
        price = ticker.fast_info['last_price']
        return float(price)
    except:
        return 0.0

btc_p = get_price("BTC")
eth_p = get_price("ETH")

# 3. HIỂN THỊ DANH MỤC SPOT
st.header("💰 Danh mục Spot (DCA 2.7tr/tuần)")
col1, col2 = st.columns(2)
with col1:
    st.metric("Bitcoin (BTC)", f"${btc_p:,.2f}", delta="Cần rút gốc nếu lãi > 50%")
with col2:
    st.metric("Ethereum (ETH)", f"${eth_p:,.2f}")
# Đọc dữ liệu từ file thực tế
try:
    df = pd.read_csv('danh_muc.csv')
    # Tính giá trung bình nếu bạn mua nhiều lần
    df_summary = df.groupby('loai_coin').agg({
        'gia_mua_usd': 'mean',
        'so_tien_vnd': 'sum'
    }).reset_index()
except FileNotFoundError:
    st.error("Chưa tìm thấy file danh_muc.csv. Hãy tạo file để theo dõi tài sản thực!")
    df_summary = pd.DataFrame()

# 4. NHẬT KÝ CHIÊM NGHIỆM (21:00)
st.header("📝 Nhật ký chiêm nghiệm & Thấu cảm")
note = st.text_area("Hôm nay bạn cảm thấy thế nào? Ghi lại để thoát khỏi sự tiêu cực công sở:")
if st.button("Lưu tâm trí"):
    with open("nhat_ky.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()}: {note}\n")
    st.success("Tâm trí đã được lưu lại. Hãy nghỉ ngơi bên các con!")

# 5. LỜI NHẮC CHIẾN LƯỢC
st.divider()
st.markdown("> **Ghi nhớ:** Sự đấu đá ở văn phòng chỉ là tạm thời. Hệ thống Micro-SaaS bạn đang xây dựng mới là vĩnh cửu.")