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
  rootPath = r'H:\My Drive\Personal\school\CST205\nwtech.github.io\Module 2'
  redEyePath = os.path.join(rootPath,"redeye.jpg")
  redEyePic = makePicture(redEyePath)
  noRedEyePic = copyPic(redEyePic)
  show(redEyePic)
  removeRedEye(noRedEyePic)
  repaint(noRedEyePic)

      
