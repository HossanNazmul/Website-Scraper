__author__ = "Nazmul Hossan"
__version__ = "1.0.0.0"
__email__ = "n.hossan@gmx.de"

# A python program to scrap a website sitemap .xml file and do the followings:
#   - the user provides a website address
#   - scrap all urls that are availble in the sitemap .xml file or .xml files for the given website
#   - iterate through every url and parse the Webpage URL, Title, Meta Description, H1 Tag Text, Language.
#   - write these information to an excel file

# required libraries
# pip install requests
# pip install beautifulsoup4
# pip install lxml
# pip install openpyxl
# pip install argparse

import argparse
import requests
from bs4 import BeautifulSoup
from lxml import etree
import re
import openpyxl

# Function to scrape sitemap.xml files
def scrape_sitemap_xml(url):
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.content, 'lxml')
    urls = []
    for loc in soup.find_all('loc'):
        urls.append(loc.text)
        print(loc.text)
    return urls

# Function to scrape webpages and extract required information
def scrape_webpage(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'lxml')
    title = soup.title.string.strip() if soup.title else ''
    description = soup.find('meta', attrs={'name': 'description'})
    description = description['content'].strip() if description else ''
    h1 = soup.find('h1').text.strip() if soup.find('h1') else ''
    language = soup.html['lang'] if 'lang' in soup.html.attrs else ''
    print('Parsing ', url, 'website data: ', title, ' - ', description, ' - ', h1, ' - ', language)
    return [url, title, description, h1, language]

# Main function to run the application
def main(website_url, excel_filename):
    #website_url = input('Enter website URL: ')
    #excel_filename = input('Enter the filename (e.g. data.xlsx) : ')
    sitemap_urls = re.findall(r'<loc>(.*?)<\/loc>', requests.get(f'{website_url}/sitemap.xml').text)
    urls = []
    for sitemap_url in sitemap_urls:
        print("Found sitemap: ", sitemap_url)
        if sitemap_url.endswith('.xml'):
            urls += scrape_sitemap_xml(sitemap_url)
        else:
            urls.append(sitemap_url)
    data = []
    for url in urls:
        data.append(scrape_webpage(url))
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.append(['Webpage URL', 'Title', 'Meta Description', 'H1 Tag Text', 'Language'])
    for row in data:
        worksheet.append(row)
    workbook.save(excel_filename)
    print('Total', len(urls), ' URLs found in ', website_url, ' and ', len(data), ' entries written to', excel_filename)

if __name__ == '__main__':
    print('Website Scraper Tool version ', __version__, ' by Nazmul Hossan (n.hossan@gmx.de)')
    print('This program is a command line application that allows the user to scrape URLs, ')
    print('Titles, Meta descriptions, H1 Tag text, and Language from webpages listed in a sitemap XML file for a given website.')
    print('The scraped data is then written to an Excel file.')
    parser = argparse.ArgumentParser("WebsiteScraper")
    parser.add_argument('-w', '--website', help='Website URL', required=True, default='')
    parser.add_argument('-f', '--file', help='Filename.xlsx', required=False, default='Website-Data.xlsx')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Show log messages in console')
    arguments = parser.parse_args()

    if arguments.website != "":
        main(arguments.website, arguments.file)
    else:
        print("Argument missing! enter the website url (e.g. https://example.com/) and filename.xlsx . type -h/--help for details")
