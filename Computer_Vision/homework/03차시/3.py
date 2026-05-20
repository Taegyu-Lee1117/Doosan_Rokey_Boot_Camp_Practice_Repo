# 문제 3 (실습 문제 - 자동 미분 Autograd)

# PyTorch의 자동 미분(Autograd) 기능을 사용하여, $y = 3x^2 + 2$ 함수에 대해 $x=4.0$ 일 때의 미분 값($\frac{dy}{dx}$)을 계산하시오.
# (참고: $y' = 6x$ 이므로, $x=4.0$ 일 때 정답은 24.0 입니다.)

# 요구사항
# - x 텐서를 생성할 때, requires_grad=True 속성을 설정해야 합니다. (자료형은 float 이어야 함)
# - y를 계산합니다.
# - y.backward()를 호출하여 경사를 계산합니다.
# - x.grad에 저장된 미분 값을 출력합니다.

import torch

# 여기에 코드를 작성하세요
# 1. x 텐서 생성 (값: 4.0, 경사 추적 활성화)
x = torch.tensor(4.0, requires_grad=True)

# 2. y 계산
y = 3 * x ** 2 + 2

# 3. 경사 계산
y.backward()

# 4. x의 미분 값 출력
print(f"x=4.0 에서의 미분 값: {x.grad}")