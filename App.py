import streamlit as st
import numpy as np
from HousingDataProcessor import HousingDataProcessor
from LinearRegressionModel import LinearRegressionModel
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")
st.title("🏠 DỰ ĐOÁN GIÁ NHÀ BẰNG HỒI QUY TUYẾN TÍNH VỚI 3 CÁCH TIẾP CẬN")
st.caption("SO SÁNH 3 CÁCH TIẾP CẬN: GRADIENT DESCENT, XÁC SUẤT THỐNG KÊ, SCIKIT-LEARN")

# Load va xu ly data
processor = HousingDataProcessor("Hanoi_housing_dataset.csv")
processor.load_and_process()
x_scaled, y_scaled = processor.get_scaled_data()
x_real, y_real = processor.get_real_data()

# Train model (gradient descent, cong thuc xstk, sklearn)
model = LinearRegressionModel()
model.set_data(x_scaled, y_scaled)

w_gd, b_gd = model.train_gradient_descent()
w_ols, b_ols = model.xstk_regression()
w_sk, b_sk = model.sklearn_regression()

# GUI
st.subheader("📏 Nhập diện tích nhà (m²):")
area = st.number_input("Diện tích", min_value=10.0, max_value=300.0, value=60.0, step=1.0)

x_input_scaled = processor.transform_area(area)

y_pred_gd = processor.inverse_predict(model.predict_gradient(x_input_scaled))[0]
y_pred_ols = processor.inverse_predict(model.predict_xstk(x_input_scaled, w_ols, b_ols))[0]
y_pred_sk = processor.inverse_predict(model.predict_sklearn(x_input_scaled.reshape(-1, 1)))[0]

# Hien thi ket qua
st.subheader("📊 KẾT QUẢ DỰ ĐOÁN:")
st.write(f"🔹 **GRADIENT DESCENT**: {y_pred_gd:,.0f} VND/m²")
st.write(f"🔹 **XÁC SUẤT THỐNG KÊ**: {y_pred_ols:,.0f} VND/m²")
st.write(f"🔹 **SCIKIT-LEARN**: {y_pred_sk:,.0f} VND/m²")

# Ve bieu do
x_line = np.linspace(min(x_scaled), max(x_scaled), 100)
x_line_real = processor.scaler_x.inverse_transform(x_line.reshape(-1, 1)).flatten()

y_line_gd = processor.inverse_predict(model.predict_gradient(x_line))
y_line_ols = processor.inverse_predict(model.predict_xstk(x_line, w_ols, b_ols))
y_line_sk = processor.inverse_predict(model.predict_sklearn(x_line.reshape(-1, 1)))

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x_real, y_real, s=10, alpha=0.2, label="DỮ LIỆU THỰC TẾ")
ax.plot(x_line_real, y_line_gd, label="GRADIENT DESCENT")
ax.plot(x_line_real, y_line_ols, label="XÁC SUẤT THỐNG KÊ")
ax.plot(x_line_real, y_line_sk, label="SCIKIT-LEARN")
ax.set_xlabel("Diện tích (m²)")
ax.set_ylabel("Giá/m² (VNĐ)")
ax.set_title("SO SÁNH MÔ HÌNH DỰ ĐOÁN GIÁ NHÀ")
ax.legend()
ax.grid(True)
st.pyplot(fig)
