numbers = set(range(1,10001))
generated_num = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)  
    generated_num.add(i)

selfnum = sorted(numbers - generated_num)
for i in selfnum:
    print(i)