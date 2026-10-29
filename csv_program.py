import csv

with open("info.csv", "w") as file:

    writer = csv.writer(file)

    writer.writerow(["RollNo", "Name", "Marks"])

    writer.writerow([37, "parth", 90])

    writer.writerow([38, "utkarsh", 91])

    writer.writerow([39, "pate", 92])

print("Data Written Successfully!!")
