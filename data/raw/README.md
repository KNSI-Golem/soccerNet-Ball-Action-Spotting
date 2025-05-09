---
license: gpl-3.0
---

# SoccerNet Challenge 2025 - Team Ball Action Spotting

## Download the dataset

Install the huggingface_hub pip package:

```bash
pip install huggingface_hub[cli]
```

Download the dataset with the following Python code :

```python
from huggingface_hub import snapshot_download
snapshot_download(repo_id="SoccerNet/SN-BAS-2025",
                  repo_type="dataset", revision="main",
                  local_dir="SoccerNet/SN-BAS-2025")
```

## Unzip the dataset splits

The zipped folder contains videos from the original [SoccerNet dataset](https://www.soccer-net.org/data), which is password-protected.
You will receive that password after signing the [SoccerNet NDA](https://docs.google.com/forms/d/e/1FAIpQLSfYFqjZNm4IgwGnyJXDPk2Ko_lZcbVtYX73w5lf6din5nxfmA/viewform).
