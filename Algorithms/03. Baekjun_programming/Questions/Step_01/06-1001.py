# Baekjun_Programming

# Title : A-B
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  01-06-1001-Programming
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
#  요구 사항 : 시간 제한 (2 초), 메모리 제한 (128 MB), 정답 비율 (72.149 %)
#  문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
#  입력 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
#  출력 : 첫째 줄에 A-B를 출력한다.
#  예제 입력 : 3 2
#  예제 출력 : 1
#
# -----------------------------------------------------------------------------------------------------------

A, B = input().split()
sub = int(A) - int(B)
print(sub)
