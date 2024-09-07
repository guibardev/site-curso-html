# Criando uma lista vazia para armazenar as idades
idades = []

# Loop para perguntar 5 idades
for i in range(5):
    idade = int(input(f"Digite a idade {i+1}: "))  # Recebe a idade e converte para inteiro
    idades.append(idade)  # Adiciona a idade na lista

# Exibindo as idades fornecidas
print("\nIdades fornecidas:")
for i, idade in enumerate(idades):
    print(f"Pessoa {i+1}: {idade} anos")