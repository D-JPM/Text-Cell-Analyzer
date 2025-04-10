# Load libraries
import pandas as pd


def main():
    # Load the Excel file
    df = pd.read_excel("data/MOCK_DATA_REPORT.xlsx") # Use pandas and read the xl file, assign this to df(DataFrame)

    # Preview of the data (testing)
    print(df.head(10)) # Show only the first few rows (This string method belongs to pandas - not python default) .head returns first 5 rows when left empty but can specific number.

if __name__ == "__main__":
    main()
