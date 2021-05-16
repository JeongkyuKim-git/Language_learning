# Baekjun_Programming

# Title : 시험 성적
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  02-02-9498-Programming
#
#  Author       : Jeongkyu Kim
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 0.1
#  Rev. Date    : July. 15, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.0
#   - Site url : Refer to https://www.acmicpc.net/step/1
#  
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (128 MB), 정답 비율 (59.013 %)
#  문제 : 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
#
#  입력 : 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
#  출력 : 시험 성적을 출력한다.
#  예제 입력 : 100
#  예제 출력 :  A
# -----------------------------------------------------------------------------------------------------------

A = int(input())
if 101 > A >= 90: print('A')
elif 90 > A >= 80: print('B')
elif 80 > A >= 70: print('C')
elif 70 > A >= 60: print('D')
else: print('F')
