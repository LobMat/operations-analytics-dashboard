import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def create_visualizations():

    BASE_DIR = Path(__file__).resolve().parent.parent
    KPI_PATH = BASE_DIR / "data" / "processed" / "kpi_summary.csv"
    FIGURES_DIR = BASE_DIR / "figures"

    FIGURES_DIR.mkdir(exist_ok=True)

    df = pd.read_csv(KPI_PATH)

    # Bar chart: average output by production line
    plt.figure(figsize=(8,6))
    plt.bar(df['production_line'], df['avg_output'], color='skyblue')
    plt.title('Average Output by Production Line')
    plt.xlabel('Production Line')
    plt.ylabel('Units Produced')
    plt.savefig(FIGURES_DIR / "avg_output_by_line.png")
    plt.close()

    # Bar chart: average downtime by production line
    plt.figure(figsize=(8,6))
    plt.bar(df['production_line'], df['avg_downtime'], color='salmon')
    plt.title('Average Downtime by Production Line')
    plt.xlabel('Production Line')
    plt.ylabel('Downtime (minutes)')
    plt.savefig(FIGURES_DIR / "avg_downtime_by_line.png")
    plt.close()

    print("Visualizations created in 'figures/' folder")

if __name__ == "__main__":
    create_visualizations()