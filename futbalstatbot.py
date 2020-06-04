import requests

url = "https://api.telegram.org/bot1163071581:AAHwVpgFOZdTH5zJ9A2zFs9WIF5qadCtCfY/"


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]