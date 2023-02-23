## Web Scraper for Sitemap XML Files ## 

Description: This program is a command line application that allows the user to scrape URLs, titles, meta descriptions, H1 tag text, and language from webpages listed in a sitemap XML file for a given website. The scraped data is then written to an Excel file.

### Usage: ### 
website_scraper.exe -w \<website-url\> -f <exel-file.xlsx>

\<website-url\> = enter the website url

<exel-file.xlsx> = enter the excel file name that you want to generate


### How to use: ###

Open a command prompt or terminal window.

Navigate to the directory containing the "website_scraper.exe" file.

Open windows command prompt and execute the command: 

website_scraper.exe -w https://dogorfrog.com/ -f DogOrFrog-Data.xlsx

The scraped data will be written to the output Excel file in the same directory as the .exe file.

Alternatively, you can enter the url and filename in start.bat file. save it and double click the start.bat file to start the program.