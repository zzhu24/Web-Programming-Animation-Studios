from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import itemgetter

import logging
import time
import json
import ast
import re
import wikipediaapi

def FindAllAnimation(quote_page):
    try:
        page = urlopen(quote_page)
    except:
        return ""

    soup = BeautifulSoup(page, "lxml")

    table = soup.find("table", {"class" : "wikitable sortable"})

    if table is None:
        logging.warning("Cannot Find Filmography Information")
        return None


    table_body = table.find("tbody")
    table = table_body.findAll("tr")

    animation = []
    last = ""
    for tr in table:
        all_td = tr.find("td")
        if all_td is not None:
            if "2018" >= all_td.text >= "1800":
                year = all_td.text
            else:
                year = last
            last = year
            all_a = all_td.find("a")
            if all_a is None:
                all_td = all_td.find_next_sibling()
                all_a = all_td.find("a", href = True, title = True)
            if(all_a):
                name = all_a["title"]
                if "(" in name:
                    name = name[0: name.index("(")-1]
                temp_url = "https://en.wikipedia.org"+all_a["href"]
                animation.append((name, temp_url, year.replace('\n',"")))


    return animation



def FindAnimeInfo(infopage):
    try:
        page = urlopen(infopage)
    except:
        return ""

    soup = BeautifulSoup(page, "lxml")

    table = soup.find('table', {'class': 'infobox'})
    if(table == None):
        logging.warning("Cannot Find Cast Information")
        return None

    director = ''
    producer = ''
    release = ''
    image = table.find('img')['src']
    image = "https:"+image


    for tr in table.find_all('tr'):
        text = tr.text
        if 'Direct' in text:
            rows = tr.find_all('a')
            for i in rows:
                director = i.text
        if 'Written' in text or 'Produce' in text:
            rows = tr.find_all('a')
            for i in rows:
                producer = i.text
        if 'run' in text:
            rows = tr.find_all('a')
            for i in rows:
                release = i.text
    return (image, director, producer, release)






if __name__ == "__main__":

    '''
    animations = FindAllAnimation('https://en.wikipedia.org/wiki/List_of_Studio_Ghibli_works')

    all_studios = []

    ghibli = {}
    ghibli['Studio Name'] = 'Ghibli Studio'
    ghibli['Studio Url'] = 'https://en.wikipedia.org/wiki/List_of_Studio_Ghibli_works'
    ghibli['Native Name'] = '株式会社スタジオジブリ'
    ghibli['Image'] = 'https://upload.wikimedia.org/wikipedia/en/c/ca/Studio_Ghibli_logo.svg'
    ghibli['Information'] = 'Studio Ghibli, Inc. (Japanese: 株式会社スタジオジブリ Hepburn: Kabushiki gaisha Sutajio Jiburi) is a Japanese animation film studio based in Koganei, Tokyo, Japan.[1] The studio is best known for its anime feature films, and has also produced several short films, television commercials, and one television film. It was founded on 15 June 1985, after the success of Nausicaä of the Valley of the Wind (1984), with funding by Tokuma Shoten.'
    ghibli['Animations'] = []

    for anime in animations:
        (name, url, year) = anime
        (image, director, producer, release) = FindAnimeInfo(url)
        single_anime = {}
        single_anime['Anime Name'] = name
        single_anime['Anime Url'] = url
        single_anime['Release'] = year
        single_anime['Anima Image'] = image
        single_anime['Director'] = director
        single_anime['Producer'] = producer
        single_anime['Description'] = ''
        anime_json = ast.literal_eval(json.dumps(single_anime))
        ghibli['Animations'].append(anime_json)

    ghibli_studio = ast.literal_eval(json.dumps(ghibli))
    all_studios.append(ghibli_studio)

    with open('Information.json', 'w') as outfile:
        json.dump(all_studios, outfile, indent=4)
    


    json_data = open("Information.json").read()
    all_studios = json.loads(json_data)

    animations = FindAllAnimation('https://en.wikipedia.org/wiki/Bones_(studio)')

    bones = {}
    bones['Studio Name'] = 'Bones Studio'
    bones['Studio Url'] = 'https://en.wikipedia.org/wiki/Bones_(studio)'
    bones['Native Name'] = '株式会社 ボンズ'
    bones['Image'] = 'https://en.wikipedia.org/wiki/Bones_(studio)#/media/File:Bones_logo.svg'
    bones['Information'] = 'Bones Inc. (Japanese: 株式会社 ボンズ Hepburn: Kabushiki-gaisha Bonzu) is a Japanese anime studio. It has produced numerous series, including Noragami, Wolfs Rain, Scrapped Princess, Eureka Seven, Angelic Layer, Darker than Black, Soul Eater, Ouran High School Host Club and two adaptions of the Fullmetal Alchemist manga along with Star Driver, Gosick, Space Dandy, and My Hero Academia. Its headquarters is located in Igusa, Suginami, Tokyo.'
    bones['Animations'] = []

    for anime in animations:
        (name, url, year) = anime
        (image, director, producer, release) = FindAnimeInfo(url)
        single_anime = {}
        single_anime['Anime Name'] = name
        single_anime['Anime Url'] = url
        single_anime['Release'] = release
        single_anime['Anima Image'] = image
        single_anime['Director'] = director
        single_anime['Producer'] = producer
        single_anime['Description'] = ''
        anime_json = ast.literal_eval(json.dumps(single_anime))
        bones['Animations'].append(anime_json)

    bones_studio = ast.literal_eval(json.dumps(bones))
    all_studios.append(bones_studio)

    with open('Information.json', 'w') as outfile:
        json.dump(all_studios, outfile, indent=4)

    '''


    json_data = open("GhibliStudios.json").read()
    all_studios = json.loads(json_data)

    '''
    animations = FindAllAnimation('https://en.wikipedia.org/wiki/A-1_Pictures#Films')

    aniplex = {}
    aniplex['Studio Name'] = 'Aniplex Studio'
    aniplex['Studio Url'] = 'https://en.wikipedia.org/wiki/A-1_Pictures'
    aniplex['Native Name'] = '株式会社エー・ワン・ピクチャーズ'
    aniplex['Image'] = 'https://upload.wikimedia.org/wikipedia/commons/d/d9/A-1_Pictures_Logo.svg'
    aniplex['Information'] = 'A-1 Pictures Inc. (Japanese: 株式会社エー・ワン・ピクチャーズ Hepburn: Kabushiki-gaisha Ē wan pikuchāzu) is a Japanese animation studio founded by ex-Sunrise producer Mikihiro Iwata, a subsidiary of Sony Music Entertainment (Japan)s anime production firm Aniplex.'
    aniplex['Animations'] = []

    for anime in animations:
        (name, url, year) = anime
        (image, director, producer, release) = FindAnimeInfo(url)
        single_anime = {}
        single_anime['Anime Name'] = name
        single_anime['Anime Url'] = url
        single_anime['Release'] = release
        single_anime['Anima Image'] = image
        single_anime['Director'] = director
        single_anime['Producer'] = producer
        single_anime['Description'] = ''
        anime_json = ast.literal_eval(json.dumps(single_anime))
        aniplex['Animations'].append(anime_json)

    aniplex_studio = ast.literal_eval(json.dumps(aniplex))
    all_studios.append(aniplex_studio)

    with open('Information.json', 'w') as outfile:
        json.dump(all_studios, outfile, indent=4)
    '''