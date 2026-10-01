from pathlib import Path

# Resolve the project root from this configuration file.
PROJECT_ROOT = Path(__file__).resolve().parent

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

# Source files
TRIP_FILE = RAW_DIR / "yellow_tripdata_2026-01.parquet"
ZONE_FILE = RAW_DIR / "taxi_zone_lookup.csv"