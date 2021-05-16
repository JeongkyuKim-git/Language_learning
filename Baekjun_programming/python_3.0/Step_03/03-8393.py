# Baekjun_Programming

# Title : 합
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  03-03-8393-Programming
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
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (128 MB), 정답 비율 (70.245 %)
#  문제 : n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
#
#  입력 : 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
#  출력 : 1부터 n까지 합을 출력한다.
#  예제 입력 : 3
#  예제 출력 : 6
# -----------------------------------------------------------------------------------------------------------

n = int(input())
for i in range(n):
    n = n + i
print(n)
