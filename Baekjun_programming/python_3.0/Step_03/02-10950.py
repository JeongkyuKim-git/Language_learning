# Baekjun_Programming

# Title : A + B - 3
# C:\Users\jkkim\PycharmProjects\Beckjun
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------------------------------
#  03-02-10950-Programming
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
#  요구 사항 : 시간 제한 (1 초), 메모리 제한 (256 MB), 정답 비율 (59.495 %)
#  문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
#  입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#        각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#  출력 : 각 테스트 케이스마다 A+B를 출력한다.
#  예제 입력 : 5 <-- case 5
#             1 1
#             2 3
#             3 4
#             9 8
#             5 2
#  예제 출력 : 2
#             5
#             7
#             17
#             7
# -----------------------------------------------------------------------------------------------------------
testset = int(input())
for i in range(testset):
    A, B = map(int, input().split())
    print(A + B)
