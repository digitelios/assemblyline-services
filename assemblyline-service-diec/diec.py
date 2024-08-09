from assemblyline_v4_service.common.base import ServiceBase
from assemblyline_v4_service.common.request import ServiceRequest
from assemblyline_v4_service.common.result import Result, ResultSection
import subprocess

class Diec(ServiceBase):
    def __init__(self, config=None):
        super(Diec, self).__init__(config)

    def start(self):
        self.log.info(f"start() from {self.service_attributes.name} service called")

    def execute(self, request: ServiceRequest) -> None:
        result = Result()
        output = ''

        try:
            output = subprocess.check_output('diec ' + request._file_path + request.file_name, shell=True, text=True)
        except subprocess.CalledProcessError as e:
            self.log.error(f"Error executing diec: {e}")

        if output:
            text_section = ResultSection('Detect it Easy')
            text_section.add_lines(str(output))
            result.add_section(text_section)

        request.result = result
