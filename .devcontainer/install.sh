#!/bin/bash

sudo chgrp vscode /workspaces/app/.venv
sudo chown vscode /workspaces/app/.venv

python3 -m venv /workspaces/app/.venv
PATH="/workspaces/app/.venv/bin:$PATH"

source /workspaces/app/.venv/bin/activate
pip install --upgrade pip

# pip install keyring artifacts-keyring

# cat <<EOF >> /workspaces/app/.venv/pip.conf
# [global]
# extra-index-url=https://pkgs.dev.azure.com/...
# EOF

pip install -r /workspaces/app/function_app/requirements-dev.txt
pip install -r /workspaces/app/function_app/requirements.txt

# echo 'export PYTHONPATH="${PYTHONPATH}:/workspaces/app/shared"' >> ~/.bashrc
