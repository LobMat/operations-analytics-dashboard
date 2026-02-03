import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_PATH = BASE_DIR / "data" / "raw" / "production_data.csv"
CLEAN_PATH = BASE_DIR / "data" / "processed" / "production_data_clean.csv"

def clean_validate(df):
    # Drop rows with missing essential fields
    df = df.dropna(subset=['date', 'production_line', 'shift', 'units_produced'])
    
    # Ensure numeric fields are valid
    df['units_produced'] = df['units_produced'].clip(lower=0)
    df['downtime_minutes'] = df['downtime_minutes'].clip(lower=0)
    
    # Defective units cannot exceed produced units
    df['defective_units'] = df[['units_produced', 'defective_units']].apply(
        lambda x: min(x['defective_units'], x['units_produced']), axis=1
    )
    
    return df

def run_cleaning():
    df = pd.read_csv(RAW_PATH)
    df_clean = clean_validate(df)
    df_clean.to_csv(CLEAN_PATH, index=False)
    print(f"Cleaned data saved to {CLEAN_PATH}")

if __name__ == "__main__":
    run_cleaning()
