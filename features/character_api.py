import requests

def get_character_info(name):
  url = "https://www.demonslayer-api.com/api/v1/characters"
  params = {"name": name} 

  response = requests.get(url, params=params)
  if response.status_code != 200:
    return None

  json_data = response.json()

  # API returns a list
  if isinstance(json_data, list):
    return json_data[0] if json_data else None

  # Fallback: { "data": [...] }
  if isinstance(json_data, dict):
    data = json_data.get("data")
    if isinstance(data, list) and data:
      return data[0]

  return None
