from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, "lxml")

csv_file1 = open("scrape.csv", "w")

csv_writer1 = csv.writer(csv_file1)
csv_writer1.writerow(["headline", "summary", "videolink"])


for article in soup.find_all("article"):

    print(article)
    headline = article.h2.a.text
    print(headline)

    summary = article.find("div", class_="entry-content").p.text
    print(summary)

    #this will continue loop if video link is missing in one of the `article`
    try:
        vid_src = article.find("iframe", class_="youtube-player")["src"]
        # print(vid_src)

        vid_id = vid_src.split("/")[4]
        vid_id = vid_id.split("?")[0]
        # print(vid_id)

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except:
        yt_link = None
    print(yt_link)
    print("")

    csv_writer1.writerow([headline, summary, yt_link])

csv_file1.close()