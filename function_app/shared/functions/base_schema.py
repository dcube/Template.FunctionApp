"""..."""

from typing import Any, Dict, List, Mapping, Union
from marshmallow import Schema, fields, ValidationError


class ServiceField(fields.Field):
    """Field that serializes to a string of numbers and deserializes
    to a list of numbers.
    """

    def _deserialize(
        self,
        value: Union[Any, List[str]],
        attr: Union[None, str],
        data: Union[None, Mapping[str, Any]],
        **kwargs: Dict[str, Any],
    ) -> List[str]:
        """..."""

        if isinstance(value, str):
            list_set = set(value.replace(" ", "").split(","))  # to have unique values
            return list(list_set)

        if isinstance(value, list):
            return value

        raise ValidationError("Services must be provided throught List[str] or str (service names separated by commas).")


class BaseSchema(Schema):
    """..."""
    code = fields.String(required=False)
