#This code is meant to rename many files at once by removing keywords.
#For example, the file named "Song Title - Song Artist OFFICIAL AUDIO.mp3" can be renamed to "Song Title.mp3"
# This code can probably can be optimized, but the main purpose of this program is to explain what is going on and what to change for those who do not know much about python.
# github.com/jmahir408
import os

#PATH: File path to the folder that contains items to be renamed. 
#If there are multiple paths separate them by commas, with each path in it's own quotation marks.
PATH = ["/Users/firstname/Desktop/items"]
paths = len(PATH)
j=0
while j < paths:
 count = os.listdir(PATH[j])

#Input keywords to remove in their own quotation marks separated by commas (an array). Be sure to include a keyword of the file extension if it is included in your items to rename (such as .mp3). We will add this back later
 keywords = ["ArtistOne",
            "(320 kbps)",
            '.mp3',
            'ArtistOne',
            'ArtistThree',
            'Official Audio',
            'ArtistTwo'
            ]
 lengths = len(keywords)
 for file in count:
   text = file
   i=0
   while i < lengths:
     text = text.replace(keywords[i],"")
     i = i+1
   oldName = PATH[j] + file
   text = text.strip()
#IMPORTANT: Replace .mp3 with the file extension that was originally removed (if desired)
   newName = PATH[j] + text + '.mp3'
   os.replace(oldName,newName)
  
j=j+1