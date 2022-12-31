import requests
def PLUGGet_joke():
    """ Gets a Chuck norris joke, returns the joke """
    # https://api.chucknorris.io/jokes/random
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data['value'])
        return data['value']
    else:
        print('Error')
        print(response.status_code)
    pass
