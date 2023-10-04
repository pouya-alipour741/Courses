
from going_modular.going_modular.engine import train_step,test_step
from tqdm.auto import tqdm
from collections import defaultdict
import torch
from time import perf_counter
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter()

def train(model,
         train_dataloader,
        test_dataloader,
         loss_fn,
         optimizer,
         device,
         epochs = 5):
    
    results = defaultdict(list)
    
    train_start_time = perf_counter()
    
    for epoch in tqdm(range(epochs)):
        train_loss, train_acc = train_step(model,
                  train_dataloader,
                  loss_fn,
                  optimizer,
                  device)

        test_loss,test_acc  = test_step(model,
                 test_dataloader,
                 loss_fn,
                 device)
        
        print(
          f"Epoch: {epoch+1} | "
          f"train_loss: {train_loss:.4f} | "
          f"train_acc: {train_acc:.4f} | "
          f"test_loss: {test_loss:.4f} | "
          f"test_acc: {test_acc:.4f}"
        )
        
        results["train_loss"].append(train_loss)
        results["train_acc"].append(train_acc)
        results["test_loss"].append(test_loss)
        results["test_acc"].append(test_acc)
        
        ##Experiment tracking
        writer.add_scalars(main_tag="Loss",
                        tag_scalar_dict={"train_loss":train_loss,"test_loss":test_loss},
                          global_step=epoch) 
        
        writer.add_scalars(main_tag="Accuracy",
                          tag_scalar_dict={"train_acc":train_acc,"test_acc":test_acc},
                          global_step=epoch)
        
        writer.add_graph(model=model,
                         ## pass in an example input
                        input_to_model=torch.randn(32,3,224,224).to(device))
        
        train_end_time = perf_counter()
        
        print(f"total train time took {train_end_time-train_start_time:.2f} seconds on {device}")
    writer.close()
    
    return results
         
