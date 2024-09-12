import numpy as np
import torch
import os
from utils.options import pth_root

def save_grad(idxs_users:np.ndarray,grad_records:list,epoch:int):
    '''Given series of updated gradients, pickle out the tensor data.
    
    idxs_users: updated users' ids
    grad_records: the users' gradient tensors
    '''
    for i in range(len(grad_records)):
        filename = f'e{epoch:03d}-{i:02d}-user{idxs_users[i]}.pth'
        filepath = os.path.join(pth_root,filename)
        torch.save(grad_records[i],filepath)