import requests
import pandas as pd
import json

headers = {"Authorization": "token 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"}
# Loading Users in Boston with follower greater than 100
# url = 'https://api.github.com/search/users?q=location:Boston followers:>100&per_page=100&page={}'
# cur_page, cur_count = 1, 0
# users = []
# while True:
#     response = requests.get(url.format(cur_page), headers=headers).json()
#
#     if 'items' not in response:
#         print(response)
#         break
#
#     if not response['items']:
#         break
#
#     users.extend(response['items'])
#     cur_page += 1
#
# df = pd.DataFrame(users)
# df.to_csv('users.csv')
#
#
# # Loading Repo Data
# def save_repo(row):
#     url = "https://api.github.com/users/{}/repos?per_page=100&page={}"
#     for i in range(5):
#         repo_data.extend(requests.get(url.format(row["login"], i + 1), headers=headers).json())
#
#
# users = pd.read_csv("users.csv")
# repo_data = []
# users.apply(save_repo, axis=1)
# df = pd.DataFrame(repo_data)
# df.to_csv("repo_data.csv")
#
#
# # Loading User Data
# users = pd.read_csv("users.csv")
# user_data = []
# users.apply(lambda row: user_data.append(requests.get(row['url'], headers=headers).json()), axis=1)
# df = pd.DataFrame(user_data)
# df.to_csv("user_data.csv")
#
#
# # Creating user_data
# df = pd.read_csv('user_data.csv')
# df = df.loc[:, ['login', 'name', 'company', 'location', 'email', 'hireable', 'bio',
#                 'public_repos', 'followers', 'following', 'created_at']]
# df['company'] = df['company'].fillna('').astype(str)
# df['company'] = df['company'].apply(lambda x: x.strip())
# df['company'] = df['company'].apply(lambda x: (x[1:] if x and x[0] == '@' else x).upper())
#
# df.to_csv('user_data_.csv', index=False)


# Creating repo_data
df = pd.read_csv('repo_data.csv')
df['login'] = df['full_name'].apply(lambda x: x[:x.index('/')])
df['license'] = df['license'].fillna('').apply(lambda x: x.strip()).astype(str)
df['license'] = df['license'].apply(lambda x: x.split(",")[0].split(':')[1][2:-1] if 'key' in x else x)
df = df.loc[:, ['login', 'full_name', 'created_at', 'stargazers_count', 'watchers_count', 'language',
                 'has_projects', 'has_wiki', 'license']]
df.rename(columns={'license': 'license_name'})

df.to_csv('repo_data_.csv', index=False)

