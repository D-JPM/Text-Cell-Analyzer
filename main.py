# Load libraries
import pandas as pd


def main():
    
    # Load the Excel file
    file_path = "data/MOCK_DATA_REPORT.xlsx"
    print(f"[DEBUG] Attempting to load file from path: {file_path}") # Debugging
    
    df = pd.read_excel(file_path) # Use pandas and read the xl file, assign this to df(DataFrame)
    print(f"[DEBUG] Successfully loaded data with shape: {df.shape}") # Debugging

    # Defining patterns I want to count
    target = 'Nottingham'
    count = 0 # Counter for the target
    
    print(f"[DEBUG] Starting search or target word: {target}") # Debugging

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
    print(f"'{target}' was found {count} times in the spreadsheet.")






    # Preview of the data (testing)
    #print(df.head(10)) # Show only the first few rows (This string method belongs to pandas - not python default) .head returns first 5 rows when left empty but can specific number.

if __name__ == "__main__":
    main()
