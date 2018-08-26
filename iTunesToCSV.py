#CODE CREDIT TO: http://www.robertprice.co.uk/robblog/python_xml_and_itunes-shtml/
#Title: Python, XML and iTunes
#Author: Robert Price
#Date: 2007

import xml.sax.handler

class ITunesHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.parsing_tag = False
        self.tag = ''
        self.value = ''
        self.tracks = []
        self.track = None

    def startElement(self, name, attributes):
        if name == 'key':
            self.parsing_tag = True

    def characters(self, data):
        if self.parsing_tag:
            self.tag = data
            self.value = ''
        else:
            # could be multiple lines, so append data.
            self.value = self.value + data

    def endElement(self,name):
        if name == 'key':
            self.parsing_tag = False
        else:
            if self.tag == 'Track ID':
            # start of a new track, so a new object
            # is needed.
                self.track = Track()
            elif self.tag == 'Name' and self.track:
                self.track.track = self.value
            elif self.tag == 'Artist' and self.track:
                self.track.artist = self.value
        # assume this is all the data we need
        # so append the track object to our list
        # and reset our track object to None.
        self.tracks.append(self.track)
        self.track = None

class Track:
    def __init__(self):
        self.track = ''
        self.artist = ''
        self.play_count = 0
        self.location = ''

    #def __str__(self):
    #    return "Track = %snArtist = %s" % (self.track,self.artist)

parser = xml.sax.make_parser()
handler = ITunesHandler()
parser.setContentHandler(handler)
parser.parse('D:\Documents and Settings\Windows User\Desktop\Purchased.xml')
for track in handler.tracks:
    print track
