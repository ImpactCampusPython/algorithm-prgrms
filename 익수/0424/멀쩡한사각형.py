# 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048
import math

def solution(w,h):
    return w*h -(w+h - math.gcd(w,h))

