
import pytz 

import os
from pathlib import Path
from random import sample
from secrets import token_hex
from datetime import datetime


def renomeia_lote(nome_lote: str) -> str:
    TZ = pytz.timezone("America/Sao_Paulo")
    carimbo = datetime.now(TZ).strftime("%Y%m%d%H%M%S")
    identificador = "".join(sample(token_hex(16),10)).lower()                                
    nome = Path(os.path.abspath(nome_lote)).stem
    extensao = Path(os.path.abspath(nome_lote)).suffix
    return f"{nome}-processado-{carimbo}-{identificador}{extensao}"
