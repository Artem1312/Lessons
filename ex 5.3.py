A = {1,2,3,4}
B = {3,4,5,6}

print("Множество A: ",A)
print("Множество B: ",B)

C = A&B
print("Множество C = A&B: ",C)

print("Множество A.intersection(B)", A.intersection(B))
print("Множество B.intersection(A)", B.intersection(A))

A.intersection_update(B)
print("Множество A: ",A)

B = B&{4,6,8,10}
print("Множество B: ",B)

C&={1,2,3}
print("Множество C: ",C)
