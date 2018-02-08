#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:37:44 2018
create gifs using imageio lib in Python
created by John Peirce
"""
import imageio
import glob

# creates a list of file names searching this folder
filenames = glob.glob("/Users/ilkay.isik/Desktop/gif_test/*.png")
filenames.sort()  # if you want them in alphabetical order then best to do this
outputName = "/Users/ilkay.isik/Desktop/gif_test/myMRI_Animation.gif"
secsPerFrame = 1/5.0  # you can provide a list instead, for 1 val per frame
reps = 1  # 1 rep (0 for infinite loop, or some other number for fixed N reps)

outputImages = []
for thisFilename in filenames:
    print(thisFilename)
    frame = imageio.imread(thisFilename)
    outputImages.append(frame)

imageio.mimsave(outputName, outputImages, loop=reps, duration=secsPerFrame)
