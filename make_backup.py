from requests import Session
from requests.auth import HTTPBasicAuth
import subprocess

username = input('\nEnter your GitHub username: ')
password = input('Enter your GitHub password or personal access token: ')
repos_type = 'owner'

session = Session()

repos = session.get(
    f"https://api.github.com/user/repos?type={repos_type}&per_page=100",
    auth=HTTPBasicAuth(username, password)
).json()

print('\nList of repositories, that you own:\n')
for repo in repos:
    print(repo['full_name'])

print(f"\nNumber of repositories: {len(repos)}\n")

while True:
    answer = input('Do you want to clone all these repositories? (Y/N): ')
    if answer.upper() == 'Y':
        i = 1
        for repo in repos:
            print(f'Repository {i}/{len(repos)}: ', end='')
            subprocess.call(
                ['git', 'clone', f"https://{username}:{password}@github.com/{repo['full_name']}",
                 f"dumps/{repo['full_name'].split('/')[-1]}"])
            i += 1
        break
    elif answer.upper() == 'N':
        break
    else:
        continue

print("\nOk, I'm done here. Goodbye :)")
