# 爬虫练习示例网站 https://scrape.center/

# 爬取网页基本三方库: requests, bs4.beautifulsoup4 
# pip install requests bs4

# 操作 Excel 三方库: pandas, openpyxl
# pip install pandas openpyxl

import hashlib
import json
import math
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

class Movie:
    def __init__(self, name, category, region, duration, online_time, score):
        self.name = name
        self.category = category
        self.region = region
        self.duration = duration
        self.online_time = online_time
        self.score = score

# 一个简单的爬取电影信息的爬虫程序 -> https://ssr1.scrape.center/
class MovieCrawler:
    def get_movie_info(self, url: str) -> list[Movie]:
        result = []
        header = {
        'Referer': 'https://ssr1.scrape.center/', 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        }
        response = requests.get(url, headers=header)
        print('obtain from url {}, response code is {}'.format(url, response.status_code))
        if response.status_code != 200:
            return []
        soup = BeautifulSoup(response.text, 'html.parser')
        block_1 = soup.find_all(name='div', class_='el-card__body')
        for b in block_1:
            name = b.find(name='h2', class_='m-b-sm').text.strip()
            categories = []
            for c in b.find(name='div', class_='categories').find_all(name='button'):
                categories.append(c.span.text)
            divs = b.find_all(name='div', class_='m-v-sm info')
            s1 = divs[0].find_all(name='span')
            region = s1[0].text
            duration = s1[2].text
            online_time_span = divs[1].find(name='span')
            online_time = ''
            if online_time_span is not None:
                online_time = online_time_span.text
            
            score = b.find(name='p', class_='score m-t-md m-b-n-sm').text.strip()
            
            #print(b.find(name='img', class_='cover').get('src'))
            result.append(Movie(name, categories, region, duration, online_time, score))

        return result

    def get_all_movies(self)-> list[Movie]:
        alll_movies = []
        page = 1
        while True:
            url = 'https://ssr1.scrape.center/page/{}'.format(page)
            r = self.get_movie_info(url)
            if not r or len(r) == 0:
                break
            alll_movies.extend(r)
            page += 1
        
        return alll_movies


    def write_to_file(self, movies: list[Movie]):
        movie_data = {
            'Name': [movie.name for movie in movies],
            'Category': [movie.category for movie in movies],
            'Region': [movie.region for movie in movies],
            'Duration': [movie.duration for movie in movies],
            'Online Time': [movie.online_time for movie in movies],
            'Score': [movie.score for movie in movies],
        }
        with pd.ExcelWriter('movies.xlsx', engine='openpyxl') as writer:
            df = pd.DataFrame(movie_data)
            df.to_excel(writer, sheet_name='movies')
    
    def crawler_and_write_excel(self):
        movies = self.get_all_movies()
        self.write_to_file(movies)


class MusicInfo:
    def __init__(self, song_name, singer, album, song_duration, song_play_url):
        self.song_name = song_name
        self.song_play_url = song_play_url
        self.singer = singer
        self.album = album
        self.song_duration = song_duration # 歌曲播放时长

    def get_tsid(self):
        return self.song_play_url.split('/')[2]

    def __str__(self):
        return f"{self.song_name} {self.song_duration}, {self.singer}, {self.album} "

# 爬取千千音乐的爬虫程序 -> https://music.91q.com/search?word=Tiger
class MusicCrawler:
    def request_info(self, keywork: str) -> list[MusicInfo]:
        result = []
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        }
        url = f'https://music.91q.com/search?word={keywork}'
        response = requests.get(url, headers=header)
        bs = BeautifulSoup(response.text, 'html.parser')
        element_ul = bs.find(name='div', class_='song-box').find(name='ul')
        
        for e_li in element_ul.find_all(name='li', class_='pr t clearfix'):
            song_name = e_li.find(name='div', class_='song-box').a.text
            song_play_url = e_li.find(name='div', class_='song-box').a.get('href')

            singer = ''
            for a_p in e_li.find(name='div', class_='artist ellipsis').find_all(name='a'):
                singer += a_p.text + ' '
            
            album = e_li.find(name='div', class_='album ellipsis').a.text
            duration = e_li.find(name='div', class_='time').text
            
            music_info = MusicInfo(song_name, singer, album, duration, song_play_url)
            # print(music_info)
            result.append(music_info)
        
        return result

    def down_music(self, tsid: str, sone_name: str):
        # TSID=T10063954909&appid=16073360&timestamp=17241397190b50b02fd0d73a9c4c8c3a781c30845f
        appid = '16073360'
        secret = '0b50b02fd0d73a9c4c8c3a781c30845f'
        timestamp = math.floor(time.time())
        original_str = f'TSID={tsid}&appid={appid}&timestamp={timestamp}'

        md5_hash = hashlib.md5()
        md5_hash.update(f'{original_str}{secret}'.encode('utf-8'))
        sign = md5_hash.hexdigest()
        # https://music.91q.com/v1/song/tracklink?sign=de9ac7376ca30c2da603d0c557f05a6f&appid=16073360&TSID=T10040899625&timestamp=1724141054
        url = f'https://music.91q.com/v1/song/tracklink?sign={sign}&{original_str}'
        header = {
            'Referer': 'https://music.91q.com/player',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        }
        response = requests.get(url, headers=header)
        if response.status_code != 200:
            print('Error, request failed, status code: ' + str(response.status_code))
            return
        else:
            #print(response.text)
            data = json.loads(response.text)
            if 'path' in data['data']:
                self.__doDown(data['data']['path'], sone_name)
            else:
                print('VIP song, not support yet')

    def __doDown(self, down_url: str, sone_name: str):
        header = {
            'Referer': 'https://music.91q.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        }
        response = requests.get(down_url, headers=header)
        if response.status_code != 200:
            print('Error, request failed, status code: ' + str(response.status_code))
            return
        else:
            with open(f'songs/{sone_name}.mp3', 'wb') as f:
                f.write(response.content)

if __name__ == '__main__':
    # 爬取电影信息
    # movie_crawler = MovieCrawler()
    # movie_crawler.crawler_and_write_excel()

    # 爬取音乐信息
    music_crawler = MusicCrawler()
    music_list = music_crawler.request_info('胡彦斌')

    for m in music_list:
        music_crawler.down_music(m.get_tsid(), m.song_name)
    print('Done')