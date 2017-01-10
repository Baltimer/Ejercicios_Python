# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
ns = {
	"standard" : "http://xspf.org/ns/0/",
	"vlc" : "http://characters.example.com"}

#def generarMenu(playlist):
tree = ET.parse('playList.xml')
root = tree.getroot()
	#for track in root.find('standard:trackList', ns):
	#	playlist[track.find('standard:title', ns).text] = track.find('standard:location', ns).text
	#return playlist
	# Utilizando 
playList = {track.find('standard:title', ns).text : track.find('standard:location', ns).text for track in root.find('standard:trackList', ns)}
if __name__ == "__main__":    
	print(playList)    
	#print (generarMenu(playList))