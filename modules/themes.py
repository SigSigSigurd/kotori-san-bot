import json
import requests
import praw
import random
import re
from .anilist import Anilist

class Themes():
    def openingsMoe():
        # get all openings & info
        songs = requests.get('https://openings.moe/api/list.php').json()
        return songs
    
    def search(show, Id, select, songs):
        for song in songs:
            title = song['source']
            opening = song['title']
            cId = Anilist.aniSearch(title)
            if Id == cId and select in opening:
                # TODO: compare anilist titles
                #print('\n' + english + '\n' + romaji + '\n' + ltitle + '\n' + str(english.lower() in ltitle or romaji.lower() in ltitle) + '\n\n')
                video = 'https://openings.moe/video/' + song['file'] + '.mp4'
                try:
                    big = song['song']['artist'] + ' - ' + song['song']['title']
                except Exception as e:
                    print(e)
                    big = 'Video'
                    #await ctx.send('Playing **' + opening + '** of *' + title + '*')
                return {'big' : big, 'video' : video, 'found' : True, 'title': title, 'op/ed': opening}
            
        
        return {'found': False}
    
    def themesMoe(year, mal, which, num):
        config = json.load(open('themes.json', 'r'))
        reddit = praw.Reddit(client_id=config['id'], client_secret=config['secret'], user_agent='Snans')

        which = {
            1 : 'OP',
            2 : 'ED'
        }[which]

        if int(year) < 2000:
            year = str(year)
            year = year[2] + '0s'

        contains = ''
        for wikipage in reddit.subreddit('animethemes').wiki:
            if str(wikipage.name) == str(year):
                contains = wikipage
                break
        
        md = contains.content_md.split('\n')
        
        first = '/anime/' + mal
        second = str(which) + str(num)
        search = first
        info = ''
        for line in md:
            if search in line:
                if search == first:
                    search = second
                else:
                    info = line.split('|')
                    break
        
        if '\"' in info[0]:
            name = info[0].split('\"')[1]
        else:
            name = 'Video'

        video = re.search("(?P<url>https?://[^\s]+)", info[1]).group("url").replace(')', '')

        return {'video' : video, 'name' : name, 'info': info}
        