#!/bin/bash
# Set environmental variables
source ./LoadEnv.sh &>/dev/null

# Run VoiceMail script
$VPYTHON ./VoiceMail.py

# Get date and time
datetime=$(date)

# Send Screenshot to Slack
curl -F file=@Close.png -F "initial_comment=$datetime" -F channels=$CHANNEL_ID -H "Authorization: Bearer ${SLACK_TOKEN}"  https://slack.com/api/files.upload

# Unset Environmental variables
vars=$(cat .env | cut -d '=' -f1)
for var in $vars; do unset $var; done