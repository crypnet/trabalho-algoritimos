def triangulo(a,b,c):
  if a >= b + c:
    return "triangulo nao e formado"
  if a*a == b *b + c *c:
    return "triangulo retangulo"
  if a*a > b*b + c*c:
    return "triangulo obtusangulo"
  if a*a < b*b + c*c:
    return "triangulo acutangulo"
a = float(input("digite o n�mero : "))
b = float(input("digite o n�mero : "))
c = float(input("digite o n�mero : "))
print(triangulo(a,b,c))