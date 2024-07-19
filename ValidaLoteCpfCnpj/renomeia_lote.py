
import pytz 
from random import sample
from secrets import token_hex
from datetime import datetime


def renomeia_lote(erro=None) -> str:
    TZ = pytz.timezone("America/Sao_Paulo")
    carimbo = datetime.now(TZ).strftime("%Y%m%d%H%M%S")
    identificador = "".join(sample(token_hex(16),10)).lower()
    if erro is None:
        return f"lote-processado-{carimbo}-{identificador}.txt"
    else:
        return f"erro-lote-processado-{carimbo}-{identificador}.txt"
