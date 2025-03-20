import pandas as pd

def clean_data(input_file, output_file):
    """Reads, cleans, and saves the dataset."""
    df = pd.read_csv(input_file)

    # Drop missing values
    df.dropna(inplace=True)

    # Convert column names to lowercase
    df.columns = [col.lower() for col in df.columns]

    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_data("sample_data.csv", "cleaned_data.csv")