# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:43:06 2022

@author: Benjamin
"""
from __future__ import unicode_literals
from pytube import YouTube
import os
import sys
def download_link(link, directory):
    yt = YouTube(link)
    #yt.register_on_progress_callback(progress_function)
    video = yt.streams.filter(only_audio=True).first().download(directory)
    base, ext = os.path.splitext(video)
    new_file = base + '.mp3'
    os.rename(video, new_file)
    print(video)

    