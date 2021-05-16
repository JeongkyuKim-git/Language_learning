# Baekjun_Programming

# Title : A + B -5
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  04-01-10952-Programming
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
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (256 MB), 정답 비율 (54.639 %)
#  문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
#  입력 : 입력은 여러 개의 테스트 케이스로 이루어져 있다.
#  각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#  입력의 마지막에는 0 두 개가 들어온다.
#
#  출력 : 각 테스트 케이스마다 A+B를 출력한다.
#  예제 입력 : 1 1
#             2 3
#             3 4
#             9 8
#             5 2
#             0 0
#  예제 출력 : 2
#             5
#             7
#             17
#             7
# -----------------------------------------------------------------------------------------------------------
import sys

while True:
    number = list(map(int,sys.stdin.readline().split()))
    Result = number[0] + number[1]
    if (number[0] == 0 and number[1] == 0):
        break
    else : print(Result)
    number.clear()
