"""..."""

import logging
from typing import List

import azure.functions as func
from ..shared.functions.queue_trigger_sample import ListeQueueTriggerSample


def main(messages: List[func.ServiceBusMessage]) -> None:
    """..."""

    logging.info("queue_trigger function processed.")
    try:

        obj_function: ListeQueueTriggerSample = ListeQueueTriggerSample()
        obj_function.prepare_and_execute(messages)

    except Exception:
        logging.exception("queue_trigger failed")
