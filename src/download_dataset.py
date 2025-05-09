"""
Code to download or generate data
"""

from pathlib import Path
from src.config import PROCESSED_DATA_DIR, SNB_DATA_DIR, PASSWORD
from huggingface_hub import snapshot_download

import pyzipper
from dotenv import load_dotenv
import os

def downloadDataset(directory):
    snapshot_download(repo_id="SoccerNet/SN-BAS-2025",
                    repo_type="dataset", revision="main",
                    local_dir=directory)

def unzipFile(input_path, password, output_path):   
    with pyzipper.AESZipFile(input_path) as zf:
            zf.pwd = password
            zf.extractall(output_path)

def unzipDirectory(directory, password):
    for filename in os.listdir(directory):
        if filename.endswith('.zip'):
            zip_path = os.path.join(directory, filename)
            print(f"\nUnzipping: {zip_path}")

            try:
                unzipFile(zip_path, password, directory)
                
                os.remove(zip_path)
            
            except RuntimeError as e:
                print(f"Failed to unzip {filename}: {e}")

def main(
    input_path: Path = SNB_DATA_DIR / 'test'
    
):
    load_dotenv()
    downloadDataset(input_path)
    unzipDirectory(input_path, PASSWORD)


if __name__ == "__main__":
    main()
