from re import sub


def valida_cnpj(num: str) -> bool:
    """
    Exemplos: '00.000.000/0001-91', '00000000000191' ou '191'
    Referência: https://www.macoratti.net/alg_CNPJ.htm
    """
    try:
        num = sub(r"[^0-9]", "", num)
        if not num.isdigit():
            raise ValueError("num inválido!")
        num = num.zfill(14)
        radical = list(num)[:-2]
        dv = list(num)[-2:]
        index_cal = 0
        lista_cal = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma1 = 0
        for x in radical:
            soma1 = soma1 + (lista_cal[index_cal] * int(x))
            index_cal = index_cal + 1
        calc_dv_1 = soma1 % 11
        if calc_dv_1 < 2:
            dv_1 = 0
        else:
            dv_1 = 11 - calc_dv_1
        try:
            index_cal = 0
            lista_cal = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            soma2 = 0
            radical.append(str(dv_1))
            for x in radical:
                soma2 = soma2 + (lista_cal[index_cal] * int(x))
                index_cal = index_cal + 1
            calc_dv_2 = soma2 % 11
            if calc_dv_2 < 2:
                dv_2 = 0
            else:
                dv_2 = 11 - calc_dv_2
            try:
                if "".join(dv).strip() == str(dv_1)+str(dv_2).strip():
                    return True
                else:
                    return False
            except Exception:
                return False
        except Exception:
            return False
    except Exception:
        return False


if __name__ == "__main__":
    num_cnpj = "00.000.000/0001-91"
    if valida_cnpj(num_cnpj):
        print("CNPJ Válido!")
    else:
        print("CNPJ Inválido!")
