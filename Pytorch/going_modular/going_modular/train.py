
"""
Trains a PyTorch image classification model using device-agnostic code.
"""

import torch
import data_setup, engine, model_builder, utils
from torchvision import transforms

# hyperparameters
EPOCHS = 5
BATCH_SIZE = 32
LEARNING_RATE = 0.001
HIDDEN_UNITS = 10


# directories
train_dir = r"C:\Users\pouya\jupyter projects\PyTorch_for Deep Learning_Machine Learning\going_modular\data\pizza_steak_sushi\train"
test_dir = r"C:\Users\pouya\jupyter projects\PyTorch_for Deep Learning_Machine Learning\going_modular\data\pizza_steak_sushi\test"

# target device
device = "cuda" if torch.cuda.is_available() else "cpu"

# transforms
data_transform = transforms.Compose([
    transforms.Resize((64,64)),
    transforms.ToTensor()   
])

train_dataloader, test_dataloader, class_names = data_setup.create_dataloaders(train_dir,
                            test_dir,
                            data_transform,
                            BATCH_SIZE,
                            num_workers=2)

model = model_builder.TinyVGG(
        input_shape=3,
        hidden_units=HIDDEN_UNITS,
        output_shape=len(class_names)
    
        ).to(device)

##set up loss and optimizer functions
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),
                           lr=LEARNING_RATE)

results = engine.train(model,
            train_dataloader,
            test_dataloader,
            criterion,
            optimizer,
            EPOCHS,
            device)

utils.save_model(model,
                directory="models",
                model_name="going_modular_script_mode_tinyvgg_model.pth")
