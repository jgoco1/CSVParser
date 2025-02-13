# CSVParser
Parses CSV #2 to remove rows containing codes contained in CSV #1


Directions:
    1. Place the Parser.py script, as well as the CSV file containing your codes and CSV file you want to edit into the same folder.
    2. Edit the configuration to match the files you want to alter (if you don't have a code editor installed just right click and edit in notepad.)
        a. Change the file paths
            file_path should be the name of the csv file you want to remove rows from
            values_file should be the name of the file containing the codes for removal
            output_file is where the program should write to. Note that any information in this file will be overwritten.
        b. Find the row and column the codes start in from the values_file.
            row_to_start_codes should be the row the codes start in
            column_to_collect_codes should be the column the codes srart in
        c. Find the row and column the codes start in from the file_path
            row_to_start_delete should be the row the codes start in
            column_to_check should be the column the codes are in
    3. Run the Parser.py file. If you have python installed you can just double click to do this, otherwise you will need to install Python.