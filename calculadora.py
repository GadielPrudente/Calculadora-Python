while True:
    numero_1 = input('dijite um numero ')
    numero_2 = input('dijite outro numero ')
    operadores = input('dijite um desse opeeradores (+-*/) ')
    numeros_validos = None
    num_float1 = 0
    num_float2 = 0
    try:
        num_float1 = float(numero_1)
        num_float2 = float(numero_2)
        numeros_validos = True 
    except:
        numeros_validos = None
        if numeros_validos is None:
            print('um ou ambos números dijitados são inválidos ')
            continue 
    operadores_permitidos = '+-*/'
    if operadores not in operadores_permitidos:
        print('operador inválido ')
        continue 
    if len(operadores) > 1:
        print('dijite apenas 1 operador ') 
        continue 
    print('realizando sua conta')
    if operadores == '+':
        print(f'o resultado de {num_float1} + {num_float2} = ', num_float1 + num_float2)
    elif operadores == '-':
         print(f'o resultado de {num_float1} - {num_float2} = ', num_float1 - num_float2)
    elif operadores == '/':
         print(f'o resultado de {num_float1} / {num_float2} = ', num_float1 / num_float2)
    elif operadores == '*':
         print(f'o resultado de {num_float1} * {num_float2} = ', num_float1 * num_float2)
    else:
        print('não deve chegar aqui ')
    sair = input('quer sair [sim] ').lower().startswith('s')
    if sair is True:
        break 

    