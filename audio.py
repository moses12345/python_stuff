from pydub import AudioSegment
from pydub.playback import play

files_path = AudioSegment.from_file(file="C:\Users\ahron\Documents\pyhon_stuff\pokemon_audio.mp3",format="mp3")
play(files_path)

# file_name = 'pokemon_audio'

# startMin = 9
# startSec = 50

# endMin = 13
# endSec = 30

# # Time to miliseconds
# startTime = startMin*60*1000+startSec*1000
# endTime = endMin*60*1000+endSec*1000

# # Opening file and extracting segment
# song = AudioSegment.from_mp3( files_path+file_name+'.mp3' )
# extract = song[startTime:endTime]

# # Saving
# extract.export( file_name+'-extract.mp3', format="mp3")