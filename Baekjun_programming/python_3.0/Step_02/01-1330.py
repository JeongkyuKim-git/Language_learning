# Baekjun_Programming

# Title : 두 수 비교하기
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  02-01-1330-Programming
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
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (512 MB), 정답 비율 (53.433 %)
#  문제 : 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
#
#  입력 : 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
#  출력 : 첫째 줄에 다음 세 가지 중 하나를 출력한다.
#       * A가 B보다 큰 경우에는 '>'를 출력한다.
#       * A가 B보다 작은 경우에는 '<'를 출력한다.
#       * A와 B가 같은 경우에는 '=='를 출력한다.
#  예제 입력_01 : 1 2
#  예제 출력_01 :  <
#  예제 입력_02 : 10 2
#  예제 출력_02 :  >
#  예제 입력_03 : 5 5
#  예제 출력_03 :  =
# -----------------------------------------------------------------------------------------------------------

A, B = map(int,input().split())
if A>B: print('>')
elif A<B: print('<')
else: print('==')
