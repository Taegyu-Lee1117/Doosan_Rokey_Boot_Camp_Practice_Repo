# 문제 5 (실습 문제 - Matplotlib 기본 라인 플롯)
# - Numpy를 사용하여 0부터 10까지 0.1 간격의 x 배열을 생성하고, y=x2 (x의 제곱) 값을 계산하시오.
# - x와 y를 사용하여 Matplotlib으로 라인 플롯(line plot)을 그리고 plt.show()로 그래프를 출력하시오.

import numpy as np
import matplotlib.pyplot as plt

# 여기에 코드를 작성하세요
# 1. x, y 데이터 생성
# (x는 0부터 10까지 0.1 간격, y는 x의 제곱)
x = np.arange(0, 10.1, 0.1)
y = x ** 2

# 2. 라인 플롯 생성
plt.plot(x, y)

# 3. 그래프 출력
plt.show()