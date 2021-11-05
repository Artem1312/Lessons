A = {1,2,3,4}
B = {3,4,5,6}

print("Множество A: ",A)
print("Множество B: ",B)

C = A|B
print("Множество C = A|B:",C)

print("Множество A.union(B)", A.union(B))
print("Множество B.union(A)", B.union(A))

A.update(B)
print("Множество A: ",A)

B = B | {-1,-2,-3}
print("Множество B: ",B)

C|={7,8,9}
print("Множество C: ",C)
