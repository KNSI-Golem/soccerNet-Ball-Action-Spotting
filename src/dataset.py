"""
Code to download or generate data
"""

from pathlib import Path
from src.config import PROCESSED_DATA_DIR, RAW_DATA_DIR
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
            print(f"\n🔓 Unzipping: {zip_path}")

            try:
                output_path = directory/filename.replace(".zip", "")
                unzipFile(zip_path, password, output_path)
                print(f"✅ Extracted to: {output_path}")
                
                os.remove(zip_path)
                print(f"🗑️ Deleted zip file: {zip_path}")
            
            except RuntimeError as e:
                print(f"❌ Failed to unzip {filename}: {e}")

def main(
    input_path: Path = RAW_DATA_DIR,
    output_path: Path = PROCESSED_DATA_DIR
    
):
    load_dotenv()
    password = os.getenv("DATA_PASSWD").encode()
    
    downloadDataset(input_path)
    unzipDirectory(input_path, password)


if __name__ == "__main__":
    main()
