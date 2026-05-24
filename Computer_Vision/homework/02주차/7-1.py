import numpy as np
import matplotlib.pyplot as plt

# 1. 가상의 데이터 생성 (독립변수 X, 종속변수 y)
np.random.seed(42)  # 일관된 결과를 위해 시드 고정
X = 2 * np.random.rand(50, 1)
# 실제 데이터 관계: y = 4 + 3X + 노이즈
y = 4 + 3 * X + np.random.randn(50, 1)

# 2. OLS(최소제곱법) 공식을 이용한 회귀계수 계산
# X의 평균, y의 평균 계산
X_mean = np.mean(X)
y_mean = np.mean(y)

# 기울기(w1)와 절편(w0) 계산
w1 = np.sum((X - X_mean) * (y - y_mean)) / np.sum((X - X_mean) ** 2)
w0 = y_mean - w1 * X_mean

# 3. 회귀직선 그리기 위한 예측 값 계산
X_line = np.linspace(0, 2, 100).reshape(-1, 1)
y_line = w0 + w1 * X_line

# 4. 그래프 시각화
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Actual Data (실제 데이터)')  # 산점도
plt.plot(X_line, y_line, color='red', linewidth=2, label=f'Linear Regression Line (y = {w0:.2f} + {w1:.2f}x)')  # 회귀직선
plt.title('Linear Regression Graph (OLS)', fontsize=14)
plt.xlabel('X (Independent Variable)', fontsize=12)
plt.ylabel('y (Dependent Variable)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()