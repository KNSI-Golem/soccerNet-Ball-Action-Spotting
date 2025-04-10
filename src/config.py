"""
Store useful variables and configuration
"""

from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
DISK_ROOT = Path("/path/to/disk/root")

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

SNB_DATA_DIR = DISK_ROOT / "soccernetball"
SN_DATA_DIR = DISK_ROOT / "soccernet"

SNB_FRAMES_DIR = DISK_ROOT / "frames_snb"
SN_FRAMES_DIR = DISK_ROOT / "frames_sn"