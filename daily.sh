#!/bin/bash

if [[ -e images/daily_image.png ]]; then
    rm images/daily_image.png
fi

if [[ -e images/daily_image_text.png ]]; then
    rm images/daily_image_text.png
fi

python3 daily_nasa_image.py