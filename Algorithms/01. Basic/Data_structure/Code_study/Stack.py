# 재귀함수
def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data-1)
        print("returned", data)


recursive(999)

# python에서는 재귀는 1000번까지만 동작한다.
# 실제 오류나는 1000 = 1001개 0포함
# recursive(1000)

# -----------------------------------

"""
파이썬 리스트 기능에서 제공하는 메서드로 스택 사용.
"""

data_stack = list()

data_stack.append(1)
data_stack.append(2)

print(data_stack)
print(data_stack.pop())

# -------------------------------

"""
리스트 변수로 스택을 다루는 pop, push 기능 구현
"""

stack_list = list()


def push(data):
    stack_list.append(data)


def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data


for index in range(10):
    push(index)

# [0,1,2,3,4,5,6,7,8,9]
# pop --> 9 마지막에 저장된 것이 출력됨
print(pop())
