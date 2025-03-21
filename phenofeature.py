import numpy as np
import pandas as pd

l_dim = 4
modalities = ["m1", "m2", "m3"]

category_to_features = {
    '1. Modality1': ['X1', 'X2', 'X3', 'X4', 'X5'],
    '2. Modality2': ['X6', 'X7', 'X8', 'X9', 'X10'],
    '3. m1': [f"{modalities[0]}_{i}" for i in range(1,1+l_dim)],
    '4. m2': [f"{modalities[1]}_{i}" for i in range(1+l_dim,1+l_dim*2)],
    '5. m3': [f"{modalities[2]}_{i}" for i in range(1+l_dim*2,1+l_dim*3)]
}
