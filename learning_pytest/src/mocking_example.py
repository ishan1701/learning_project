import requests

def get_frm_json_placeholder(url:str):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('<UNK>')

    return response.json()


if __name__ == '__main__':
    print(get_frm_json_placeholder('https://jsonplaceholder.typicode.com/users'))
    
