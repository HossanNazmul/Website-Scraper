## Web Scraper for Sitemap XML Files ## 

Description: This program is a command line application that allows the user to scrape URLs, titles, meta descriptions, H1 tag text, and language from webpages listed in a sitemap XML file for a given website. The scraped data is then written to an Excel file.

### Usage: ### 
website_scraper.exe -w \<website-url\> -f <exel-file.xlsx>

\<website-url\> = enter the website url

<exel-file.xlsx> = enter the excel file name that you want to generate


### How to use: ###

Download the "website_scraper.exe" files which are located under "release" folder. 

Open a command prompt or terminal window.

Navigate to the directory containing the "website_scraper.exe" file.

Open windows command prompt and execute the command: 

website_scraper.exe -w https://dogorfrog.com/ -f DogOrFrog-Data.xlsx

The scraped data will be written to the output Excel file in the same directory as the .exe file.

Alternatively, you can enter the url and filename in start.bat file. save it and double click the start.bat file to start the program.


### For Advance user: ###
The program is written in Python and uses the following libraries:

requests
BeautifulSoup
lxml
openpyxl

To use the program, simply run the Python file and enter the URL of the sitemap XML file when prompted. The program will then scrape all URLs in the sitemap file and extract the desired data from each webpage. Finally, the program will prompt the user to enter a name for the output Excel file.

The program also includes error handling to catch and handle exceptions that may occur during scraping. If an error occurs, the program will print an error message to the console and continue scraping as much data as possible.

Note: The program may not work properly for websites that do not have a sitemap XML file or for sitemap files that are not properly formatted. It is recommended to test the program on a small sitemap file before using it on a larger one.

Requirements:

Python 3.x
requests
BeautifulSoup
lxml
openpyxl
Installation:

Install Python 3.x: https://www.python.org/downloads/
Install required libraries using pip:
requests: pip install requests
BeautifulSoup: pip install beautifulsoup4
lxml: pip install lxml
openpyxl: pip install openpyxl
Usage:

Open a command prompt or terminal window.
Navigate to the directory containing the Python file.
Run the Python file: python web_scraper.py
Enter the URL of the sitemap XML file when prompted.
Enter a name for the output Excel file when prompted.
The scraped data will be written to the output Excel file in the same directory as the Python file.