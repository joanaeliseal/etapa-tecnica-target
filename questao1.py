""" QUESTÃO 1"""
def is_fibonacci(n):
    if n < 0:
        raise ValueError("O número deve ser maior ou igual a zero.")
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or a == n

# Função de testes
def test_is_fibonacci():
    assert is_fibonacci(0) == True
    assert is_fibonacci(1) == True
    assert is_fibonacci(13) == True
    assert is_fibonacci(14) == False
    print("Todos os testes passaram.")

# Exemplo de uso com tratamento de erros
try:
    numero = int(input("Informe um número: "))
    if is_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
except ValueError as e:
    print(e)

# Rodando os testes
test_is_fibonacci()
