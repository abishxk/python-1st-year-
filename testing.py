from moviepy.editor import *
import pygame
def launch(movie):
    pygame.display.set_caption('Hello World!')
    clip = VideoFileClip(movie)
    clip.preview()
    pygame.quit()
launch("Red Notice (2021) 1080p NF WEB-DL x264 (DD+ 5.1 - 192Kbps) .mkv")
