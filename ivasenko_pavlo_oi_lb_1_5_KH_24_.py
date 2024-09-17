import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

range_values = np.arange(0, 50001, 1000)
sigma_thickness = 2000

terms = {
    'poor_level': 4000,
    'very_low_level': 10000,
    'low_level': 14000,
    'medium_level': 18000,
    'more_than_medium_level': 22000,
    'high_level': 30000,
    'more_than_high_level': 40000,
    'rich_level': 50000,
}

poor_level = fuzz.gaussmf(range_values, terms['poor_level'], sigma_thickness)
very_low_level = fuzz.gaussmf(range_values, terms['very_low_level'], sigma_thickness)

low_level = fuzz.gaussmf(range_values, terms['low_level'], sigma_thickness)
medium_level = fuzz.gaussmf(range_values, terms['medium_level'], sigma_thickness)

more_than_medium_level = fuzz.gaussmf(range_values, terms['more_than_medium_level'], sigma_thickness)
high_level = fuzz.gaussmf(range_values, terms['high_level'], sigma_thickness)

more_than_high_level = fuzz.gaussmf(range_values, terms['more_than_high_level'], sigma_thickness)
rich_level = fuzz.gaussmf(range_values, terms['rich_level'], sigma_thickness)

plt.plot(range_values, poor_level, 'red', label='Найнижчий')
plt.plot(range_values, very_low_level, 'peru', label='Дуже низький')
plt.plot(range_values, low_level, 'grey', label='Низький')
plt.plot(range_values, medium_level, 'y', label='Середній')
plt.plot(range_values, more_than_medium_level, 'linen', label='Вище середнього')
plt.plot(range_values, high_level, 'g', label='Високий')
plt.plot(range_values, more_than_high_level, 'c', label='Більше високого')
plt.plot(range_values, rich_level, 'yellow', label='Дуже високий')

plt.title('Рівень життя людини в залежності від статків')
plt.ylabel('Ступінь належності')
plt.legend()
plt.show()