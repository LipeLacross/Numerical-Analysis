# calcula a precisão da máquina
A = 1
s = 1 + A

while s > 1:
    A /= 2
    s = 1 + A

print("precisão:", 2 * A)  # 2A é o menor valor que faz 1 + A > 1

# explicação:
# 2A é o menor valor que, quando somado a 1, muda o resultado.
# se for somado um número menor que 2A a 1, a máquina nem nota a diferença e continua 1.
# isso mostra o limite da precisão dos cálculos em ponto flutuante na máquina.
