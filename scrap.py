import requests
import codecs

from bs4 import BeautifulSoup


def getdata(i):
    url = str(i)
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        links = soup.findAll("p")
        if len(links) != 1:
            txt = soup.findAll("h1")[0].text
            txt += "\n"
            #path = 'E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\Tokenise'

            for t in links:
                txt += t.text
            #filename = path + "\scrapped_text.txt"
            f = open('E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\Tokenise\\scrapped_text.txt', 'a', encoding='utf-8')
            f.write(str(txt))
    else:
        print("error")


def main():
    # print("enter the link\n")
    # ll=input()
    url1 = "http://www.mathrubhumi.com/news/kerala/malayalam/prof-t-j-joseph-abhimanyu-murder-maharajas-college-sfi-popular-front-sdpi-1.2945324"
    getdata(url1)


if __name__ == "__main__":
    main()
