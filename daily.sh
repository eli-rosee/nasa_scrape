#!/bin/bash

if [[ -e daily_image.png ]]; then
    rm daily_image.png
fi

if [[ -e daily_image_text.png ]]; then
    rm daily_image_text.png
fi

python3 daily_nasa_image.py