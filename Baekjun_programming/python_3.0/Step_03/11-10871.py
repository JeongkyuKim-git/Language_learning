# Baekjun_Programming

# Title : x보다 작은 수
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  03-11-10871-Programming
#
#  Author       : Jeongkyu Kim
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 0.1
#  Rev. Date    : July. 17, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.0
#   - Site url : Refer to https://www.acmicpc.net/step/1
#  
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (256 MB), 정답 비율 (56.758 %)
#  문제 : 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
#
#  입력 : 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
#         둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
#  출력 : X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.
#  예제 입력 : 10 5
#             1 10 4 9 2 3 8 5 7 6
#  예제 출력 : 1 4 2 3
# -----------------------------------------------------------------------------------------------------------
import sys

# n (number)
number = sys.stdin.readline()
x_number = sys.stdin.readline()
Arr = list(sys.stdin.readline().split())

print(Arr)

for i in Arr:
    if i < x_number:
        print(i, end=" ")
