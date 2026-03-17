#!/usr/bin/bash

# exit on command fail
set -e

# get the absolute path to where the script is located
declare -r SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# get the absolute path of project directory
declare -r PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"





# server environment directory
declare -r DLP_ENV="$PROJECT_DIR/dlp-venv"

# server environment pip
declare -r DLP_ENV_PIP="$DLP_ENV/bin/pip3"

# server environment requirements
declare -r DLP_REQUIREMENTS="$PROJECT_DIR/requirements/dlp.txt"



# ensure that the python environment exists
if [[ ! -d "$DLP_ENV" ]]; then
    python3 -m venv "$DLP_ENV"
    "$DLP_ENV_PIP" install -U yt-dlp-ejs
fi




