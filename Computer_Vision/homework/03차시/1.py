# 문제 1 (실습 문제 - 텐서 생성 및 속성 확인)
# - 파이썬 2차원 리스트 data = [[10, 20], [30, 40], [50, 60]]를 사용하여 PyTorch 텐서 x를 생성하시오.
# - 그 다음, x의 자료형(dtype)과 모양(shape)을 출력하는 코드를 작성하시오.

import torch

data = [[10, 20], [30, 40], [50, 60]]

# 여기에 코드를 작성하세요
# 1. 텐서 생성
x = torch.tensor(data)

# 2. 자료형(dtype) 출력
print(f"Tensor Dtype: {x.dtype}")

# 3. 모양(shape) 출력
print(f"Tensor Shape: {x.shape}")