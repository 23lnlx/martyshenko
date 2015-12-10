import numpy as np
import pandas as pd
def make_pheta_i(data):
    logic_data = data.isnull()
    ssv = logic_data.sum().sum() #сумма по всем v_ij
    sv = logic_data.sum() #сумма по столбцам
    q_j = ssv/sv
    sq_j = q_j[q_j != np.inf].sum() # стобцы со всеми заполненными строками не участвуют
    q_j[q_j == np.inf] = sq_j #чтоб бесконечности не было
    Q_j = q_j / sq_j
    pheta_table = Q_j * logic_data
    pheta_i = pheta_table.sum(axis=1)
    return pheta_i