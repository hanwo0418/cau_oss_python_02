# arithmetic_ops 함수는 사용자에게 정수 2개를 입력받고 연산
def arithmetic_ops(op):
    num1 = int(input("input 1st number: "))
    num2 = int(input("input 2nd number: "))
    return num1, num2, op(num1, num2)

def add(x, y): return x + y
def sub(x, y): return x - y

while True:
        op = input("input operation: ")
        if op == "end":
            break  # end 입력 시 반복을 종료
        elif op == "+":
            num1, num2, ret = arithmetic_ops(add)
        elif op == "-":
            num1, num2, ret = arithmetic_ops(sub)
        elif op == "*":
            num1, num2, ret = arithmetic_ops(lambda x, y: x * y)
        elif op == "/":
            num1, num2, ret = arithmetic_ops(lambda x, y: x / y)
        elif op == "%":
            num1, num2, ret = arithmetic_ops(lambda x, y: x % y)
        else:
            print("Invalid operation")
            continue # Invalid operation이므로 연산결과를 출력하지 않고 처음부터 반복
        print(f"{num1} {op} {num2} = {ret}")

print("Exit program")
