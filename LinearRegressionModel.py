import numpy as np
from sklearn.linear_model import LinearRegression

class LinearRegressionModel:
    def __init__(self, alpha=1e-2, epochs=4000):
        self.alpha = alpha
        self.epochs = epochs
        self.w = 0.0
        self.b = 0.0
        self.model_sk = None
        self.x = None
        self.y = None

    def set_data(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)

    def train_gradient_descent(self):
        self.w, self.b = 0.0, 0.0
        for _ in range(self.epochs):
            y_pred = self.w * self.x + self.b
            error = y_pred - self.y
            dw = (2 / self.n) * np.sum(error * self.x)
            db = (2 / self.n) * np.sum(error)
            self.w -= self.alpha * dw
            self.b -= self.alpha * db
        return self.w, self.b

    def predict_gradient(self, x_new):
        return self.w * x_new + self.b

    def xstk_regression(self):
        x_mean = np.mean(self.x)
        y_mean = np.mean(self.y)
        w = np.sum((self.x - x_mean) * (self.y - y_mean)) / np.sum((self.x - x_mean) ** 2)
        b = y_mean - w * x_mean
        return w, b

    def predict_xstk(self, x_new, w, b):
        return w * x_new + b

    def sklearn_regression(self):
        self.model_sk = LinearRegression()
        self.model_sk.fit(self.x.reshape(-1, 1), self.y)
        return self.model_sk.coef_[0], self.model_sk.intercept_

    def predict_sklearn(self, x_new):
        return self.model_sk.predict(x_new.reshape(-1, 1))
