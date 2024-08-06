import requests

WEBSITES = [
    'https://graphql.anilist.co',
    'https://kitsu.io/api/edge'
]

def fetch_anime_data(query):
    url = 'https://graphql.anilist.co'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json={'query': query}, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def get_weekly_top_anime():
    query = '''
    {
      Page {
        media(sort: POPULARITY_DESC, type: ANIME, season: WINTER, seasonYear: 2024) {
          title {
            romaji
            english
          }
          id
        }
      }
    }
    '''
    data = fetch_anime_data(query)
    if data and 'data' in data and 'Page' in data['data']:
        return data['data']['Page']['media']
    return None

# Add other API functions (get_trending_anime, search_anime, etc.) here
