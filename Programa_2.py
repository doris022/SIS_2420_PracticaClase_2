def prim(num_prim):
    a = 0
    for i in range(1, num_prim + 1):
        if num_prim %i==0:
            a=a+1
    
    if a==2:
        return "es Primo"
    else:
        return "no es Primo"
    

numero = int(input("Ingrese un numero: "))
primo = prim(numero) 
print(f"El numero {numero} {primo}")


