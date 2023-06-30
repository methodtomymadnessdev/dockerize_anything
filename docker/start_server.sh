#!/bin/bash

if [[ -z "${DEVELOPMENT_ENVIRONMENT}" ]];
then
    (gunicorn -w 4 'app:app' -b 0.0.0.0:5010) &
fi;
nginx -g "daemon off;";

