import numpy as np

def calculate(l):

    if(len(l)!=9):
        raise ValueError(" List must contain nine numbers")
    k=np.array(l).reshape(3,3)


    d= {
        'mean':[k.mean(axis=0),k.mean(axis=1),k.mean().item()],
        'variance':[k.var(axis=0),k.var(axis=1),k.var().item()],
        'standard deviation':[k.std(axis=0),k.std(axis=1),k.std().item()],
        'max':[k.max(axis=0),k.max(axis=1),k.max().item()],
        'min':[k.min(axis=0),k.min(axis=1),k.min().item()],
        'sum':[k.sum(axis=0),k.sum(axis=1),k.sum().item()],

    }
    return d

