#!/bin/bash
#SBATCH --job-name=train_soccernet
#SBATCH --output=slurm_%j.out
#SBATCH --error=slurm_%j.err
#SBATCH --partition=plgrid-gpu-a100
#SBATCH --account=plggolemml25-gpu-a100
#SBATCH --gres=gpu:a100:1
#SBATCH --mem=60G
#SBATCH --cpus-per-task=8
#SBATCH --time=04:00:00


# Optional: activate conda/venv if you're using your own
source /net/tscratch/people/plgkobusf112/.venv/bin/activate

# Navigate to project directory
cd /net/people/plgrid/plgkobusf112/soccerNet-Ball-Action-Spotting

# Run training
python -m src.modeling.train_tdeed_bas --model SoccerNetBall_baseline
