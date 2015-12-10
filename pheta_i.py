import numpy as np
import pandas as pd
def make_pheta_i(data):
    logic_data = data.isnull()
    ssv = logic_data.sum().sum() #����� �� ���� v_ij
    sv = logic_data.sum() #����� �� ��������
    q_j = ssv/sv
    sq_j = q_j[q_j != np.inf].sum() # ������ �� ����� ������������ �������� �� ���������
    q_j[q_j == np.inf] = sq_j #���� ������������� �� ����
    Q_j = q_j / sq_j
    pheta_table = Q_j * logic_data
    pheta_i = pheta_table.sum(axis=1)
    return pheta_i