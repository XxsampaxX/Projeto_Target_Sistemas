
def fibonacci(num):
    arr = [0,1]
    # Entrada do usuário com um valor:
    n = int(input("Digite um número: "))
   # Criando a sequência fibonacci:
    if num==1:
        print('0')
    elif num==2:
        print('[0,','1]')
    else:
        while(len(arr)<num):
            arr.append(0)
        if(num==0 or num==1):
            return 1
        else:
            arr[0]=0
            arr[1]=1
            for i in range(2,num):
                arr[i]=arr[i-1]+arr[i-2]
            print(arr)
            #Verificando e imprimindo na tela se o número digitado pelo usuário esta na sequência:
            if n in  arr:
                print(f'Esse número pertence a sequência: {n}')
            else:
                print(f'Esse número não pertence a sequência: {n}')

     #Definindo o tamnho da sequência de fibonacci:       
fibonacci(15)
