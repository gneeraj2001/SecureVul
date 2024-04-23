import requests
def fetch_data(URL):
    # fetch data from API using requests library
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(""Error: "", e)
        return None

def get_data(data):
    # get data from API using json library
    try:
        return data['results'][0]['title']
    except:
        return None

def get_data_from_url(url):
    # get data from API using url library
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(""Error: "", e)
        return None

def get_data_from_url_and_data(url, data):
    # get data from API using url and data library
    try:
        response = requests.get(url, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(""Error: "", e)
        return None

def get_data_from_url_and_data_and_data(url, data, data2):
    # get data from API using url and