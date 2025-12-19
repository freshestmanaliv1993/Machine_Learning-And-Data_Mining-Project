import csv
import matplotlib.pyplot as plt


filename = 'StudentsPerformance.csv'
read_list = [] 
write_list = [] 


with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        x_val = float(row['reading score'])
        y_val = float(row['writing score'])
        read_list.append(x_val)
        write_list.append(y_val)



def calculate_mean(data):
    return sum(data) / len(data)

read_mean = calculate_mean(read_list)
write_mean = calculate_mean(write_list)

numerator = 0
denominator = 0

for i in range(len(read_list)):
    numerator += (read_list[i] - read_mean) * (write_list[i] - write_mean)
    denominator += (read_list[i] - read_mean) ** 2

m = numerator / denominator
b = write_mean - (m * read_mean)

print("-" * 30)
print("Simple Linear Model Results:")
print(f"Slope (m):     {m:.4f}")
print(f"Intercept (b): {b:.4f}")
print(f"Equation:      y = {m:.4f}x + {b:.4f}")
print("-" * 30)

def predict(x_input):
    return (m * x_input) + b


read_min = min(read_list)
read_max = max(read_list)
write_min = predict(read_min)
write_max = predict(read_max)


plt.figure(figsize=(10, 6))
plt.scatter(read_list, write_list, color='gray', alpha=0.5, label='Actual Scores')
plt.plot([read_min, read_max], [write_min, write_max], color='red', linewidth=3, label='Manual Regression Line')
plt.title(f'Simple Linear Regression\nEquation: y = {m:.2f}x + {b:.2f}')
plt.xlabel('Reading Score')
plt.ylabel('Writing Score')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()