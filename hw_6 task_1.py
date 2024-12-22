import re
import matplotlib.pyplot as plt

file_path = 'data.txt'

dates = []
temperatures = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # извлечение даты и температуры
        match = re.search(r'(\d{4}-\d{2}-\d{2}): Temperature = (\d+)°C', line)
        if match:
            dates.append(match.group(1))  # Первая группа — дата
            temperatures.append(int(match.group(2)))  # Вторая группа — температура

# Задача 1
max_temp_index = temperatures.index(max(temperatures))
max_temp_date = dates[max_temp_index]
print(f"Самая высокая температура: {max(temperatures)}°C, дата: {max_temp_date}")

# Задача 2
plt.figure(figsize=(10, 6))
plt.hist(temperatures, bins=10, edgecolor='black')
plt.title('Гистограмма температур', fontsize=16)
plt.xlabel('Температура (°C)', fontsize=12)
plt.ylabel('Количество дней', fontsize=12)
plt.grid(True)
plt.savefig('temperature_histogram.png')
plt.show()

# Задача 3
filtered_temperatures = [temp for temp in temperatures if temp >= 13]
filtered_dates = [date for i, date in enumerate(dates) if temperatures[i] >= 13]

plt.figure(figsize=(10, 6))
plt.plot(filtered_dates, filtered_temperatures, marker='o', linestyle='-', color='b', label='Temperature')
plt.title('Температура по дням (Фильтрация)', fontsize=16)
plt.xlabel('Дата', fontsize=12)
plt.ylabel('Температура (°C)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('temperature_plot_filtered.png')
plt.show()