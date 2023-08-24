"""..."""

from typing import Any, Dict, List, Union, Mapping

import logging

from azure.functions import ServiceBusMessage

from marshmallow import fields, ValidationError

from .base_function import BaseFunction
from .base_schema import BaseSchema


class ServiceBusMessageField(fields.Field):
    """..."""

    def _deserialize(
        self,
        value: Union[Any, List[str]],
        attr: Union[None, str],
        data: Union[None, Mapping[str, Any]],
        **kwargs: Dict[str, Any],
    ) -> List[str]:
        """..."""

        if isinstance(value, list):
            for message in value:
                if not isinstance(message, ServiceBusMessage):
                    raise ValidationError("A list of ServiceBusMessage was expected")
        else:
            raise ValidationError("A list of ServiceBusMessage was expected")

        return value


class ServicesFromServiceBusMessage(fields.Field):
    """..."""

    def _deserialize(
        self,
        value: Union[Any, List[str]],
        attr: Union[None, str],
        data: Union[None, Mapping[str, Any]],
        **kwargs: Dict[str, Any],
    ) -> List[str]:
        """..."""

        services: List[str] = []

        if data is not None:
            messages: List[Any] = data["messages"]

            for message in messages:
                services.append(message.get_body().decode("utf-8"))

            return list(set(services))

        return []


class ListeQueueTriggerSampleSchema(BaseSchema):
    """..."""

    messages = ServiceBusMessageField(required=True)
    services = ServicesFromServiceBusMessage(required=True)


class ListeQueueTriggerSample(BaseFunction):
    """..."""

    schema_model: Any = ListeQueueTriggerSampleSchema

    def prepare_and_execute(self, params: List[ServiceBusMessage]) -> None:
        """..."""

        new_params: Dict[str, Any] = self.initialize({"messages": params, "services": []})

        self.execute(new_params["services"])

    def execute(self, service: str) -> None:
        """..."""

        logging.info("ListeQueueTrigger - running service")
        logging.info("service - %s", service)
