"""..."""

import logging
from typing import Any, Dict, List

from marshmallow import fields, validates_schema, ValidationError
from .base_function import BaseFunction
from .base_schema import BaseSchema, ServiceField


class HttpTriggerSampleSchema(BaseSchema):
    """..."""
    service = fields.String(required=True)
    depends_on = ServiceField(required=False, load_default=[])

    @validates_schema
    def validate_example(self, data: Dict[str, Any], **kwargs: Dict[str, Any]) -> None:  # pylint: disable=unused-argument
        """..."""
        intersection: List[str] = list(set([data["service"]]) & set(data["depends_on"]))

        if len(intersection) >= 1:
            raise ValidationError(f"Service {data['service']} cannot be dependent on itself.")


class HttpTriggerSample(BaseFunction):
    """..."""

    schema_model: Any = HttpTriggerSampleSchema

    def prepare_and_execute(self, params: Dict[str, Any]) -> str:
        """..."""

        new_params: Dict[str, Any] = self.initialize(params)
        return self.execute(new_params["service"], new_params["depends_on"])

    def execute(self, service: str, depends_on: List[str]) -> str:
        """..."""

        logging.info("ListeQueueTrigger - running service")
        logging.info("service - %s", service)
        logging.info("depends_on - %s", depends_on)
        logging.info("service - %s", service)

        return "test"
