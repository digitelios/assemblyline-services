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
        # 1. Create a result object where all the result sections will be saved to
        result = Result()

        try:
            output = subprocess.check_output('diec', shell=True, text=True)
        except subprocess.CalledProcessError as e:
            self.log.error(f"Error executing diec: {e}")

        # 2. Create a section to be displayed for this result
        # 3. Make sure you add your section to the result
        if output:
            text_section = ResultSection(str(output))

            result.add_section(text_section)

        # 4. Wrap-up: Save your result object back into the request
        request.result = result
