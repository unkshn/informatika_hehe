import pandas as pd

df = pd.read_csv('C:/Users/kseni/OneDrive/Desktop/petrova_ks/projects_6/task_6-0/wild_boars.csv')

means = df.mean(numeric_only=True)

with open('C:/Users/kseni/OneDrive/Desktop/petrova_ks/projects_6/task_6-0/means.txt', 'w', encoding='utf-8') as f:
    for col in means.index:
        f.write(f"{col}\t{means[col]:.2f}\n")
