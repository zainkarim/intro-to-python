# add one to each element of each sub-list
L = [[1,2,3],
     [4,5,6],
     [7,8,9]]

for i in range(0, len(L)):
    for j in range(0, len(L[i])):
        L[i][j] += 1
print(L)

for i in range(0, 5):
    for j in range(0, 5):
        print(i, j)
