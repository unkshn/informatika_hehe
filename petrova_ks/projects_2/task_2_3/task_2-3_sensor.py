operator = input("Введите имя оператора ")
pressure = input("Введите значение давления ")

with open("C:/Users/kseni/OneDrive/Desktop/petrova_ks/projects_2/task_2_3/sensor_log.txt", 'w', encoding='utf-8') as file:
    file.write(f"{operator}\t{pressure}\n")

print("Данные успешно сохранены в sensor_log.txt")