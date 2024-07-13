# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import time
from nifiapi.properties import PropertyDescriptor
from nifiapi.properties import StandardValidators
from nifiapi.properties import ExpressionLanguageScope
from nifiapi.flowfiletransform import FlowFileTransform, FlowFileTransformResult


class UpdateAttributeFileLookup(FlowFileTransform):
    """This processor sets the latest known date on each flow file passing through.

    This is an example of a processor which meets a specific NiFi community requested need.
    In their case they have a file with a specific naming pattern sitting in a directory.
    They want to always know the date value extracted from the name of the file in that directory
    and place it on any flowfiles passing through a specific point in the flow.  This processor
    does exactly that.
    """

    class Java:
        implements = ['org.apache.nifi.python.processor.FlowFileTransform']

    class ProcessorDetails:
        version = '0.0.3-SNAPSHOT'

    DIRECTORY = PropertyDescriptor(
        name='Directory',
        description='Directory To Read for File with Date Information',
        expression_language_scope=ExpressionLanguageScope.FLOWFILE_ATTRIBUTES,
        validators=[StandardValidators.FILE_EXISTS_VALIDATOR],

    )

    PROPERTIES = [DIRECTORY]

    def __init__(self, jvm, **kwargs):
        super().__init__()
        self.extracted_date = None
        self.last_extract_time = time.time_ns()

    def transform(self, context, flow_file):
        # Check if time to update extracted date
        curr_time = time.time_ns()
        if not self.extracted_date or ((int(self.last_extract_time) + 10000000000) < curr_time):
            self.last_extract_time = curr_time
            dir_path = context.getProperty(self.DIRECTORY.name).evaluateAttributeExpressions(flow_file).getValue()
            files = []
            try:
                for file_path in os.listdir(dir_path):
                    if os.path.isfile(os.path.join(dir_path, file_path)):
                        files.append(file_path)
            except FileNotFoundError:
                self.logger.info(f"The directory {dir_path} does not exist")
            except PermissionError:
                self.logger.info(f"Permission denied to access files in {dir_path}")
            except OSError as e:
                self.logger.info(f"An unspecified OS error occurred: {e}")

            if len(files) > 0:
                filename = files[-1]
                match = re.match(r'.*-(?P<date_extract>\d{8})-.*', filename)
                if match:
                    self.extracted_date = match.group('date_extract')

        if self.extracted_date:
            return FlowFileTransformResult(relationship="success", attributes={"extracted-date": self.extracted_date})
        else:
            return FlowFileTransformResult(relationship="failure")

    def getPropertyDescriptors(self):
        return self.PROPERTIES