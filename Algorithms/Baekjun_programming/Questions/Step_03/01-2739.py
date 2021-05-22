# Baekjun_Programming

# Title : 구구단
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  03-01-2739-Programming
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
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (128 MB), 정답 비율 (53.785 %)
#  문제 : N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
#
#  입력 : 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.
#  출력 : 출력형식과 같게 N*1부터 N*9까지 출력한다.
#  예제 입력 : 2
#  예제 출력 : 2 * 1 = 2
#             2 * 2 = 4
#             2 * 3 = 6
#             2 * 4 = 8
#             2 * 5 = 10
#             2 * 6 = 12
#             2 * 7 = 14
#             2 * 8 = 16
#             2 * 9 = 18
# -----------------------------------------------------------------------------------------------------------

N = int(input())
for i in range(1,10):
    sum = N * i
    print(N, "*", i, "=", sum )
