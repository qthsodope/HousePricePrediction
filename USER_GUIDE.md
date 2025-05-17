# 🏡 Hướng Dẫn Triển Khai Project Dự Đoán Giá Nhà

---

## 1. Yêu cầu trước khi bắt đầu

- Máy tính đã cài **Python 3.8 trở lên**
- Có kết nối Internet để cài đặt thư viện
- Biết cách mở **Terminal** (Command Prompt, PowerShell trên Windows hoặc Terminal trên macOS/Linux)

---

## 2. Tải project và giải nén

1. Truy cập repo **HousePricePrediction** → nhấn **Code** → **Download ZIP**
2. Giải nén file `.zip` để thu được thư mục `HousePricePrediction-main`
   - Windows: nhấp chuột phải → **Extract All...**
   - macOS/Linux: nhấp chuột phải → **Giải nén** hoặc dùng lệnh `unzip`

---

## 3. Mở Terminal và chuyển đến thư mục project

```bash
# Mở Terminal và chuyển đến thư mục vừa giải nén
cd "đường_dẫn_đến_thư_mục_HousePricePrediction-main"

# Ví dụ:
cd "C:\Users\TenUser\Downloads\HousePricePrediction-main"

# Kiểm tra bạn đã vào đúng thư mục
# Windows:
dir

# macOS/Linux:
ls
```

---

## 4. Cài đặt các thư viện cần thiết

```bash
pip install pandas numpy matplotlib scikit-learn streamlit
```

---

## 5. Chạy project

### ▶️ Cách 1: Giao diện Web với Streamlit (GUI)

```bash
streamlit run App.py
```

- Trình duyệt sẽ mở ra giao diện để bạn nhập diện tích và xem dự đoán giá.
- Có biểu đồ trực quan và so sánh 3 phương pháp hồi quy.

---

### ▶️ Cách 2: Chạy trong Terminal bằng `Main.py`

```bash
python Main.py
```

Bạn sẽ thấy:

- Kết quả đánh giá mô hình (RMSE, MAE)
- Vòng lặp cho phép nhập diện tích bất kỳ và in ra dự đoán giá/m²

Ví dụ:

```text
Nhập diện tích cần dự đoán (hoặc gõ 'quit' để thoát): 80
→ Dự đoán giá/m² cho nhà 80 m²: 46,123,456 VND/m²
```

Gõ `"quit"` để thoát khỏi chương trình.

---

- **App.py**: dùng để chạy ứng dụng Web, phù hợp cho người dùng không chuyên kỹ thuật
- **Main.py**: chạy trong Terminal, phù hợp để kiểm thử, đánh giá mô hình, hoặc chạy nhanh

Bạn có thể chọn cách chạy phù hợp với nhu cầu của mình.
