#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Credits to http://brunelvis.org/index.php/2013/04/29/itunes-music-to-data-via-python/

SRC = "C:/Users/theplaineric/Desktop/MusicRecommender/iTunes Music Library.xml"
TRACKS = "C:/Users/theplaineric/Desktop/MusicRecommender/LibraryTracks.csv"
TRACK_INFO = ["Track ID", "Name", "Artist", "Genre", "Total Time", "Location", "Play Count"]

from xml.dom import minidom
from music import *
import unicodecsv as csv

srcfile = open(SRC, 'r', encoding='utf-8')

dom = minidom.parse(srcfile)
remove_whitespace(dom)
srcfile.close()
main = dom.getElementsByTagName('plist')[0].childNodes[0]
tracks = getItems(main, 'Tracks')

# Write out the values to a csv file
c = csv.writer(open(TRACKS, "wb"), encoding='utf-8')
c.writerow(TRACK_INFO)
for i in tracks:
    row = map(lambda x: get_item(i, x), TRACK_INFO)
    c.writerow(row)