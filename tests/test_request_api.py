# Drake Zeringue
# 10/24/2019

import pytest
import requests

url = 'https://api.duckduckgo.com/?q=presidents of the united states&format=json'
response = requests.get(url)
my_json = response.json()
related_topics_list = my_json['RelatedTopics']

def test_invalid_name():
    contains_pres = False
    for dict in related_topics_list:
        if "Todd" in dict['Text']:
            contains_pres = True
            break
    assert contains_pres == False

@pytest.mark.parametrize("president", ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Jackson', 'Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Truman', 'Eisenhower', 'Kennedy', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Obama', 'Trump'])
def test_valid_names(president):
    contains_pres = False
    for dict in related_topics_list:
        if president in dict['Text']:
            contains_pres = True
            break
    assert contains_pres == True
