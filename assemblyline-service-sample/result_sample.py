from assemblyline_v4_service.common.base import ServiceBase
from assemblyline_v4_service.common.request import ServiceRequest
from assemblyline_v4_service.common.result import Result, ResultSection

class Sample(ServiceBase):
    def __init__(self, config=None):
        super(Sample, self).__init__(config)

    def start(self):
        # ==================================================================
        # Startup actions:
        #   Your service might have to do some warming up on startup to make things faster
        # ==================================================================

        self.log.info(f"start() from {self.service_attributes.name} service called")

    def execute(self, request: ServiceRequest) -> None:
        # ==================================================================
        # Execute a request:
        #   Every time your service receives a new file to scan, the execute function is called.
        #   This is where you should execute your processing code.
        #   For this example, we will only generate results ...
        # ==================================================================

        # 1. Create a result object where all the result sections will be saved to
        result = Result()

        # 2. Create a section to be displayed for this result
        text_section = ResultSection('Example of a default section')

        # 2.1. Add lines to your section
        text_section.add_line("This is a line displayed in the body of the section")

        # 2.2. Your section can generate a score. To do this it needs to fire a heuristic.
        #     We will fire heuristic #1
        text_section.set_heuristic(1)

        # 2.3. Your section can add tags, we will add a fake one
        text_section.add_tag("network.static.domain", "cyber.gc.ca")

        # 3. Make sure you add your section to the result
        result.add_section(text_section)

        # 4. Wrap-up: Save your result object back into the request
        request.result = result
