from moviepy.editor import *
from moviepy.video.fx import *
import os
import time



def mergeVideos(inputPath, outputPath):
    L = []
    for root, dirs, files in os.walk(inputPath):
        for file in files:
            if os.path.splitext(file)[1] == '.mp4':
                filePath = os.path.join(root, file)
                video = VideoFileClip(filePath)
                L.append(video)

    timestr = time.strftime("%Y%m%d%H")
    final_clip = concatenate_videoclips(L, method="compose")
    final_clip.to_videofile(outputPath+timestr+".mp4",fps=24)

# inputPath = "D:/08 Code/instaFunctionGraph/downloadSavedVideo/：saved"
# outputPath = "D:/08 Code/instaFunctionGraph/downloadSavedVideo/outputs/"
# mergeVideos(inputPath, outputPath)