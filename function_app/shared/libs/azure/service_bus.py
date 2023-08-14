"""..."""

import os

from typing import List

from azure.servicebus.aio import ServiceBusClient, ServiceBusSender
from azure.servicebus import ServiceBusMessage
from azure.identity.aio import DefaultAzureCredential

from ..exceptions import ExceptionBadParameter


async def _send_a_list_of_messages(sender: ServiceBusSender, elements: List[str]) -> None:
    """..."""

    # Create a list of messages and send it to the queue
    messages: List[ServiceBusMessage] = [ServiceBusMessage(str(element)) for element in elements]
    await sender.send_messages(messages)  # type: ignore


async def prepare_and_send_message(entity: str, elements: List[str]) -> None:
    """..."""

    credential: DefaultAzureCredential = DefaultAzureCredential()
    namespace: str = os.environ["API_STATUS_SERVICEBUS__fullyQualifiedNamespace"]

    # create a Service Bus client using the connection string
    async with ServiceBusClient(
        namespace,
        credential,  # type: ignore
        logging_enable=True,
    ) as servicebus_client:

        if entity == "queue":
            queue_name: str = os.environ["queue_name"]
            sender = servicebus_client.get_queue_sender(queue_name=queue_name)
        elif entity == "topic":
            topic_name: str = os.environ["topic_name"]
            sender = servicebus_client.get_topic_sender(topic_name=topic_name)
        else:
            raise ExceptionBadParameter("Only 'queue' and 'topic' are correct entities.")

        async with sender:
            await _send_a_list_of_messages(sender, elements)
