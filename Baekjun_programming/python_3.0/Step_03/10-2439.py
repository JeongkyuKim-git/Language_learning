# Baekjun_Programming

# Title : 별 찍기-2
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  03-10-2439-Programming
#
#  Author       : Jeongkyu Kim
#  E-mail       : jkkim@mme.dongguk.edu
#  Version      : 0.1
#  Rev. Date    : July. 22, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.0
#   - Site url : Refer to https://www.acmicpc.net/step/1
#  
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (128 MB), 정답 비율 (58.607 %)
#  문제 : 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#         하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
#
#  입력 : 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#  출력 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
#  예제 입력 : 5
#  예제 출력 :      *
#                 **
#                ***
#               ****
#              *****
# -----------------------------------------------------------------------------------------------------------
import sys

number = sys.stdin.readline()

for i in range(1,int(number)+1):
    print(" "*(int(number)-i)+"*"*i)
