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

    average_of_difference = round(total_differences / (num_rows - 1), 2)

    print('Financial Analysis')
    print('----------------------------')
    print(f'Months: {num_rows}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average_of_difference}')
    print(f'Greatest Increase in Profits: {max_increase_month} (${max_increase})')
    print(f'Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})')

    file = open('PyBank.txt','w') 
 
    file.write('Financial Analysis') 
    file.write('----------------------------') 
    file.write(f'Months: {num_rows}') 
    file.write(f'Total: ${total}') 
    file.write(f'Average Change: ${average_of_difference}') 
    file.write(f'Greatest Increase in Profits: {max_increase_month} (${max_increase})')
    file.write(f'Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})')

    file.close() 