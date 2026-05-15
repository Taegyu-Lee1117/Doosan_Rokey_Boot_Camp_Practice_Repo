# 문제 3 (실습 문제 - Numpy 조건 연산: 불리언 인덱싱)
# - 아래 주어진 Numpy 배열 scores에서 80점 이상인 점수들만 추출하여 출력하시오. 
# (힌트: 불리언 인덱싱/마스킹 사용)
import numpy as np

scores = np.array([75, 90, 82, 65, 95, 78, 88])

# 여기에 코드를 작성하세요
# 80점 이상인 점수들만 출력
high_scores = scores[scores >= 80]
print(high_scores)