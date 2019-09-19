def vetor(number):
  for i in range(0 , number+1):
    vet=[]
    for x in range(i):
      vet.append(x+1)
    print(vet)
vetor(int(input('Digite Um numero')))