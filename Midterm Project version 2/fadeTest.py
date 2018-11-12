# Test of fading method

def fade():
  picture = makePicture(pickAFile())
  
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
  show(picture)
  writePictureTo(picture, '/Users/craigcalvert/Desktop/output.png')