from re import sub


def valida_cpf(num: str) -> bool:
    """
    Exemplos: '000.000.001-91', '00000000191' ou '191'
    Referência: https://www.macoratti.net/alg_cpf.htm
    """
    try:
        num = sub(r"[^0-9]", "", num)
        if not num.isdigit():
            raise ValueError("num inválido!")
        num = num.zfill(11)
        radical = list(num)[:-2]
        dv = list(num)[-2:]
        num_cal = 10
        soma1 = 0
        for x in radical:
            soma1 = soma1 + (num_cal * int(x))
            num_cal = num_cal - 1
        calc_dv_1 = soma1 % 11
        if calc_dv_1 < 2:
            dv_1 = 0
        else:
            dv_1 = 11 - calc_dv_1
        try:
            num_cal = 11
            soma2 = 0
            radical.append(str(dv_1))
            for x in radical:
                soma2 = soma2 + (num_cal * int(x))
                num_cal = num_cal - 1
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
    num_cpf = "000.000.001-91"
    if valida_cpf(num_cpf):
        print("CPF Válido!")
    else:
        print("CPF Inválido!")
