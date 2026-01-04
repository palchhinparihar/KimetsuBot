import requests, json

def get_character_info(name):
  url = f'https://www.demonslayer-api.com/api/v1/characters?name={name}'
  response = requests.get(url)
  if response.status_code == 200:
    json_data = json.loads(response.text)
    if isinstance(json_data, list) and len(json_data) > 0:
      return json_data[0]
    else:
      return None
  else:
    return None