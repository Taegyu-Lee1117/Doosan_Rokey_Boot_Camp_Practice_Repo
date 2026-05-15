# 문제 6 (실습 문제 - Matplotlib 그래프 꾸미기)
# - 아래 주어진 x 데이터와 y (sin 함수) 데이터를 사용하여 산점도(scatter plot)를 그리되, 
# 다음 요구사항에 맞게 그래프를 꾸미고 plt.show()로 출력하시오.

# - 그래프 제목(Title): 'Sine Wave Scatter Plot'
# - X축 라벨(Label): 'X value'
# - Y축 라벨(Label): 'Y value (sin(x))'

import numpy as np
import matplotlib.pyplot as plt

# 데이터 (수정 불필요)
x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)

# 1. 산점도 그리기
plt.scatter(x, y)

# 2. 제목 추가
plt.title('Sine Wave Scatter Plot')
# 3. X축 라벨 추가
plt.xlabel('X value')
# 4. Y축 라벨 추가
plt.ylabel('Y value (sin(x))')

# 5. 그래프 출력
plt.show()