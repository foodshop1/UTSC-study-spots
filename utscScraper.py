import requests
from bs4 import BeautifulSoup

url = 'https://www.utsc.utoronto.ca/studentexperience/study-space'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


tables = soup.find_all('table') #returns list of all table tags 
data = {}


# print the first table's rows (tables[0] is the only table on the site, we use this just to be safe)
for row in tables[0].find_all('tr'): #loop through all of the rows of the table
    cells = row.find_all(['td']) #list of all   
    row_text = []  # create an empty list for this row
    for cell in cells:
        text = cell.text.strip()
        row_text.append(text)
    print (row_text)




#TODO: put the data into a dictionary ie: the room title, room num, capacity, etc