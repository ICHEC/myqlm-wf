import pandas as pd
import numpy as np
from features2qubits import RadialEncoding

# load data
data_train = pd.read_csv("data/train_32.csv", header=0)
features = ['B02', 'B03', 'B04', 'B08']

x_train = np.array(data_train[features].values, dtype=float)

encoding = RadialEncoding(
    max_feature=np.max(x_train), shift=1., scaling=5.4, n_features=len(features)
    )
qbits0 = encoding.encode(x_train[0])
print(qbits0)