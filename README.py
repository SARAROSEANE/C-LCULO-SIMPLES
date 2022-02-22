a=int(input("Código do item 1: "))
b=int(input("Quantidade do item 1: "))
c=float(input("Valor unitário 1: "))


a2=int(input("Código do item 2: "))
b2=int(input("Quantidade do item 2: "))
c2=float(input("Valor unitário 2: "))

var1=(b*c)
var2=(b2*c2)
rest =var1+var2

print('VALOR A PAGAR: R$ %.2f' % rest)
