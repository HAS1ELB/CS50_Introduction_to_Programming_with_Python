exp = input("Expresion: ")

x, y, z = exp.split(" ")

new_x = float(x)
new_z = float(z)

if y == "+":
    res = new_x + new_z
if y == "-":
    res = new_x - new_z
if y == "*":
    res = new_x * new_z
if y == "/":
    res = new_x / new_z

print(round(res,1))
