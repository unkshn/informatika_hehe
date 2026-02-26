name = input("Введите название питательной среды ")
agar = input("Введите концентрацию агара ")
temperature = input("Введите температуру стерилизации ")

# Записываем данные в файл
with open("C:/Users/kseni/OneDrive/Desktop/petrova_ks/projects_2/task_2_3/recipe.txt", 'w', encoding='utf-8') as file:
    file.write(f"{name}\nКонцентрация агара: {agar}%\nТемпература стерилизации: {temperature}°C")

print("Файл 'recipe.txt' успешно сформирован!")
