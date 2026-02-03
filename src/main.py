import analysis
import clean_validate
import ingest
import visualize

def main():
    print("Starting data pipeline...")
    ingest.load_data_to_psql()
    clean_validate.run_cleaning()
    analysis.run_analysis()
    visualize.create_visualizations()
    print("Data pipeline completed.")

if __name__ == "__main__":
    main()