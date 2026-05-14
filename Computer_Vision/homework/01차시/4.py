# - 두 개의 숫자 a와 b를 인자로 받아, 
# $a^2 + b$ (a의 제곱 더하기 b)를 계산하여 
# 반환(return)하는 함수 calc_func(a, b)를 정의하시오.

# 여기에 함수를 정의하세요
def calc_func(a, b):
    return a ** 2 + b


# --- 테스트 코드 (수정 불필) ---
result = calc_func(5, 10)
print(f"5^2 + 10 = {result}")  # 예상 출력: 5^2 + 10 = 35