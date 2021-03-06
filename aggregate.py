from bs4 import BeautifulSoup
import re
import unicodedata
import requests
url = "http://www.basketball-reference.com/players/a/armstda01.html"
soup2 = BeautifulSoup(requests.get(url).text)
name = soup2.find("h1")
name = unicode(name)
name = name[4:]
name = name[:-5]
height = soup2.findAll("p")[3]
Height = unicode(height)
Weight = Height
m = re.search('Height:(.+?)Weight:', Height)
if m:
    Height = m.group(1)
m = re.search('</span>(.+?)<span', Height)
if m:
    Height = m.group(1)

#players with pronounciations of their names
#require a sepcial case
if(len(Height)>8):
    height = soup2.findAll("p")[4]
    Height = unicode(height)
    Weight = Height
    m = re.search('Height:(.+?)Weight:', Height)
    if m:
        Height = m.group(1)
    m = re.search('</span>(.+?)<span', Height)
    Height = Height[:-24]
    Height = Height[7:]
#find the player's weight
m = re.search('Weight:(.+?)Age:', Weight)
if m:
    Weight = m.group(1)
m = re.search('Weight:</span> (.+?) lbs', Weight)
if m:
    Weight = m.group(1)
Height = Height[:-3]
Height = Height[1:]
if (len(Height) == 4):
    Feet = Height [:-3]
    Inches = Height [2:]
else:
    Feet = Height [:-2]
    Inches = Height [2:]
Total = int(Feet)*12 + int(Inches)
print "%s of Height %d Inches and Weights %d lbs" % (name, Total, int(Weight))