print("mod/mod1.py 시작")

PI = 3.14 # 변수

def add(x, y):
    """두 수를 더하는 함수"""
    return x + y

def sub(x, y):
    """두 수를 빼는 함수"""
    return x - y    

def mul(x, y):
    """두 수를 곱하는 함수"""
    return x * y    

def div(x, y):
    """두 수를 나누는 함수"""
    if y == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return x / y

print("mod/mod1.py 끝")
