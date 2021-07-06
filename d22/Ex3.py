import requests

from bs4 import BeautifulSoup
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="internship"
)
dbse = mydb.cursor()


url_to_scrape = 'https://en.wikipedia.org/wiki/Main_Page'
plain_html_text = requests.get(url_to_scrape)
soup = BeautifulSoup(plain_html_text.text, "html.parser")
print(soup.prettify())
