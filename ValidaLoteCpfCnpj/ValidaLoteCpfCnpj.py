
from nifiapi.properties import PropertyDescriptor
from nifiapi.properties import StandardValidators
from nifiapi.flowfiletransform import FlowFileTransform
from nifiapi.flowfiletransform import FlowFileTransformResult

class ValidaLoteCpfCnpj(FlowFileTransform):
    class Java:
        implements = ["org.apache.nifi.python.processor.FlowFileTransform"]

    class ProcessorDetails:
        version = "0.0.1-Python"
        description = """
        Este processo é responsável por validar um lote de números
        de CPF ou CNPJ. O lote deve ser disponibilizado no formato .txt ou
        .csv com uma única coluna contendo a descrição 'CPF' ou 'CNPJ'.
        O retorno adicionará uma coluna 'STATUS' com os valores 'True'
        ou 'False' às informações originais.
        """
        tags = ["CPF", "CNPJ", "Validador", "Lote..."]

    VALIDADOR = PropertyDescriptor(
        name = "Tipo documento",
        description = "Escolha o tipo documento que será validado",
        allowable_values = ["CPF", "CNPJ"],
        default_value = "CPF",
        validators = [StandardValidators.NON_EMPTY_VALIDATOR],
        required = True
    )

    property_descriptors = [
        VALIDADOR,
    ]

    def __init__(self, **kwargs):
        pass

    def getPropertyDescriptors(self):
        return self.property_descriptors

    def getDynamicPropertyDescriptor(self, propertyname):
        return PropertyDescriptor(
            name = propertyname,
            description = "Uma propriedade definida pelo usuário",
            validators = [StandardValidators.NON_EMPTY_VALIDATOR],
            dynamic = True
        )

    def transform(self, context, flowfile):
        from io import StringIO

        import pandas as pd

        from renomeia_lote import renomeia_lote
        from valida_cpf import valida_cpf
        from valida_cnpj import valida_cnpj

        try:
            nome_lote = (
                flowfile
                .getAttribute("filename")
            )
            opcao_documento = (
                context
                .getProperty(self.VALIDADOR)
                .evaluateAttributeExpressions(flowfile)
                .getValue()
            )
            conteudo = (
                flowfile
                .getContentsAsBytes()
                .decode()
            )
            conteudo_io = StringIO(conteudo)
            df_base = pd.read_csv(
                conteudo_io,
                sep=";",
                dtype="str"
            )

            if opcao_documento == "CPF":
                df_base.columns = ["CPF"]
                df_base["STATUS"] = df_base["CPF"].apply(valida_cpf)
            else:
                df_base.columns = ["CNPJ"]
                df_base["STATUS"] = df_base["CNPJ"].apply(valida_cnpj)

            df_base = df_base.to_csv(index=False, sep=";")

            atributos = (
                {
                    "mime.type": "text/csv",
                    "filename": renomeia_lote(nome_lote)  
                }
            )

            return FlowFileTransformResult(
                relationship = "success",
                contents = df_base,
                attributes = atributos
            )

        except Exception as erro:
            nome_lote = (
                flowfile
                .getAttribute("filename")
            )
            atributos = (
                {
                    "mime.type": "text/csv",
                    "filename": nome_lote.strip(),
                    "erro": f"{erro}"  
                }
            )
            return FlowFileTransformResult(
                relationship = "failure",
                attributes = atributos
            )
