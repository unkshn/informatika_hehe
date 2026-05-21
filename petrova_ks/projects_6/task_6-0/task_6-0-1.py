import pandas as pd

df = pd.read_csv('C:/Users/kseni/OneDrive/Desktop/petrova_ks/projects_6/task_6-0/wild_boars.csv')

print("tusk_length_cm:")
print(df['tusk_length_cm'])

min_kleuk = df['tusk_length_cm'].min()
max_kleuk = df['tusk_length_cm'].max()

print(f"\nсамые короткие клыки: {min_kleuk} см")
print(f"самые длинные клыки: {max_kleuk} см")