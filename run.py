#!/usr/bin/python3
import os, sys, time, subprocess
from pytube import Playlist, YouTube, exceptions
from tqdm import tqdm

class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def verifyURL(url):
    return True if "playlist" in url else False

def getPlayList(url):
    pList = Playlist(url)
    return pList

def showContents(list):
    for i in tqdm(range(len(list))):
        tqdm.write('[' + str(i+1) + '] ' + list[i])
        time.sleep(0.001)

def add_directory(path):
    try: 
        if os.path.isdir(path):
            return
        else:
            os.mkdir(path)
    except OSError:
        print(f"{b.WARNING}Creation of directory '{path}' failed{b.ENDC}")
    else:
        print(f"'{path}' directory successfully created")

def dlPl(list, di, _res):
    print('\n\n')
    add_directory(di)
    for url in tqdm(range(len(list))):
        try:
            p = YouTube(list[url])
        except:
            tqdm.write(f'{b.WARNING}[{url+1}]\t{p.title} is unavaialable, skipping.{b.ENDC}')
        else:  
            if not os.path.exists(os.getcwd()+"/"+di+"/"+p.title+'.mp4'):
                tqdm.write(f'{b.OKCYAN}[{url+1}]\tDownloading {p.title} ...{b.ENDC}')
                p.streams.filter(res=str(_res)+'p').first().download(os.getcwd()+"/"+di)
            else:
                tqdm.write(f'[{url+1}] {p.title} already exist, skipping')
                continue
    print('Download Complete!')


if __name__ == '__main__':
    
    URL = str(input('Target URL : '))
    _res = int(input('Resolution : '))
    if _res not in [144, 240, 360, 720, 1080, 1440, 2160]:
        print(f'{b.WARNING}Not valid Resolution{b.ENDC}')
        exit()

    if verifyURL(URL):
        showContents(getPlayList(URL))
        _dir = str(input('Directory Name : '))
        dlPl(getPlayList(URL), _dir, _res)
    else:
        yt = YouTube(URL)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()    
