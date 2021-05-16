# Baekjun_Programming

# Title : 사칙연산(calculator)
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  01-09-10869-Programming
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
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (256 MB), 정답 비율 (54.447 %)
#  문제 : 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
#  입력 : 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
#  출력 : 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
#  예제 입력 : 7 3
#  예제 출력 : 10
#              4
#             21
#              2
#              1
#
# -----------------------------------------------------------------------------------------------------------

import math
A, B = input().split()

div = float(A) / float(B)
mul = int(A) * int(B)
sub = int(A) - int(B)
sum = int(A) + int(B)

# remainder
rem = int(A) % int(B)

print(sum,'\n',sub,'\n',mul,'\n',math.trunc(div),'\n',rem)
