import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CLEAN_PATH = BASE_DIR / "data" / "processed" / "production_data_clean.csv"
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "kpi_summary.csv"

def analyze(df):
    # Average output and downtime by line
    line_summary = df.groupby('production_line').agg(
        avg_output=('units_produced', 'mean'),
        avg_downtime=('downtime_minutes', 'mean'),
        avg_defect_rate=('defective_units', lambda x: (x.sum()/df.loc[x.index,'units_produced'].sum()))
    ).reset_index()
    
    # Output trend over time
    trend_summary = df.groupby('date').agg(total_output=('units_produced', 'sum')).reset_index()
    
    return line_summary, trend_summary

def run_analysis():
    df = pd.read_csv(CLEAN_PATH)
    line_summary, trend_summary = analyze(df)
    line_summary.to_csv(OUTPUT_PATH, index=False)
    trend_summary.to_csv(BASE_DIR / "data" / "processed" / "output_trend.csv", index=False)
    print("Analysis complete. KPI summary and output trend saved.")

if __name__ == "__main__":
    run_analysis()

