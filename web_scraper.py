import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

fact_sections = soup.find_all('section')

bu_facts = []

for sec in fact_sections:
    bu_fact = {}

    title = sec.find('h4')
    bu_fact['category'] = title.get_text().strip()
    
    for fact_list in sec.find('ul').find_all('li'):
        label = fact_list.find('span', class_='stat-label').get_text().strip()
        stat = fact_list.find('span', class_='stat-figure').get_text().strip()
        bu_fact[f'{label}'] = stat
       
    bu_facts.append(bu_fact)

with open('bu_facts.json', 'w') as f:
    json.dump(bu_facts, f, indent=4)





