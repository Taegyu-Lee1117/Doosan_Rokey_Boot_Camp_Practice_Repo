# 문제 1 (실습 문제 - Numpy 배열 생성 및 연산)

# 파이썬 리스트 [10, 20, 30, 40, 50]을 사용하여 x라는 이름의 Numpy 배열을 생성하시오.
# 그 다음, x의 모든 요소(element)에 5를 곱한 결과를 y라는 변수에 저장하고 y를 출력하시오.

import numpy as np

# 파이썬 리스트
list_x = [10, 20, 30, 40, 50]

# 1. list_x를 numpy 배열 x로 변환
x = np.array(list_x)

# 2. x의 모든 요소에 5를 곱하여 y에 저장
y = x * 5

# 3. y 출력
print(y)