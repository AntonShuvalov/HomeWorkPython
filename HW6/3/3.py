# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

import math
res = []
for i in range(1, 12):
    for j in range(1, i):
        if math.gcd(i, j) == 1:
            res.append(f'{j}/{i}')
print(res)
