# Scrapy similier to BeautifulSoup but used when scrape massive website, massive amount of data
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
# responce for next page
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# print(res.text)
# till now we use request to get data here in res we get html format of webiste link
# now we use beautiflsoup to beautify the information

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup.body.contents)
# we can use soup. then any html code and it will print it the first iteam but in find all it will display all
# print(soup.find_all('div'))

# css selector(like class,id,elements...)
# here we want to select class score and '.' is notation for class and for id it is #
links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
