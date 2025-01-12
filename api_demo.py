import requests

def fetch_random_user():
    url = 'https://jsonplaceholder.typicode.com/users/1'

    try:
        response = requests.get(url)
        response.raise_for_status() # check for any HTTP error

        user = response.text
        return user
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

        return None

def main():
    users = fetch_random_user()
    if users:
        print('User', users)
    else:
        print('Failed to fetch user')

if __name__ == '__main__':
    main()