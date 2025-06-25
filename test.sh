#!/bin/bash

if [[ -e daily_image.png ]]; then
    rm daily_image.png
fi

python3 daily_nasa_image.py