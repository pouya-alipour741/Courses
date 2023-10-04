
"""
Contains various utility functions for PyTorch model training and saving.
"""
import torch
from pathlib import Path

def save_model(model,
               directory,
              model_name):
    """save a model to a directory
    
    Args:
        model
        directory
        model_name
    example:
        save_model(model=model_0,
        target_dir="models",
        model_name="05_going_modular_tingvgg_model.pth")
    """
    directory_path = Path(directory)
    directory_path.mkdir(parents=True,exist_ok=True)
    
    assert model_name.endswith("pth") or model_name.endswith("th") 
    model_save_path = directory_path/model_name
    
    print(f"saving model to {model_save_path}")

    torch.save(obj=model.state_dict(),
              f=model_save_path)
    
    
