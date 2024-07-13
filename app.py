# import pandas as pd
# 
# df_arquivo = pd.read_csv("arquivo.txt", sep=";", dtype="str")
# 
# df_arquivo = "As colunas do arquivo. São: " + "-".join([column for column in df_arquivo.columns])
# 
# print(df_arquivo)

import pandas as pd
from io import StringIO

data = """
nome;idade;altura
maria;21;1.65
joão;45;1.71
"""

data_io = StringIO(data)
df = pd.read_csv(data_io, sep=';')
print(df)
