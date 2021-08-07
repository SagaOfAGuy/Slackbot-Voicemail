#!/bin/bash
# Set environmental variables
source ./LoadEnv.sh &>/dev/null

# Get virtual environment directory and python3 version
venvpath=$(pipenv --venv)
venvpypath="${venvpath}/bin/python3"

# Run VoiceMail script
$venvpypath ./VoiceMail.py

# Get date and time
datetime=$(date)



# Send Screenshot to Slack
curl -F file=@Close.png -F "initial_comment=$datetime" -F channels=$CHANNEL_ID -H "Authorization: Bearer ${SLACK_TOKEN}"  https://slack.com/api/files.upload

# Unset Environmental variables
vars=$(cat .env | cut -d '=' -f1)
for var in $vars; do unset $var; done

rm ./Close.png
