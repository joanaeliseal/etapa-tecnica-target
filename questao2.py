def contar_a(string):
    if not isinstance(string, str):
        raise TypeError("A entrada deve ser uma string.")
    count = string.lower().count('a')
    return count

# Função de testes
def test_contar_a():
    assert contar_a("Abracadabra") == 5
    assert contar_a("Ala") == 2
    assert contar_a("XYZ") == 0
    print("Todos os testes passaram.")

# Exemplo de uso com tratamento de erros
try:
    texto = input("Informe a string: ")
    quantidade_a = contar_a(texto)
    print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
except TypeError as e:
    print(e)

# Rodando os testes
test_contar_a()
