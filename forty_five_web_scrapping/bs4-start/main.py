from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_web = response.text

soup = BeautifulSoup(yc_web, 'html.parser')

articles = soup.find_all(class_='storylink')
points = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

article_text = []
article_link = []

for article_tag in articles:
    art_text = article_tag.getText()
    article_text.append(art_text)
    art_link = article_tag.get('href')
    article_link.append(art_link)

# for x in range(11):
#     print(f'Article: {article_text[x]} \n Link: {article_link[x]} \n Points: {points[x]} \n')

top = points.index(max(points))

print(f'Article: {article_text[top]} \n Link: {article_link[top]} \n Points: {points[top]} \n')







# with open ('website.html') as file:
#     contents = file.read()
#
# # beautiful soup takes content and parser html.parser or lxml
# soup = BeautifulSoup(contents, 'html.parser')
#
# #print(soup.title)
# #print(soup.title.name)
# #print(soup.title.string)
# #indents contents
# #print(soup.prettify())
# #returns first link tag
# #print(soup.a)
#
# all_anchor_tags = soup.find_all(name='a')
#
# for tag in all_anchor_tags:
#     # get text from tags
#     #print(tag.getText())
#     # use .get to get an of the attributes value
#     #print(tag.get('href'))
#     pass
#
# heading = soup.find(name='h1', id='name')
#
# section_heading = soup.find(name='h3', class_='heading')
# #print(section_heading.getText())
#
# #selector acts like a css selector here was are looking for a link tag (a) inside a p tag
# company_url = soup.select_one(selector='p a')
# #print(company_url.get('href'))
#
# #select_one returns the first one it finds, select returns all with the matching selector
# site_heading = soup.select('.heading')
# print(site_heading)

