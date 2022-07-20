
#ENMASCARAMIENTO DE BITS POR DESPLAZAMIENTO
numero = 32
numero = numero << 1
print(numero)
numero >>= 1
print(numero)
numero <<= 3
print(numero)

#ENMASCARAMIENTO PERRON
#   0   0   1   0   1   0   0   0

#PRENDER
numero = 0
numero |= (1<<5)
print(numero)
numero |= (1<<1) |(1<<0)
print(numero)

#APAGAR
numero &= ~(1<<1)
print(numero)

