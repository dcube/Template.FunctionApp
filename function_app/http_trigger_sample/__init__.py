""" http_trigger : Azure function endpoint """

import json
import logging
from typing import Any, Dict

import azure.functions as func

from ..shared.functions.http_trigger_sample import HttpTriggerSample


def main(req: func.HttpRequest) -> func.HttpResponse:  # pylint: disable=unused-variable
    """ Main programm """

    logging.info("http_triggered function processed.")

    func.HttpResponse.mimetype = "application/json"  # type: ignore
    func.HttpResponse.charset = "utf-8"  # type: ignore

    try:

        obj_function: HttpTriggerSample = HttpTriggerSample()
        result: str = obj_function.prepare_and_execute(dict(req.params))

        main_result: Dict[str, Any] = {}
        main_result["result"] = result
        main_result["success"] = True
        return func.HttpResponse(json.dumps(main_result), status_code=200)

    except Exception as err:
        logging.exception("http_triggered failed")
        error_result: str = json.dumps({
            "error": str(err),
            "success": False,
        })

        return func.HttpResponse(error_result, status_code=500)
