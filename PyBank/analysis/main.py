# import os module
import os
# import CSV
import csv
# csv path
csvpath = os.path.abspath("../Resources/pybank_budget_data.csv")


# open/read csv
with open(csvpath, newline='') as data_file:
    reader = csv.reader(data_file)
    # skip  header
    csv_header = next(data_file)

    # intilizing variables
    previous_value = 0
    total_differences = 0
    num_rows = 0
    total = 0

    # Max increase vars
    max_increase = 0
    max_increase_month = ""

    # Max decrease vars
    max_decrease = 0
    max_decrease_month = ""

    for row in reader:
        current_value = int(row[1])
        total += current_value
        # Skip the first row since there is no difference
        if num_rows > 0:
            difference = current_value - previous_value
            # calculating The greatest decrease in losses
            if difference < max_decrease:
                max_decrease_month = row[0]
                max_decrease = difference
            # calculating The greatest increase in gains
            if difference > max_increase:
                max_increase_month = row[0]
                max_increase = difference
            total_differences += difference
        previous_value = current_value
        num_rows += 1
    # calculating average difference and rounding to the hundredth place
    average_of_difference = round(total_differences / (num_rows - 1), 2)
    # creating variable for output print
    output = (
        'Financial Analysis\n'
        '----------------------------\n'
        f'Months: {num_rows}\n'
        f'Total: ${total}\n'
        f'Average Change: ${average_of_difference}\n'
        f'Greatest Increase in Profits: {max_increase_month} (${max_increase}\n'
        f'Greatest Decrease in Profits: {max_decrease_month} (${max_decrease}\n'
    )
    # printing output to terminal
    print(output)

    # writing output to txt file
    file = open('PyBank.txt', 'w')
    file.write(output)
    file.close()
