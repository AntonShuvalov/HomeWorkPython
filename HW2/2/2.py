# Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

print('|_x_|_y_|_z_|', '¬(X ∧ Y) ∨ Z')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            res = not (x and y) or z
            print(f"| {x} | {y} | {z} |       {int(res)}")
