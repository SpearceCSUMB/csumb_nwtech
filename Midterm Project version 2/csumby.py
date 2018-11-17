# CST205
# Midterm Project
# Craig Calvert
#

# Greenscreen method
def chromakey(foregroundPic,backgroundPic):
  greenScreenColor = makeColor(0,255,0)
  foregroundPixels = getPixels(foregroundPic)
  for row in range(foregroundPic.getHeight()):
      for col in range(foregroundPic.getWidth()):
        foregroundPixel = getPixel(foregroundPic,col,row)
        pixelColor = getColor(foregroundPixel)
        dist = distance(pixelColor,greenScreenColor)
        if(dist < 89):
          backgroundPixel = getPixel(backgroundPic,col,row)
          backgroundColor = getColor(backgroundPixel)
          setColor(foregroundPixel,backgroundColor)
  return foregroundPic
  
def fade(picture):
  for x in range(0, getWidth(picture)):
    for y in range(0, getHeight(picture)):
      pixel = getPixel(picture, x, y)
      a = getRed(pixel)
      b = a * 0.37 + 98
      setRed(pixel, b)
      a = getGreen(pixel)
      b = a * 0.37 + 98
      setGreen(pixel, b)
      a = getBlue(pixel)
      b = a * 0.37 + 98
      setBlue(pixel, b) 
  return(picture)

def csumby(picture):
  picWidth = getWidth(picture)
  picHeight = getHeight(picture)
  csumbBlue = makeColor(0,42,78)
  
  # Check if picture being entered is a standard Instagram size
  if (picWidth == 1080 and picHeight == 566 or
    picHeight == 1080 or picHeight == 1350):
    pass
  else:
    print('Picture is the incorrect size. All pictures need to be:\n1080 x 566, 1080 x 1080, or 1080 x 1350.')
  # If picture is correct size call method to face picture
  fade(picture)
  # Picture border (top, bottom, left, right)
  addRectFilled(picture, 0, 0, picWidth, 15, csumbBlue)
  addRectFilled(picture, 0, picHeight - 15, picWidth, 15, csumbBlue)
  addRectFilled(picture, 0, 15, 15, picHeight - 30, csumbBlue)
  addRectFilled(picture, picWidth - 15, 15, 15, picHeight - 30, csumbBlue)
  # Select logo
  if picHeight == 566:
    logo = makePicture(pickAFile())
  elif picHeight == 1080:
    logo = makePicture(pickAFile())
  else:
    logo = makePicture(pickAFile())
  picture = chromakey(logo, picture)
  show(picture)
  return(picture)
  
# Test methods

def csumbyTest():
  pic = makePicture(pickAFile())
  csumby(pic)
  show(pic)
  
def getPixelColor():
  pic = makePicture(pickAFile())
  test = getPixel(pic, 0, 0)
  print(test)
