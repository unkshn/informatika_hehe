# task_2-2_inventory_control.py

reactiv_name = input("Введите название реактива ")
reactiv_quantity = int(input("Введите количество реактива "))
report = f"Реактив {reactiv_name} поступил на склад в количестве {reactiv_quantity} шт."
print(report)

f = open("C:/Users/kseni/OneDrive/Desktop/petrova_ks/projects_2/task_2_2/inventor.txt", 'w', encoding='utf-8')
print(report, file=f)
f.close()
