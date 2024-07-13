from nifiapi.flowfiletransform import FlowFileTransform, FlowFileTransformResult

class descobreColunasArquivo(FlowFileTransform):
    class Java:
        implements = ["org.apache.nifi.python.processor.FlowFileTransform"]
    class ProcessorDetails:
        version = "0.0.1-Python"
        dependencies = ["numpy==1.24.4", "pandas==2.0.3", "python-dateutil==2.9.0.post0", "pytz==2024.1", "six==1.16.0", "tzdata==2024.1"]
        description = """Esse processo descobre as colunas existentes em um arquivo de texto separado por ponto e vírgula. """
        tags = ["pandas", "python", "outros..."]

    def __init__(self, **kwargs):
        pass

    def transform(self, context, flowfile):
        import pandas as pd
        from io import StringIO

        input = flowfile.getContentsAsBytes().decode()
        input = StringIO(input)
        df_arquivo = pd.read_csv(input, sep=";")
        output = "As colunas do arquivo: " + "-".join([column for column in df_arquivo.columns])

        return FlowFileTransformResult(
          relationship = "success",
          contents = output,
          attributes = {"transformation": "to_upper_case"}
        )

