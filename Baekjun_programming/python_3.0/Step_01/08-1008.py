# Baekjun_Programming

# Title : A/B
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  01-08-1008-Programming
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
#  요구 사항 : 시간 제한 (2 초), 메모리 제한 (128 MB), 정답 비율 (33.285 %)
#  문제 : 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.
#
#  입력 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
#  출력 : 첫째 줄에 A/B를 출력한다.
#  예제 입력_1 : 1 3
#  예제 출력_2 : 0.33333333333333333333333333333333
#  예제 입력_1 : 4 5
#  예제 출력_2 : 0.8
#
# -----------------------------------------------------------------------------------------------------------

A, B = input().split()
div = int(A) / int(B)
print(div)
