# imports
from bs4 import BeautifulSoup
import requests
from PIL import Image
import shutil

# declares url base and sends a get request to the website
url_base = 'https://www.nasa.gov/'
https_response = requests.get(url_base)

# only runs the program if the get response is confirmed
if https_response.status_code == 200:

    # extracts the html text from the get request and turns it into soup
    html_page = https_response.text
    soup = BeautifulSoup(html_page, 'lxml')

    # extracts the image's rc from the specified div / img block
    image_block = soup.find('div', 'hds-image-of-the-day')
    image_src = image_block.find('img').attrs['src']

    # if the image src was successfully obtained, run the rest of program
    if image_src:
        print(image_src)

        # request the image file specifically with a get request
        r = requests.get(image_src, stream=True)

        # opens up a file for the image and dumps the binary into it
        with open('daily_image.jpg', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

        # opens the file and displays it to the user
        with Image.open('daily_image.jpg') as image:
            image.show('Nasa Daily Image')

    else:
        print("Error: image download could not be found.")
else:
   print("Error: website could not be scraped.")
