# Baekjun_Programming

# Title : 나머지(remainder)
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  01-10-10430-Programming
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
#  문제 : 
#  (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
#  (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
#
#  입력 : 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
#  출력 : 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
#  예제 입력 : 5 8 4
#  예제 출력 :  1
#              1
#              0
#              0
#
# -----------------------------------------------------------------------------------------------------------

A,B,C= map(int,input().split())

print((A+B)%C)
print(((A%C) + (B%C))%C)
print(((A*B)%C))
print(((A%C) * (B%C))%C)
