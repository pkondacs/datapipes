import random
import csv
from faker import Faker

fake = Faker()

# Generate 700 random corporation names
corporations = [fake.company() for _ in range(700)]

# Generate random zip codes, states, and cities
zip_codes = [fake.zipcode() for _ in range(700)]
states = [fake.state() for _ in range(700)]
cities = [fake.city() for _ in range(700)]

# Combine the data into a list of tuples
data = list(zip(corporations, zip_codes, states, cities))

# Save the data to a CSV file
filename = "C:\datapipes\data\corporations_data.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Corporation Name", "Zip Code", "State", "City"])  # Write header
    writer.writerows(data)  # Write data rows

print("Data saved successfully in", filename)
