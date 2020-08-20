print('A')
A = [38, 21, 54, 62, 19]
smallestA = A[0]
for i in A:
    if i < smallestA:
        smallestA = i

print('smallest\'s A :', smallestA)

largestA = A[0]
for i in A:
    if i > largestA:
        largestA = i

print('largest\'s A :', largestA)
print()

print('B')
B = [12, 24, 1, 55, 922]
B.sort()
smallestB = B[0]
print('smallestB :', smallestB)

B.sort(reverse=True)
largestB = B[0]
print('largestB :', largestB)
print()

print('C')
C = [3, 77, 2, 3, 98]
print('smallestC :', min(C))
print('largestC :', max(C))

print('A의 합계 구하기')
sumA = 0
for i in A:
    sumA += i

print('A의 합은', sumA)
print()

print('B의 합 구하기')
print(sum(B))
print()
