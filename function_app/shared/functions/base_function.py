"""..."""

from typing import Any, Dict

from marshmallow import ValidationError
from .base_schema import BaseSchema

from ..libs.exceptions import ExceptionBadParameter


class BaseFunction:
    """
    Base class for every functions
    """

    format_date: str = "%Y-%m-%d %H:%M:%S"
    schema_model: Any = BaseSchema

    def initialize(self, params: Any) -> Dict[str, str]:
        """
        The function initilizes function parameters

        Args:
            params(Any): list of parameters of the function

        Returns:
            Dict[str, str]: list of accepted parameters parameters

        Exceptions:
            ExceptionBadParameter: raise exception if input parameters are not accepted
        """

        try:
            new_params: Dict[str, str] = self.schema_model().load(params)
        except ValidationError as err:
            raise ExceptionBadParameter("Bad Parameter.", err) from err

        return new_params
