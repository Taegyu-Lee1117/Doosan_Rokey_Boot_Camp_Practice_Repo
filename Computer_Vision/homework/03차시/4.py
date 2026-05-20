# 문제 4 (실습 문제 - 다중 변수 자동 미분)

# $z = 4a + 5b^2$ 함수가 있을 때, $a=2.0$, $b=3.0$ 일 때의 각 변수에 대한 편미분 값($\frac{\partial z}{\partial a}$ 와 $\frac{\partial z}{\partial b}$)을 계산하시오.

# (참고: $\frac{\partial z}{\partial a} = 4$, $\frac{\partial z}{\partial b} = 10b = 30$)

import torch

# 여기에 코드를 작성하세요
# 1. a, b 텐서 생성 (경사 추적 활성화)
a = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(3.0, requires_grad=True)

# 2. z 계산
z = 4 * a + 5 * b ** 2

# 3. 경사 계산
z.backward()

# 4. a와 b의 편미분 값 출력
print(f"a에 대한 편미분 값: {a.grad}")
print(f"b에 대한 편미분 값: {b.grad}")