import pandas as pd

df = pd.read_csv('C:/Users/kseni/OneDrive/Desktop/petrova_ks/projects_6/task_6-0/wild_boars.csv')

with open('C:/Users/kseni/OneDrive/Desktop/petrova_ks/projects_6/task_6-0/modes.txt', 'w', encoding='utf-8') as f:
    for col in df.columns:
        mode_vals = df[col].mode()
        mode_val = mode_vals.iloc[0]
        f.write(f"{col}\t{mode_val}\n")
