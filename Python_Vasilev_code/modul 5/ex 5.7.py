n = 100

D = {s for s in range(1,n+1) if (s%5 == 2 or s%5 == 4) and s%7 == 3 and s%3 != 1}

print("Приведенные ниже числа от 1 до ",n)
print("1) при делении на 5 дают в остатке 2 или 4;")
print("2) при делении на 7 дают в остатке 3;")
print("3) при делении на 3 не дают в остатке 1;")
print(D)