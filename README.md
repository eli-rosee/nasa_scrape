# NASA Daily Image Scraper

This Python script fetches NASA's "Image of the Day" and adds the description as a text overlay on the image. The final result is then displayed.

## Features

- Web scraping with 'BeautifulSoup'
- Image display / overlay with 'Pillow'
- Daily reuse support with Bash script
- '.gitignore' and 'requirements.txt' for a clean repo setup

## How to Run (with listed bash commands)

1. Clone the repo:
    git clone https://github.com/eli-rosee/nasa_scrape
    cd nasa_scrape

2. Set up the virtual environemnt (optional)
    python3 -m venv .venv
    source .venv/bin/activate

3. Install dependencies
    pip install -r requirements.txt

4. Run the scraper:
    ./daily.sh

## Cleanup

Each run removes the previous image files and creates updated ones using the 'daily.sh' script.

## Dependencies

- 'beautifulsoup4'
- 'requests'
- 'Pillow'
- 'lxml'
