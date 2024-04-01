import matplotlib.pyplot as plt
import math
import numpy as np

# Read equations from equations.txt
with open('equations.txt', 'r') as file:
    equations = file.readlines()

# Function to evaluate equations
def evaluate_equation(x, equation):
    return eval(equation.strip().replace('x', str(x)))

# Function to plot equations for specified values of x
def plot_equations(x_values, all_results, all_eq_labels):
    plt.figure(figsize=(10, 6))
    for i, x in enumerate(x_values):
        results = all_results[i]
        plt.plot(range(1, len(results) + 1), results, marker='o', linestyle='-', label=f'x = {x}')
    plt.xlabel('Equation')
    plt.ylabel('Result')
    plt.title('Values of Equations')
    plt.xticks(range(1, len(results) + 1), [f'E{i}' for i in range(1, len(results) + 1)])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()  # Moved outside the loop

# Loop
while True:

    # Ask the user for input values of x
    x_values = input("Enter the values of x (1 to 50) separated by commas: ").split(',')
    x_values = [int(x) for x in x_values]

    # Validate the input values
    invalid_values = [x for x in x_values if x < 1 or x > 50]
    if invalid_values:
        print("Invalid input. x must be between 1 and 50.")
    else:
        # Initialize lists to store results
        all_results = []
        all_eq_labels = []

        # Evaluate equations for each value of x and print the results in the results.txt file
        with open('results.txt', 'w') as output_file:
            for x in x_values:
                output_file.write(f"For x = {x}:\n")
                results = []
                eq_labels = []
                for eq in equations:
                    eq_label = eq.split('=')[0].strip()
                    expression = eq.split('=')[1].strip()
                    result = evaluate_equation(x, expression)
                    results.append(result)
                    eq_labels.append(eq_label)
                    output_file.write(f"{eq_label} = {result}\n")
                all_results.append(results)
                all_eq_labels.append(eq_labels)

        # Plot the equations for the specified values of x
        plot_equations(x_values, all_results, all_eq_labels)

        print("Results saved to results.txt\n")

        # Ask the user if they want to remove a number
        remove_num = input("Do you want to remove a number? (yes/no): ")
        if remove_num.lower() == 'yes':
            num_to_remove = int(input("Enter the number you want to remove: "))
            if num_to_remove in x_values:
                idx = x_values.index(num_to_remove)
                x_values.pop(idx)
                all_results.pop(idx)
                all_eq_labels.pop(idx)
                print(f"Number {num_to_remove} removed.")
                # Plot the updated equations
                plot_equations(x_values, all_results, all_eq_labels)

        # Evaluate equations for each value of x and print the results
        with open('results.txt', 'w') as output_file:
            for x in x_values:
                output_file.write(f"For x = {x}:\n")
                results = []
                eq_labels = []
                for eq in equations:
                    eq_label = eq.split('=')[0].strip()
                    expression = eq.split('=')[1].strip()
                    result = evaluate_equation(x, expression)
                    results.append(result)
                    eq_labels.append(eq_label)
                    output_file.write(f"{eq_label} = {result}\n")
                all_results.append(results)
                all_eq_labels.append(eq_labels)
                output_file.write("\n")  # Add a blank line after each set of equations

        print("Results saved to results.txt\n")

        # Ask the user if they want to continue
        choice = input("Do you want to choose different numbers? (yes/no): ")
        if choice.lower() != 'yes':
            break  # Exit the loop if the user doesn't want to continue
