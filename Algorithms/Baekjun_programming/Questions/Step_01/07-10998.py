# Baekjun_Programming

# Title : AxB
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  01-07-10998-Programming
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
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (256 MB), 정답 비율 (77.690 %)
#  문제 : 두 정수 A와 B를 입력받은 다음, AxB를 출력하는 프로그램을 작성하시오.
#
#  입력 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
#  출력 : 첫째 줄에 AxB를 출력한다.
#  예제 입력 : 1 2
#  예제 출력 : 2
#
# -----------------------------------------------------------------------------------------------------------

A, B = input().split()
mul = int(A) * int(B)
print(mul)
