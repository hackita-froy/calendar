import requests
import random

def get_historic_death(month, day):
  url = 'http://history.muffinlabs.com/date/{month}/{day}'.format(month=month,day=day)
  response = requests.get(url)
  return random.choice(response.json()['data']['Deaths'])
