import requests, json

def get_characters_list():
  url = 'https://www.demonslayer-api.com/api/v1/characters'
  response = requests.get(url)
  if response.status_code == 200:
    json_data = json.loads(response.text)
    return json_data
  else:
    return []