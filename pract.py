import urllib
from lxml.html import parse
from urllib.request import urlopen

url = urlopen("http://www.mumbaiyellowpages.org/localbook/car-rentals.php")
parsed = parse(url)
# print(parsed)

root = parsed.getroot()
# print(root)
links = root.findall(".//a")
# print(links)
for link in links:
	if "http" in link.get("href"):
		print("<a href=", link.get("href"), ">", link.text, "</a href>")

tables = root.findall(".//table")
print(tables)
i = 6
rows = tables[i].findall(".//tr")
print(rows)
j = 2
data = rows[j].findall(".//td")
print(data)
print(data[1].text_content())
a = data[0].findall(".//div", {"class": "channels_tittle"})
print(a[1].text_content())


