import csv

# Function to read values to remove from a CSV file
def read_values_to_remove(values_file, column_to_collect_codes, row_to_start_codes):
    values_to_remove = []
    with open(values_file, 'r', newline='') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i >= row_to_start_codes - 1:
                values_to_remove.append(row[column_to_collect_codes].strip())
                print("Adding value to remove:", row[column_to_collect_codes].strip())
    return values_to_remove

# Function to remove rows containing specified values
def remove_rows_with_values(file_path, values_to_remove, output_file, column_to_check, row_to_start_delete):
    with open(file_path, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        headers = next(reader)
        writer.writerow(headers)
        for i, row in enumerate(reader):
            if i >= row_to_start_delete - 1:
                if row[column_to_check + 6].strip() not in values_to_remove:
                    writer.writerow(row)
                else:
                    print("Removing row with value:", row[column_to_check + 6])
            else:
                writer.writerow(row)

#Configuration
row_to_start_codes = 3  # Which row do the codes start in?
column_to_collect_codes = 2 # Which column should codes be collected from?
row_to_start_delete = 1  # Which row is the first to delete?
column_to_check = 2  # Which column should be checked?
file_path = 'example.csv'  # Path to the input CSV file
values_file = 'values_to_remove.csv'  # Path to the CSV file with values to remove
output_file = 'filtered_example.csv'  # Path to the output CSV file

values_to_remove = read_values_to_remove(values_file, column_to_collect_codes, row_to_start_codes)
remove_rows_with_values(file_path, values_to_remove, output_file, column_to_check, row_to_start_delete)

print(len(values_to_remove)) 
print("Task Done")