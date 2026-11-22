import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
# Please write your code here.
INT_MAX = sys.maxsize
min_val = INT_MAX


for i in range(1, n-1):
    cpX = x[:]
    cpY = y[:]
    cpX.pop(i)
    cpY.pop(i)
    d = 0
    for j in range(n-2):
        l = abs(cpX[j] - cpX[j+1]) + abs(cpY[j] - cpY[j+1])
        d += l
    if min_val >= d :
        min_val = d
print(min_val)