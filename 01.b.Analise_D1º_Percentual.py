import pandas as pd

# Carregar o arquivo CSV em um DataFrame
file_path = "/home/henrique/PycharmProjects/extração/Base_2024.csv"
df = pd.read_csv(file_path)

# Criar uma lista com o prefixo das colunas desejadas
columns_prefix = ["D 1º", "D 2º", "D 3º", "D 4º", "D 5º"]

# Inicializar uma lista para armazenar os resultados
results = []

# Iterar sobre as colunas desejadas
for prefix in columns_prefix:
    # Calcular as contagens para cada número
    counts = df[prefix].value_counts().sort_index()

    # Calcular o total de amostras
    total_samples = counts.sum()

    # Calcular os percentuais para cada número
    percentages = (counts / total_samples) * 100

    # Adicionar os resultados formatados à lista
    for i in range(100):
        result_str = f"{prefix} \"{i:02d}\": {counts.get(i, 0)} x ({percentages.get(i, 0):.2f}%)"
        results.append(result_str)

# Preencher com strings vazias para garantir que ambas as listas tenham o mesmo comprimento
while len(results) < 100:
    results.append("")

# Dividir a lista de resultados em duas colunas
results_df = pd.DataFrame({"00-49": results[:50], "50-99": results[50:]})

# Exibir o DataFrame
print(results_df)
