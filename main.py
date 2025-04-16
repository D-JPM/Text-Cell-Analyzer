# Load libraries
import pandas as pd
import os


def main():
    
    # Load the Excel file
    file_path = input("Please enter the path to your excel file: ")
    
    # Run through file load and debug statements
    if os.path.isfile(file_path):
        print("[DEBUG] File loaded")
        print(f"[DEBUG] Attempting to load file from path: {file_path}")
        df = pd.read_excel(file_path) #Use pandas and read the xl file, assign this to df(DataFrame)
        print(f"[DEBUG] Successgully loaded data with shape: {df.shape}")
    else:
        print("[DEBUG] File not loaded, please check file format and path is correct.")
        return # Exit if file is invalid or load fails.
    print(f"[DEBUG] Attempting to load file from path: {file_path}") # Debugging
    
    
    
    # Enumerate and display the columns
    for index, column in enumerate(df.columns):
        print(f"{index}: {column}")
    column_input = input("Enter the indice(s) of column (s) you want to select seperated by ',': ") # Modified the string prompt
    print(f"[DEBUG] Raw column input: {column_input}")
    split_input = column_input.split(',') # Splitting the user input by comma
    print(f"[DEBUG] Split column input: {split_input}")
    indices = [int(index.strip()) for index in split_input] # Take the user input, clean off whitespaces using strip and then convert to integer and store in 'indices'
    print(f"[DEBUG] Cleaned column indices: {indices}")
    selected_column = df.iloc[:, indices] # use idloc to select column index.



    # Making pattern targets dynamic user input
    user_input = input("Enter target keywords seperated by commas: ")
    targets = [word.strip() for word in user_input.split(',')]
    target_count = {} # Counter for the target
    
    

    for target in targets:
        print(f"[DEBUG] Starting search or target word: {target}") # Debugging
        count = 0
        # Loop through each column name in the df 
        for column in df.columns: 
            print(f"[DEBUG] Inspecting column: {column}") # Debugging
            # For each column, loop through every cell
            for cell in df[column]:
                # Make sure the cell is a string before searching
                # Check 1. is the cell a strin (isinstance)
                # Check 2. Does the target word appear in the cell
                if isinstance(cell, str) and target.lower() in cell.lower(): # .lower so that it is case-insensitive
                    print(f"[DEBUG] Match found in cell: {cell}")
                    # If both conditions(checks above) are true, increase the counter below by 1
                    count += 1
        target_count[target] = count


    for target, count in target_count.items():
        print(f"'{target}' was found {count} times in the spreadsheet.")






    # Preview of the data (testing)
    #print(df.head(10)) # Show only the first few rows (This string method belongs to pandas - not python default) .head returns first 5 rows when left empty but can specific number.

if __name__ == "__main__":
    main()
