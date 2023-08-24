"""..."""

import os
from typing import Optional

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def get_key_vault_value(secret_name: str) -> Optional[str]:
    """..."""

    key_vault_name = os.environ["KEY_VAULT_NAME"]
    key_vault_uri = f"https://{key_vault_name}.vault.azure.net"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=key_vault_uri, credential=credential)

    return client.get_secret(secret_name).value  # type: ignore
