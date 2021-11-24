import os
import subprocess


def compressVideos(filePath, path):
    extention = os.path.splitext(filePath)[1]
    fileName = filePath.split('/')[-1]
    if extention == '.mp4' or extention == '.avi' or extention == '.mkv' or extention == '.mpg' or extention == '.mpeg':
        if not os.path.exists(f'{path}/compressed/'):
            os.makedirs(f'{path}/compressed/')
        media_in = path + fileName
        media_out = path + '/compressed/'+ fileName
        subprocess.run('ffmpeg -i '+media_in.replace(" ", "\\ ") +
                       " -vcodec libx264 -crf 22 " + media_out.replace(" ", "\\ "), shell=True)


