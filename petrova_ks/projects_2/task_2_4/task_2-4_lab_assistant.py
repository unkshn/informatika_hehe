volume = float(input("Введите нужный объем раствора: "))

salt_mass = volume * 0.009

with open("C:/Users/kseni/OneDrive/Desktop/petrova_ks/projects_2/task_2_4/recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли:  {salt_mass:.2f} г\n")
    file.write(f"Объем воды:  {volume} мл\n")

print("Рецепт успешно сохранен в файл recipe.txt")