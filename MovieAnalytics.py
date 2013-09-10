import httplib
import urllib2
import xml.etree.ElementTree as ET
import os
import sys

#Uncomment and give proper path for saving in a file.
#sys.stdout = open ('<Enter file path>', 'w');

def getDataFromIMDb(movie):
    file = urllib2.urlopen('http://mymovieapi.com/?title='+movie+'&type=xml');
    try:
        et = ET.fromstring(file.read())
    except:
        return
    file.close()
    errorTag = et.find('error')
    if errorTag is None:
        for item in et.findall('item'):
            titleTag = item.find('title')
            if titleTag is not None:
                title = item.find('title').text
            else:
                title = movie
            ratingTag = item.find('rating')
            if ratingTag is not None:
                rating = ratingTag.text
            else:
                rating = 'N/A'
            yearTag = item.find('year')
            if yearTag is not None:
                year = item.find('year').text
            else:
                year = 'N/A'
            print(title + '\t' + year + '\t' + rating)
            #print('[' + title + ',' + rating + '],')

def browseFilms(path):
    for file in os.listdir(path):
        if os.path.isdir(path+"\\"+file) == True:
            count = browseFilms(path+"\\"+file)
        elif file.endswith(".mkv") or file.endswith(".avi") or file.endswith(".mp4"):
            getDataFromIMDb(os.path.splitext(file)[0])

browseFilms('F:\IMDb TOP 250')
#For a folder
#browseFilms('<Enter path of movies folder')

#For individual movies
#getDataFromIMDb('American History X')
