import json
import ast

def ParseStudio(studio_info):

    studio_json = []

    for item in studio_info:
        studio = {}
        studio['Name'] = item['Studio Name']
        studio['Url'] = item['Studio Url']
        studio['Japanese'] = item['Native Name']
        studio['Image'] = item['Image']
        studio['Information'] = item['Information']
        single = ast.literal_eval(json.dumps(studio))
        studio_json.append(single)

    with open('StudiosInfo.json', 'w') as outfile:
        json.dump(studio_json, outfile, indent=4)


def ParseAnimations(anime_info):

    animation_json = []

    for item in anime_info:
        single_anime = {}
        single_anime['Name'] = item['Anime Name']
        single_anime['Url'] = item['Anime Url']
        single_anime['Release'] = item['Release']
        single_anime['Image'] = item['Anima Image']
        single_anime['Director'] = item['Director']
        single_anime['Producer'] = item['Producer']
        single_anime['Description'] = item['Description']
        single = ast.literal_eval(json.dumps(single_anime))
        animation_json.append(single)

    with open('AniplexAnimations.json', 'w') as outfile:
        json.dump(animation_json, outfile, indent=4)


if __name__ == "__main__":
    json_data = open("GhibliStudios.json").read()
    # all_studios = json.loads(json_data)

    # ParseStudio(all_studios)

    # ParseAnimations(all_studios[2]['Animations'])
