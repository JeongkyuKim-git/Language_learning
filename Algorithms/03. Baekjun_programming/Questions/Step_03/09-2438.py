# Baekjun_Programming

# Title : 별 찍기-1
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  03-09-2438-Programming
#
#  Author       : Jeongkyu Kim
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 0.1
#  Rev. Date    : July. 16, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.0
#   - Site url : Refer to https://www.acmicpc.net/step/1
#  
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (128 MB), 정답 비율 (62.169 %)
#  문제 : 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#
#  입력 : 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#  출력 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
#  예제 입력 : 5
# 예제 출력 : *
#            **
#            ***
#            ****
#            *****
# -----------------------------------------------------------------------------------------------------------

import sys

number = sys.stdin.readline()

for i in range(0,int(number)):
    for j in range(i+1):
        print("*", end="")
    print("")
