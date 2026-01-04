import requests

def get_combat_styles_list():
  url = 'https://www.demonslayer-api.com/api/v1/combat_styles'
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    if data and isinstance(data, list):
      return data  # Return the full list of combat style dicts
    else:
      return []  # No combat styles found
  else:
    return []  # Failed to fetch

def get_combat_style(name):
  url = f'https://www.demonslayer-api.com/api/v1/combat_styles?name={name}'
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    if data and isinstance(data, list) and len(data) > 0:
      return data[0]  # Return the full combat style dict
    else:
      return None  # Not found
  else:
    return None  # Failed to fetch
