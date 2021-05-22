# Baekjun_Programming

# Title : A + B -4
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  04-02-10951-Programming
#
#  Author       : Jeongkyu Kim
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 0.1
#  Rev. Date    : August. 07, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.0
#   - Site url : Refer to https://www.acmicpc.net/step/1
#  
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (256 MB), 정답 비율 (36.661 %)
#  문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
#  입력 : 입력은 여러 개의 테스트 케이스로 이루어져 있다.
#         각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
#  출력 : 각 테스트 케이스마다 A+B를 출력한다.
#  예제 입력 : 1 1
#             2 3
#             3 4
#             9 8
#             5 2
#  예제 출력 : 2
#             5
#             7
#             17
#             7
# -----------------------------------------------------------------------------------------------------------
# 문제를 해석하고 출력을 했을 경우 틀렸다고 하여, 어떤 문제가 있는지 생각했다.
# 1. 입력을 받자마자 에러가 난다고 가정했을때, 조건에 해당되는 B<10을 해야 종료되는 줄 알았지만 그렇지 않았다.
# 2. 다른 블로그의 참고를 해보니 에러가 나도 동작이 된다는 것에 의아한 문제이다.

# 1. 
"""
while True:
    number = list(map(int,sys.stdin.readline().split()))
    if (number[1] > 10):
        break
    else:
        Result = number[0] + number[1]
        print(Result)
    number.clear()
"""

# 2.
while True:
    try:
        A, B=map(int,input().split())
        print(A+B)
    except EOFError:
        break

