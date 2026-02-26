dna = input("Введите последовательность ДНК: ")

dna_upper = dna.upper()

a_count = dna_upper.count('A')
t_count = dna_upper.count('T')
g_count = dna_upper.count('G')
c_count = dna_upper.count('C')

total_length = len(dna_upper)

print("\n=== Анализ последовательности ДНК ===\n")
print(f"Последовательность в верхнем регистре: {dna_upper}\n")
print("Подсчёт нуклеотидов:")
print(f"A: {a_count}")
print(f"T: {t_count}")
print(f"G: {g_count}")
print(f"C: {c_count}")
print(f"\nОбщая длина: {total_length} нуклеотидов")