import numpy as np
import pandas as pd
def make_lambd(data, packets_num):
    X_r = data.groupby(level=0).mean()
    X_minus_r = pd.DataFrame(columns = data.columns)
    for packet in range(packets_num):
        X_minus_r.loc[packet] = data.loc[data.index.get_level_values(0) != packet].mean()
    return X_minus_r - X_r