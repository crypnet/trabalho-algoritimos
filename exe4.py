n = float(input('Digite um numero: '))

if n>0:
  raiz = n**(1/2)
  print("A raiz de ",n," é {:.2f}".format(raiz))
else:
  print("Raiz inexistente ")
