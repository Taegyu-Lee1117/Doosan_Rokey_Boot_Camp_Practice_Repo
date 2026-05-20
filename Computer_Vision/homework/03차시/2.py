# 문제 2 (실습 문제 - 텐서 연산)
# - 다음 두 PyTorch 텐서 a와 b가 주어졌을 때, 두 텐서의 요소별 곱셈(element-wise multiplication) 결과와 행렬 곱셈(matrix multiplication) 결과를 각각 계산하여 출력하시오.

import torch

a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[10, 20], [30, 40]])

# 여기에 코드를 작성하세요
# 1. 요소별 곱셈 (a * b)
element_wise_mul = a * b
print(f"요소별 곱셈:\n{element_wise_mul}")

# 2. 행렬 곱셈 (a @ b 또는 torch.matmul(a, b))
matrix_mul = torch.matmul(a,b)
print(f"행렬 곱셈:\n{matrix_mul}")