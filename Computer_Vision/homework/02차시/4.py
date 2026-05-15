# 문제 4 (실습 문제 - Numpy 집계 함수)
# - 아래 주어진 2차원 Numpy 배열 data를 사용하여, 다음 두 가지 값을 계산하고 출력하시오.

# 1. 배열 data의 전체 합계 (모든 요소의 합)
# 2. 배열 data의 각 열(column)의 평균 (힌트: axis 인자 사용)

import numpy as np

data = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

# 여기에 코드를 작성하세요
# 1. 전체 합계
total_sum = data.sum()
print(f"전체 합계: {total_sum}")

# 2. 각 열의 평균
col_mean = data.mean(axis = 0)
print(f"각 열의 평균: {col_mean}")