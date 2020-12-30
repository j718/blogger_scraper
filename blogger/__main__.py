
import requests
from bs4 import BeautifulSoup

posts = []
for year in [2014, 2015]:
    for month in range(1,13):
        formatted_month = f"0{month}" if month < 10 else month
        URL = f'http://sisterkelley.blogspot.com/{year}/{formatted_month}/'
        page = requests.get(URL)
    
        soup = BeautifulSoup(page.content, 'html.parser')
        new_posts = soup.find_all(class_="post-outer")
        print(year, formatted_month, len(new_posts))
        if new_posts:
            posts = posts + new_posts

with open("out.html", "w", encoding="utf-8") as out_file:
    out_file.write("<!DOCTYPE html>")
    out_file.write("""
    <head><style>
img {
    width: 50vh;
    height: auto;
}
</style></head>""")
    out_file.write('<body style="margin-left: 100px; margin-right: 100px;">')
    for post in posts:
        title_raw = post.find(class_="post-title")
        
        title = title_raw.text.strip() if title_raw else "Untitled"
        body = post.find(class_="post-body")
        out_file.write(f"<h1>{title}</h1>")
        out_file.write(str(body))
    out_file.write("</body>")


print('done')