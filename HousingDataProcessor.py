import pandas as pd
import numpy as np
import re
from sklearn.preprocessing import StandardScaler

class HousingDataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.scaler_x = StandardScaler()
        self.scaler_y = StandardScaler()

    @staticmethod
    def clean_price(value):
        if isinstance(value, str):
            value = re.sub(r"[^0-9,\.]", "", value.strip())
            value = value.replace(",", ".")
            try:
                return float(value)
            except:
                return np.nan
        return np.nan

    def load_and_process(self):
        df = pd.read_csv(self.file_path)[['Giá/m2', 'Diện tích']].dropna()

        # tach don vi tien te
        df['unit'] = df['Giá/m2'].apply(lambda x: 'triệu' if 'triệu' in x else ('tỷ' if 'tỷ' in x else None))
        df = df[df['unit'].notna()]
        df['value'] = df['Giá/m2'].apply(self.clean_price)
        df = df.dropna(subset=['value'])

        df['price_per_m2'] = df.apply(
            lambda row: row['value'] * 1e6 if row['unit'] == 'triệu' else row['value'] * 1e9, axis=1
        )

        df['area'] = (
            df['Diện tích']
            .astype(str)
            .str.replace(" m²", "", regex=False)
            .str.replace(",", ".")
            .apply(self.clean_price)
        )
        df = df.dropna(subset=['area'])

        # Loc dien tich va gia
        df = df[df['area'] > 10]

        q1_area, q3_area = df['area'].quantile([0.25, 0.75])
        iqr_area = q3_area - q1_area
        upper_area = q3_area + 1.5 * iqr_area
        df = df[df['area'] <= upper_area]

        df = df[df['price_per_m2'] < df['price_per_m2'].quantile(0.99)]

        # save data goc
        self.x_real = df['area'].values.reshape(-1, 1)
        self.y_real = df['price_per_m2'].values.reshape(-1, 1)

        # chuan hoa
        self.x_scaled = self.scaler_x.fit_transform(self.x_real).flatten()
        self.y_scaled = self.scaler_y.fit_transform(self.y_real).flatten()

    def get_scaled_data(self):
        return self.x_scaled, self.y_scaled

    def get_real_data(self):
        return self.x_real.flatten(), self.y_real.flatten()

    def inverse_predict(self, y_scaled):
        return self.scaler_y.inverse_transform(np.array(y_scaled).reshape(-1, 1)).flatten()

    def transform_area(self, area):
        return self.scaler_x.transform(np.array([[area]])).flatten()
