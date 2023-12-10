import os
import whisper
from pytube import YouTube

link = 'https://www.youtube.com/watch?v=RTkM06CIMJs'
# link to the youtube video
title = 'test'
# name of transcript

path = '../outputs'
file_name = f'{title}.txt'

try:
    yt = YouTube(link)
except:
    print("Connection Error")

yt.streams.filter(file_extension='mp4')

stream = yt.streams.get_by_itag(139)
stream.download(f"{path}", f"{title}.mp4")
print('downloaded audio file')


print('transcribing...')
model = whisper.load_model("base")
result = model.transcribe(f"{path}/{title}.mp4", fp16=False)
# print(result['text'])
with open(f'{path}/{file_name}', 'w') as out:
    out.writelines(result['text'])
print('transcription saved')

os.remove(f"{path}/{title}.mp4")
print('deleted audio file')
