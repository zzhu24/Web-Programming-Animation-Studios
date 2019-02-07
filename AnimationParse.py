import json
import ast


if __name__ == "__main__":
    '''
    json_data = open("AniplexAnimations.json").read()
    aniplex = json.loads(json_data)


    with open('AnimationsTotal.json', 'w') as outfile:
        json.dump(aniplex, outfile, indent=4)
    '''

    '''
    bones_data = open("BonesAnimations.json").read()
    bones = json.loads(bones_data)

    json_data = open("AnimationsTotal.json").read()
    all_animations = json.loads(json_data)

    for anime in bones:
        all_animations.append(anime)

    with open('AnimationsTotal.json', 'w') as outfile:
        json.dump(all_animations, outfile, indent=4)
    '''

    ghibli_data = open("GhibliAnimations.json").read()
    gihbli = json.loads(ghibli_data)

    json_data = open("AnimationsTotal.json").read()
    all_animations = json.loads(json_data)

    for anime in gihbli:
        all_animations.append(anime)

    with open('AnimationsTotal.json', 'w') as outfile:
        json.dump(all_animations, outfile, indent=4)