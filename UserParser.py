from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import itemgetter

import logging
import time
import json
import ast
import re
import wikipediaapi


if __name__ == "__main__":

    all_users = []


    for i in range(10):
        user = {}
        user['Name'] = ''
        user['Birthday'] = ''
        user['FavoriteStudio'] = ''
        user['FavoriteAnimation'] = ''
        user_json = ast.literal_eval(json.dumps(user))
        all_users.append(user_json)

    with open('UserProfiles.json', 'w') as outfile:
        json.dump(all_users, outfile, indent=4)
