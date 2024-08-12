from assemblyline_v4_service.common.base import ServiceBase
from assemblyline_v4_service.common.request import ServiceRequest
from assemblyline_v4_service.common.result import Result, ResultSection
import subprocess

class Diec(ServiceBase):
    def __init__(self, config=None):
        super().__init__(config)

    def start(self):
        self.log.info(f"start() from {self.service_attributes.name} service called")

    def execute(self, request: ServiceRequest) -> None:
        result = Result()
        output = ''

        try:
            output = subprocess.run(f"diec {request._file_path}", text=True, capture_output=True, shell=True)
        except subprocess.CalledProcessError as e:
            self.log.error(f"Error executing diec: {e}")

        if output:
            text_section = ResultSection('Detect it Easy')
            text_section.add_lines(str(output))
            result.add_section(text_section)

        request.result = result
