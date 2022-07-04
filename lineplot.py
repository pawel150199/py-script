import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,1, figsize=(7,5))

year_1 = [2016, 2017, 2018, 2019, 2020, 2021]
population_1 = [42, 43, 45, 47, 48, 50]

year_2 = [2016, 2017, 2018, 2019, 2020, 2021]
population_2 = [43, 43, 44, 44, 45, 45]

ax[0].plot(year_1, population_1, marker='o', linestyle='--', color='g', label='Country 1')
ax[1].plot(year_2, population_2,  marker='d', linestyle='-', color='r', label='Country 2')

plt.xlabel('Year')
plt.ylabel('Population (M)')
plt.title('Year vs Population')
plt.legend(loc='lower right')
plt.tight_layout()

plt.show()