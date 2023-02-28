# Função para somar os dias de faturamento 
def soma (dias):
    soma = 0
    for i in dias:
        soma = soma + i
    return soma
# Definindo os valores dos dias de faturamento segundo o xml  
dias = [22174.1664, 24537.6698, 26139.6134, 0, 0, 26742.6612, 0, 42889.2258, 46251.174, 11191.4722, 0, 0, 3847.4823, 373.7838, 2659.7563,
         48924.2448, 18419.2614, 0, 0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0, 0, 25681.8318, 1718.1221, 13220.495, 8414.61]
# Declarando as variáveis  
mai = 0
men = 0
med = 0
diamed = 21
maiomed = 0
mesmed = 20865.3701
# Calculando a média mensal 
soma  =  soma (dias)
med = soma/diamed 
# Calculando a quantidade de dias acima da média 
for num in dias:
    if num >= mesmed:
        maiomed += 1
    print(maiomed) 
 # Verificando o maior e o menor dia de faturamento do mês:
for c in range (0, 30):
    if c == 0:
        mai = men = dias[c]
    else: 
        if dias[c] > mai: 
            mai = dias [c]
        if dias[c] < men:
            men = dias[c]
    if dias[c] >= med:
        mesmed = dias[c]
# Informando na tela todas as informações para o usuario
print('=-' * 30)
print(f'Todos os dias de faturamento: {dias}')
print('=-' * 30)
print(f'O maior valor de faturamento do mês em um dia foi: {mai}')
print('=-' * 30)
print(f'O menor valor de faturamento do mês em um dia foi: {men}')
print('=-' * 30)
print("Soma dos dias de faturamento = {0:2f}". format(soma)) 
print('=-' * 30)
print(f'Media mensal de faturamento: {med}' )
print('=-' * 30)
print(f'Número de dias acima da media mensal: {maiomed} dias' )


