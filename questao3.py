def calcular_soma():
    indice = 12
    soma = 0
    k = 1

    while k < indice:
        k += 1
        soma += k

    return soma

# Função de testes
def test_calcular_soma():
    assert calcular_soma() == 91
    print("Todos os testes passaram.")

# Exemplo de uso
print(f"O valor final de SOMA é: {calcular_soma()}")

# Rodando os testes
test_calcular_soma()
