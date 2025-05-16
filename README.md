# 🏠 DỰ ĐOÁN GIÁ NHÀ HÀ NỘI BẰNG HỒI QUY TUYẾN TÍNH

Ứng dụng giúp bạn dự đoán **giá nhà trên mỗi mét vuông (VND/m²)** dựa trên **diện tích**, sử dụng 3 phương pháp hồi quy tuyến tính khác nhau. Giao diện được xây dựng bằng **Streamlit**, thân thiện và dễ sử dụng.

---

## 🚀 TÍNH NĂNG NỔI BẬT

- 🎯 Dự đoán giá nhà theo diện tích nhập vào
- 📈 So sánh kết quả từ 3 phương pháp hồi quy:
  - Gradient Descent (tối ưu lặp)
  - Công thức OLS thủ công của XSTK
  - Thư viện Scikit-learn
- 🧹 Làm sạch và chuẩn hoá dữ liệu tự động
- 📊 Biểu đồ trực quan hóa dữ liệu và mô hình

---

## 📁 CẤU TRÚC DỰ ÁN

- `App.py`: Giao diện Streamlit cho người dùng.
- `Main.py`: Chạy mô hình và hiển thị kết quả từ dòng lệnh.
- `HousingDataProcessor.py`: Tiền xử lý và chuẩn hoá dữ liệu.
- `LinearRegressionModel.py`: Cài đặt 3 phương pháp hồi quy tuyến tính.
- `Hanoi_housing_dataset.csv`: Dữ liệu gốc về giá nhà tại Hà Nội.

---

## 📊 VÍ DỤ DỰ ĐOÁN

**Nhập:** `Diện tích = 60 m²`  
**Kết quả thực tế (sử dụng Gradient Descent):**

- 🔹 Gradient Descent: `102,334,114 VND/m²`
- 🔹 Công thức OLS: *(tùy thuộc mô hình, thường gần tương đương)*
- 🔹 Scikit-learn: *(gần giống OLS)*

> Lưu ý: Giá trị này phụ thuộc vào dữ liệu thực tế trong file `Hanoi_housing_dataset.csv`, và có thể thay đổi nếu dữ liệu thay đổi.

---

## 🧠 CÁC KỸ THUẬT SỬ DỤNG

- Làm sạch dữ liệu với `pandas`, `regex`
- Loại bỏ ngoại lệ bằng IQR
- Chuẩn hóa bằng `StandardScaler`
- Hồi quy tuyến tính với 3 cách:
  - Tự code Gradient Descent
  - Công thức OLS thống kê
  - LinearRegression từ scikit-learn
- Đánh giá mô hình bằng RMSE và MAE

---

## 📌 LƯU Ý

- Dữ liệu chỉ mang tính minh hoạ, không phản ánh giá thị trường thực tế.
- Phù hợp để học và so sánh các kỹ thuật hồi quy tuyến tính.

---

## 👨‍💻 TÁC GIẢ

**Codeaholic65L1 Team** — Dự án minh hoạ thực tiễn các phương pháp Linear Regression.
