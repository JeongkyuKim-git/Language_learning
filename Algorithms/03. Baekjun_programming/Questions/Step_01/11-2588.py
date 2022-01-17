# Baekjun_Programming

# Title : 곱셈(multiple)
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  01-11-2588-Programming
#
#  Author       : Jeongkyu Kim
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 0.1
#  Rev. Date    : July. 13, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.0
#   - Site url : Refer to https://www.acmicpc.net/step/1
#  
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (128 MB), 정답 비율 (54.256 %)
#  문제 : 세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
#         4 7 2 .... (1)
#       x 3 8 5 .... (2)
#   -----------------
#       2 3 6 0 .... (3)
#     3 7 7 6   .... (4)
#   1 4 1 6     .... (5)
#   -----------------
#   1 8 1 7 2 0 .... (6)
#  (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
#
#  입력 : 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
#  출력 : 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.
#  예제 입력 : 472
#             385
#  예제 출력 :  2360
#              3776
#              1416
#              181720
#
# -----------------------------------------------------------------------------------------------------------

# Step_1 주석은 보기 예시와 동일하게 출력하기 위한 문장 및 계산과정을 보여준다.
"""
import math

A,B = map(int,input().split())

units = (B%10)
tens = (B%100)/10
hundread = (B)/100

calculate_units = units * A
calculate_tens = math.trunc(tens) * A
calculate_hundread = math.trunc(hundread) * A
sum = calculate_units + (calculate_tens * 10) + (calculate_hundread * 100)

print(' ',calculate_units)
print('',calculate_tens)
print(calculate_hundread)
print(sum)
"""

# Step_2 두개의 A,B를 동시에 받기 위한 방법이다.
"""
A,B = map(int,input().split())
print("%d\n%d\n%d\n%d"%((A * (B%10)),(A * ((B%100)//10)),(A * (B//100)),(A*B)))
"""

# Step_3 백준에서 'running time' 문제로 인해 바로 출력하기 위한 문장
A =int(input())
B =int(input())
print("%d\n%d\n%d\n%d"%((A * (B%10)),(A * ((B%100)//10)), (A * (B//100)),(A*B)))
