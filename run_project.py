"""Run every stage of the independent Level 1 project in the correct order."""

from src.prepare_data import prepare
from src.build_database import build_database
from src.analyse_data import run_analysis

if __name__ == "__main__":
    prepare()
    build_database()
    run_analysis()
    print("Level 1 project completed successfully.")

