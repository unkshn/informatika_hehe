import pandas as pd

df = pd.read_csv('C:/Users/kseni/OneDrive/Desktop/petrova_ks/projects_6/task_6-0/wild_boars.csv')

medians = df.median(numeric_only=True)

with open('C:/Users/kseni/OneDrive/Desktop/petrova_ks/projects_6/task_6-0/medians.txt', 'w', encoding='utf-8') as f:
    for col in medians.index:
        f.write(f"{col}\t{medians[col]:.2f}\n")
