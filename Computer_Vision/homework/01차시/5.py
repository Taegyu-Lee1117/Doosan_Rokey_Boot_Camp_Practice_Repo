# - 'f 문자열의 상세 옵션'을 참고하여, 
# f-string을 사용해 변수 val1과 val2를 아래의 요구사항에 맞게 포맷팅하여 
# str_result 변수에 할당하시오. 

# - 요구사항 1. val1 (float): 소수점 이하 두 번째 자리까지만 표시 
# 2. val2 (int): 총 5자리로 표시하되, 빈자리는 0으로 채움

val1 = 3.14159265
val2 = 42

str_result = f"val1 = {val1:.2f}, val2 = {val2:05d}" # 여기에 f-string을 작성하여 할당하세요

# --- 테스트 코드 (수정 불필) ---
print(str_result)
# 예상 출력: val1 = 3.14, val2 = 00042