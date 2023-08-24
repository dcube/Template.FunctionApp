#!/bin/bash

RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[34m"
YELLOW="\e[33m"
BOLD="\e[1m"

ENDCOLOR="\e[0m"

cd /workspaces/app/function_app/

echo -e "\n${YELLOW}> Pyright / Pylance.${ENDCOLOR}"
result=$(pyright /workspaces/app/function_app -p /workspaces/app/function_app/tools/pyrightconfig.json)

if [ "$?" -eq 0 ]; then
    echo -e "${GREEN}${BOLD}Success: $result${ENDCOLOR}"
else
    echo -e $result
fi

echo -e "\n${YELLOW}> Pylint.${ENDCOLOR}"
pylint /workspaces/app/function_app --score=false

if [ "$?" -eq 0 ]; then
    echo -e "${GREEN}${BOLD}Success: no issues found${ENDCOLOR}"
fi

echo -e "\n${YELLOW}> Mypy.${ENDCOLOR}"
mypy . --exclude '/(venv|site-packages|node_modules|__pycache__|\..*)/$'

echo -e "\n${YELLOW}> Flake8.${ENDCOLOR}"
flake8 /workspaces/app/function_app

if [ "$?" -eq 0 ]; then
    echo -e "${GREEN}${BOLD}Success: no issues found${ENDCOLOR}"
fi

echo -e "\n${YELLOW}> Yapf.${ENDCOLOR}"
yapf --diff /workspaces/app/function_app --recursive

if [ "$?" -eq 0 ]; then
    echo -e "${GREEN}${BOLD}Success: no issues found${ENDCOLOR}"
fi

echo -e "\n${BLUE}All verifications are done.${ENDCOLOR}\n"
