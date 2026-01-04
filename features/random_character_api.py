import requests
import random

def get_random_character():
  import random
  url = 'https://www.demonslayer-api.com/api/v1/characters'
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    if data and isinstance(data, list):
      return random.choice(data)  # Return a random character dict
    else:
      return None  # No characters found
  else:
    return None  # Failed to fetch