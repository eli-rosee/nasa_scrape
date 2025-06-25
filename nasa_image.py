# imports
from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageDraw, ImageFont
import shutil
import textwrap

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

    image_title = image_block.find('p', 'heading-22').text
    image_text = image_block.find('p', 'p-md').text
    image_src = image_block.find('img').attrs['src']

    # if the image src was successfully obtained, run the rest of program
    if image_src:

        # request the image file specifically with a get request
        r = requests.get(image_src, stream=True)

        # opens up a file for the image and dumps the binary into it
        with open('images/daily_image.png', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

        # opens the file and displays it to the user
        with Image.open('images/daily_image.png') as image:
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default(20)
            rgb_image = image.load()

            width, height = image.size
            r, g, b = rgb_image[width/2, height - 25]

            color = (255 - r, 255 - g, 255 - b)

            text_list = []
            
            for line in textwrap.wrap(image_text, width/15):
                # Draw the text
                text_list.append(line)
            
            text_list.reverse()
            
            for i, line in enumerate(text_list):
                draw.text((width/2, height - (i * 25)), line, fill=color, font=font, align='center', anchor='md')

            image.show(image_title)

            image.save('images/daily_image_text.png')

    else:
        print("Error: image download could not be found.")
else:
   print("Error: website could not be scraped.")
