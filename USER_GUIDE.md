# Hướng Dẫn Triển Khai Project Dự Đoán Giá Nhà

---

## 1. Yêu cầu trước khi bắt đầu

- Máy tính đã cài **Python phiên bản mới nhất** (khuyến nghị Python 3.8 trở lên).
- Có kết nối Internet để cài đặt các thư viện cần thiết.
- Có thể mở được terminal (Command Prompt, PowerShell trên Windows hoặc Terminal trên macOS/Linux).

---

## 2. Tải project và giải nén

1. Ngay tại repo **HousePricePrediction** Nhấn nút **Code** (màu xanh lá) → chọn **Download ZIP**.
2. File ZIP sẽ được tải về máy tính, thường có tên `HousePricePrediction-main.zip`.
3. Giải nén file ZIP vừa tải để được thư mục `HousePricePrediction-main`.
   - Trên Windows: nhấp chuột phải vào file ZIP → chọn **Extract All...** → chọn vị trí giải nén → bấm **Extract**.
   - Trên macOS/Linux: nhấp chuột phải → chọn **Giải nén** hoặc dùng lệnh terminal `unzip HousePricePrediction-main.zip`.
4. Sau khi giải nén, bạn sẽ có thư mục `HousePricePrediction-main` chứa toàn bộ mã nguồn và file dữ liệu.

---

## 3. Mở Terminal và chuyển đến thư mục project

1. **Mở Terminal**  
   - Trên **Windows**: Nhấn `Win + R`, gõ `cmd`.
   - Trên **macOS/Linux**: Mở ứng dụng **Terminal**.

2. **Copy đường dẫn đầy đủ của thư mục project**  
   - Mở thư mục `HousePricePrediction-main` vừa giải nén trên máy tính.  
   - Click vào thanh địa chỉ của cửa sổ thư mục, **copy toàn bộ đường dẫn**.  
     
     Ví dụ:  
     - Windows:  
       `C:\Users\Username\Downloads\HousePricePrediction-main`  
     - macOS/Linux:  
       `/Users/username/Downloads/HousePricePrediction-main`

3. **Chuyển đến thư mục project trong Terminal**  
   - Quay lại cửa sổ Terminal, gõ lệnh sau rồi nhấn Enter:  
     ```bash
     cd "đường_dẫn_bạn_vừa_copy"
     ```  
     
     Ví dụ:  
     ```bash
     cd "C:\Users\Username\Downloads\HousePricePrediction-main"
     ```
     
4. **Kiểm tra bạn đã vào đúng thư mục**  
   - Windows:  
     ```bash
     dir
     ```  
   - macOS/Linux:  
     ```bash
     ls
     ```  
   Bạn sẽ thấy các file như `App.py`, `Hanoi_housing_dataset.csv`, v.v.

---

## 4. Cài đặt các thư viện cần thiết

Trong terminal (vẫn đang ở thư mục project), chạy lệnh sau để cài đặt tất cả thư viện cần thiết:

```bash
pip install pandas numpy matplotlib scikit-learn streamlit
```

---

## 5. Chạy ứng dụng

Trong terminal (vẫn ở thư mục project), chạy lệnh sau để khởi động ứng dụng:

```bash
streamlit run App.py
```

---



