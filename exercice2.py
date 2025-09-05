def est_premier(n):
    if n < 2:
        return False
    for i in range(2,n):
            if n % i== 0:
                return False
    return True
print("les nombres premier sont:")
for i in range(2,101):
    if est_premier(i):
        print(i)

print("les nombres non premier sont")