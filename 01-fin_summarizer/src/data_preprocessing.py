import pandas as pd


# convert csv to dataframe
def convert_csv_to_df(csv_data) -> pd.DataFrame:
    try:
        df = pd.read_csv(csv_data, low_memory=False)
        df.dropna(how="all", inplace=True)
        df.columns.str.strip().str.lower().str.replace(" ", "_")
        return df

    except FileNotFoundError:
        print("Error: file not found")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except pd.errors.EmptyDataError:
        print("File data is empty")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()