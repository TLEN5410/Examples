import bs4
import urllib
import json

zipcode = raw_input("Please enter zip code: ")
uszip_url = 'http://uszip.com/zip/' + zipcode
uszip_conn = urllib.urlopen(uszip_url)
html = uszip_conn.read()
soup = bs4.BeautifulSoup(html)

city = soup.find('title').get_text()
population = soup.find("dt", text="Total population").findNextSibling()
city = soup.select('div.zip-data.clearfix > hgroup > h2')[0]
print city.get_text() + ' Population: ', population.get_text()

key = ''
base_url = 'http://api.wunderground.com/api/' + key 
request_url = base_url + '/conditions/q/' + zipcode + '.json'
wunderground_conn = urllib.urlopen(request_url)
results = json.load(wunderground_conn)
print city.get_text() + ' Temp:', results['current_observation']['temp_f']
