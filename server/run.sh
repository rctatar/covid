#!/bin/bash
export FLASK_APP=run.py
export FLASK_DEBUG=1
export FLASK_ENV=development
if [ "$1" = "--init" ]; then
  flask db init --recreate
  flask run
else
  flask run --port=8003 $1 $2 $3
fi

