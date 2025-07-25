# :milky_way: NASA Daily Image Scraper

This Python script fetches NASA's "Image of the Day" and adds the description as a text overlay on the image. The final result is then displayed.

## :wrench: Features

- Web scraping with _BeautifulSoup_
- Image display / overlay with _Pillow_
- Daily reuse support with Bash script
- ._gitignore_ and _requirements.txt_ for a clean repo setup

## :camera: Example Output

![Alt text](images/readme_image.png?raw=true "Nasa Daily Image with Description Overlay")

## :rocket: How to Run (with listed bash commands)

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

## :broom: Cleanup

Each run removes the previous image files and creates updated ones using the _daily.sh_ script.

## :package: Dependencies

- _beautifulsoup4_
- _requests_
- _Pillow_
- _lxml_

## :robot: Future Improvements

- Add auto-upload feature to a website or social media
- Schedule daily automation on PC and output to wallpaper
- Scrape the entirety of the daily image archives on the nasa site

## :artificial_satellite: Credits

Images and descriptions are provided by [NASA.gov](https://www.nasa.gov).
