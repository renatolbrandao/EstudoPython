print("Exemplo de captura de exceções")
try:
    numero = int(input("\nDigite um numero inteiro"))
    resultado = 10 / numero
    print(f'Resultado: {resultado}')
except ValueError as e:
    print(f"Erro de value error: {e}")
    raise ValueError("Tipo incompativel")
except Exception as e:
    print(f"Erro: {e}")