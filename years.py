
def bisexto(ano):
    if ano % 4 == 0 and ano % 100!=0 or ano % 400 == 0:
        print("{} é um ano Bisexto".format(ano))
    else:
        print("{} não é um ano Bisexto".format(ano))


while True:
    try:
        x = int(input("Escolha um ano: "))
        bisexto(x)
    except ValueError:
        print("Anos precisam ser numeros inteiros!")





