def triangulo(a,b,c):
  if a >= b + c:
    return "triangulo nao e formado"
  if a*a == b *b + c *c:
    return "triangulo retangulo"
  if a*a > b*b + c*c:
    return "triangulo obtusangulo"
  if a*a < b*b + c*c:
    return "triangulo acutangulo"
a = float(input("digite o número : "))
b = float(input("digite o número : "))
c = float(input("digite o número : "))
print(triangulo(a,b,c))