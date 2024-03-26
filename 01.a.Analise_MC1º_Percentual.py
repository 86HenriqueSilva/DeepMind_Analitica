import pandas as pd
"Percentual com base no total de amostras"
# Carregar o arquivo CSV em um DataFrame
file_path = "/home/henrique/PycharmProjects/extração/Base_2024.csv"
df = pd.read_csv(file_path)

# Calcular as contagens para cada número
counts = df["MC 1º"].value_counts().sort_index()

# Calcular o total de amostras
total_samples = counts.sum()

# Calcular os percentuais para cada número
percentages = (counts / total_samples) * 100

# Criar um DataFrame com os resultados formatados
results_df = pd.DataFrame({
    "00-49": [f"MC 1º \"{i:02d}\": {counts[i]} x ({percentages[i]:.2f}%)" for i in range(50)],
    "50-99": [f"MC 1º \"{i:02d}\": {counts[i]} x ({percentages[i]:.2f}%)" for i in range(50, 100)]
})

# Exibir o DataFrame
print(results_df)
