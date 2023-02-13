import requests
import urllib3
from bs4 import BeautifulSoup


def soup(contents):
    soup = BeautifulSoup(contents.content, 'html.parser')
    jobs = soup.find('main',class_='main')
    jobs1 = jobs.find_all('div', class_='home-post-box')
    with open('text.txt', 'w') as file:
        for results in jobs1:
            head_title = results.find('h2', class_='home-title')
            tag = results.find('span', class_='h-tags')
            contents = results.find('div', class_='home-desc')
            # print('Title: ',head_title.text)
            # if tag == None:
            #     continue
            # else:
            #     print('Tag: ',tag.text)
            # print('Contents: ',contents.text)
            # print()
            file.write(head_title.text.strip())
            print('\n')
            if tag == None:
                continue
            else:
                file.write(tag.text.strip())
            file.write(contents.text.strip())
    
    return results

def write_contents(contents):
    contents = soup(contents)
    with open('file.txt', 'w') as file:
        file.write(str(contents._content))
        file.close()
        
def read_contents(contents):
    with open('file.txt', 'r') as read_file:
        read_file.read(int(contents))

url = "https://thehackernews.com/search/label/Cyber%20Attack"
web_scrape = requests.get(url)
contents = soup(web_scrape)
# print(contents)
# write = write_contents(web_scrape)
# read = read_contents(write)
# print(write)


