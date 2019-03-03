#!/bin/sh

scriptPath=$(dirname "$(readlink -f "$0")")
source "${scriptPath}/.env.sh"

python /app/refresh_dyndns.py -u ${USER_ID} -k ${API_KEY} -d ${DOMAIN}