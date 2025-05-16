import numpy as np
import matplotlib.pyplot as plt
from HousingDataProcessor import HousingDataProcessor
from LinearRegressionModel import LinearRegressionModel

def evaluate_and_predict(w, b, x_scaled, y_real, processor, label):
    y_pred_scaled = w * x_scaled + b
    y_pred_real = processor.inverse_predict(y_pred_scaled)

    # tinh RMSE n MAE thu cong
    rmse = np.sqrt(np.mean((y_real - y_pred_real) ** 2))
    mae = np.mean(np.abs(y_real - y_pred_real))

    print(f"[{label}] w = {w:.4f}, b = {b:.4f}")
    print(f"→ RMSE: {rmse:,.0f} VND/m² | MAE: {mae:,.0f} VND/m²")
    return y_pred_real

def main():
    # B1: Load va xu ly data
    processor = HousingDataProcessor("Hanoi_housing_dataset.csv")
    processor.load_and_process()
    x_scaled, y_scaled = processor.get_scaled_data()
    x_real, y_real = processor.get_real_data()

    # B2: Train model (gradient descent, cong thuc xstk, sklearn)
    model = LinearRegressionModel()
    model.set_data(x_scaled, y_scaled)

    w_gd, b_gd = model.train_gradient_descent()
    w_ols, b_ols = model.xstk_regression()
    w_sk, b_sk = model.sklearn_regression()

    print("\t KẾT QUẢ HỒI QUY \t")
    y_gd_real = evaluate_and_predict(w_gd, b_gd, x_scaled, y_real, processor, "Gradient Descent")
    print("\n")
    y_ols_real = evaluate_and_predict(w_ols, b_ols, x_scaled, y_real, processor, "CT XSTK")
    print("\n")
    y_sk_real = evaluate_and_predict(w_sk, b_sk, x_scaled, y_real, processor, "Scikit-learn")

    # check xstk vs sklearn
    # print("\n\t KIỂM CHỨNG CT XSTK \t")
    # diff_w = abs(w_ols - w_sk)
    # diff_b = abs(b_ols - b_sk)
    # print(f"Chênh lệch hệ số w: {diff_w:.10f}")
    # print(f"Chênh lệch hệ số b: {diff_b:.10f}")
    #
    # if diff_w < 1e-8 and diff_b < 1e-8:
    #     print("CT XSTK khớp với Scikit-learn OLS")
    # else:
    #     print("CT XSTK ko khớp")

    # B3: Bieu do
    x_line = np.linspace(min(x_scaled), max(x_scaled), 100)
    x_line_real = processor.scaler_x.inverse_transform(x_line.reshape(-1, 1)).flatten()
    y_line_gd = processor.inverse_predict(w_gd * x_line + b_gd)
    y_line_ols = processor.inverse_predict(w_ols * x_line + b_ols)
    y_line_sk = processor.inverse_predict(w_sk * x_line + b_sk)

    plt.figure(figsize=(10, 6))
    plt.scatter(x_real, y_real, s=10, alpha=0.2, label="Dữ liệu thực tế")
    plt.plot(x_line_real, y_line_gd, label="Gradient Descent")
    plt.plot(x_line_real, y_line_ols, label="CT XSTK")
    plt.plot(x_line_real, y_line_sk, label="Scikit-learn")
    plt.xlabel("Diện tích (m²)")
    plt.ylabel("Giá/m² (VND)")
    plt.title("So sánh 3 phương pháp hồi quy tuyến tính")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # B4: Test main voi dien tich cu the
    area = 500
    x_input = processor.transform_area(area)
    y_pred = processor.inverse_predict(w_gd * x_input + b_gd)[0]

    print(f"\n→ Dự đoán giá/m² cho nhà {area} m²: {y_pred:,.0f} VND/m²") # dung Gradient Descent

if __name__ == "__main__":
    main()

