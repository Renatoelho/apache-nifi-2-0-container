from nifiapi.flowfiletransform import FlowFileTransform, FlowFileTransformResult

class TesteProcessorPython(FlowFileTransform):
    class Java:
        implements = ['org.apache.nifi.python.processor.FlowFileTransform']
    class ProcessorDetails:
        version = '0.0.1-SNAPSHOT'

    def __init__(self, **kwargs):
        pass

    def transform(self, context, flowfile):
        # Import Python dependencies
        input = flowfile.getContentsAsBytes().decode()
        # Convert input to upper case
        output = input.upper()
        return FlowFileTransformResult(
          relationship = "success",
          contents = output,
          attributes = {"transformation": "to_upper_case"}
        )

#    def getRelationships(self):
#        return ["success", "failure"]
