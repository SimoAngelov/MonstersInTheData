"""Project paths, resolved relative to the repository root.

Used by the notebooks and by src/clean.py, so that no path is hard-coded.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent #the root of the project
RAW = ROOT / "data" / "raw" #the raw data folder
PROCESSED = ROOT / "data" / "processed" #the processed data folder
CONFIG = ROOT / "config" #the config folder