import json 
from pathlib import Path 

# CHECKPOINT_PATH 
CHECKPOINT_PATH = Path("data/checkpoints/energy_ingest.json")

def load_checkpoint():
    if CHECKPOINT_PATH.exist():
        with open(CHECKPOINT_PATH, 'r') as f:
            return json.load(f)
    return {"offset" : 0}

def save_checkpoint(offset: int):
    CHECKPOINT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CHECKPOINT_PATH, 'w') as f:
        json.dump({"offset": offset}, f)