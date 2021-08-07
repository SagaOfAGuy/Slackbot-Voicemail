#!/bin/bash

# Export environmental variables found in .env file to local environment
grep -v '^#' .env
export $(grep -v '^#' .env | xargs)
