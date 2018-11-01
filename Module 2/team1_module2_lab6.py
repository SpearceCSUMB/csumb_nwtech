#Team 1: Northwestern Technology
#Brian Sheridan
#Craig Calvert
#Kevin Bentley
#Samuel Pearce

#Warm Up
def copyPic(pic):
  width = pic.getWidth()
  height = pic.getHeight()
  sourcePixels = getPixels(pic)
  newPic = makeEmptyPicture(width,height)
  for row in range(height):
    for col in range(width):
      sourcePixel = getPixel(pic,col,row)
      sourceColor = getColor(sourcePixel)
      destPixel = getPixel(newPic,col,row)
      setColor(destPixel,sourceColor)
  return newPic

#red eye red color: 223,68,84
def removeRedEye(pic):
  redEyeColor = makeColor(223,68,84)
  pixels = getPixels(pic)
  for p in pixels:
    pixelColor = getColor(p)
    dist = distance(pixelColor,redEyeColor)
    if(dist < 75):
      #desaturate the color if it's too close to redeye
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      luminance = r*0.299 + g*0.587 + b*0.114
      newColor = makeColor(luminance,luminance,luminance)
      setColor(p,newColor)

def testRedEye():
  # Set this path to where your module 2 github repository is
  rootPath = r'C:\dev\cs205\csumb_nwtech\Module 2'
  redEyePath = os.path.join(rootPath,"redeye.jpg")
  redEyePic = makePicture(redEyePath)
  noRedEyePic = copyPic(redEyePic)
  show(redEyePic)
  removeRedEye(noRedEyePic)
  repaint(noRedEyePic)

#Problem 1:
def makeSepia(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    luminance = r*0.299 + g*0.587 + b*0.114
    redMult = 1
    blueMult = 1
    blue
    if(r < 63):
      redMult = 1.1
      blueMult = 0.9
    elif(62 < r and r < 192):
      redMult = 1.15
      blueMult = 0.85
    else:
      redMult = 1.08
      blueMult = 0.93    
    r = redMult * luminance
    r = min(r,255)
    b = blueMult * luminance
    setRed(p,r)
    setGreen(p,luminance)
    setBlue(p,b)
  return pic


#Problem 3

def chromakey(foregroundPic,backgroundPic):
  greenScreenColor = makeColor(50,150,50)
  foregroundPixels = getPixels(foregroundPic)
  for row in range(foregroundPic.getHeight()):
      for col in range(foregroundPic.getWidth()):
        foregroundPixel = getPixel(foregroundPic,col,row)
        pixelColor = getColor(foregroundPixel)
        dist = distance(pixelColor,greenScreenColor)
        if(dist < 75):
          backgroundPixel = getPixel(backgroundPic,col,row)
          backgroundColor = getColor(backgroundPixel)
          setColor(foregroundPixel,backgroundColor)
  return foregroundPic        


def testProblem1():
  rootPath = r'C:\dev\cs205\csumb_nwtech\Module 2'
  originalPath = os.path.join(rootPath,"1.jpg")
  originalPic = makePicture(originalPath)
  originalPic = makeSepia(originalPic)
  show(originalPic)

def testProblem3():
  rootPath = r'C:\dev\cs205\csumb_nwtech\Module 2'
  foregroundPath = os.path.join(rootPath,"henry_greenscreen.jpg")
  backgroundPath = os.path.join(rootPath,"outdoors.jpg")
  backgroundPic = makePicture(backgroundPath)
  foregroundPic = makePicture(foregroundPath)
  foregroundPic = chromakey(foregroundPic,backgroundPic)
  show(foregroundPic)  
  