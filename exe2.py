import random
def maiorFunc(vet):
  maior = vet[0]
  segmaior = vet[0]
  print(vet)
  for i in range(1, len(vet)):
    if vet[i] > maior:
      maior =vet[i]
    elif vet[i] > segmaior and vet[i] < maior:
      segmaior = vet[i]
  print('--------------------------------')
  print("é o maior :", float(maior))
  print('--------------------------------')
  print("é segundo maior:", float(segmaior))
x = []
for i in range(10):
  x.append(random.randint(1, 100))
print(x[i])
maiorFunc(x)