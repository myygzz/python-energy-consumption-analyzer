
import csv
import matplotlib.pyplot as plt

# Read electricity consumption data
dates = []
consumption = []

with open("energy_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dates.append(row["date"])
        consumption.append(float(row["energy_kwh"]))

# Calculate statistics
total = sum(consumption)
average = total / len(consumption)

highest = max(consumption)
highest_index = consumption.index(highest)
highest_day = dates[highest_index]

# Display results
print("===== ENERGY CONSUMPTION ANALYZER =====")
print(f"Total consumption: {total:.2f} kWh")
print(f"Average daily consumption: {average:.2f} kWh")
print(f"Highest consumption: {highest:.2f} kWh")
print(f"Highest consumption day: {highest_day}")

# Generate chart
plt.figure(figsize=(11, 5))

plt.plot(dates, consumption, marker="o")

plt.title("Daily Electricity Consumption")
plt.xlabel("Date")
plt.ylabel("Energy Consumption (kWh)")

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig("energy_chart.png")
plt.show()