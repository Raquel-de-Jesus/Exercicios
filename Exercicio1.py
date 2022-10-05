x = int(input("Informe o eixo X: "))
y = int(input("Informe o eixo Y: "))

while x != 0 and y != 0:
  if x > 0 and y > 0:
    print("Primeiro quadrante")
  elif x > 0 and y < 0:
    print("Quarto quadrante")
  elif x < 0 and y < 0:
    print("Terceiro quadrante")
  else:
    print("Segundo quadrante")
  x = int(input("Informe o eixo X: "))
  y = int(input("Informe o eixo Y: "))