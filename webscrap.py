import urllib3
import time
from bs4 import BeautifulSoup

countries = []


def scraper(site_string):
    manager = urllib3.PoolManager()

    site = manager.request('GET', site_string)

    soup = BeautifulSoup(site.data, 'html.parser')
    all_links = soup.findAll('a')
    links1 = all_links[5:]
    next_link = links1[-1]

    for a in links1:
        if a.text.strip() == "< Previous":
            links1.remove(a)

    for b in links1:
        if b.text.strip() != "Next >":
            countries.append(b.text.strip())
        if b.text.strip() == "Next >" and b['href'] != "":
            # print(" to print next page")
            site_string = site_string[0:30] + next_link['href']
            # print(site_string)
            time.sleep(5)
            scraper(site_string)


def print_countries(countries):
    len(countries)
    # for country in countries:
    #     print(country)


if __name__ == '__main__':
    site_string = "http://example.webscraping.com"
    scraper(site_string)
    print_countries(countries)
