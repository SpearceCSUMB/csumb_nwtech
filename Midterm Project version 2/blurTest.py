# Test method to blur a picture
def blur():
  picture = makePicture(pickAFile())
  width = getWidth(picture)
  height = getHeight(picture)
  
  for x in range(1, width - 1):
    for y in range(1, height - 1):
      pixel = getPixel(picture, x, y)
      right = getPixel(picture, x + 1, y)
      left = getPixel(picture, x - 1, y)
      topLeft = getPixel(picture, x - 1, y - 1)
      top = getPixel(picture, x, y - 1)
      topRight = getPixel(picture, x + 1, y - 1)
      bottomLeft = getPixel(picture, x - 1, y + 1)
      bottom = getPixel(picture, x, y + 1)
      bottomRight = getPixel(picture, x + 1, y + 1)
      
      colorAverage = lambda function: sum(map(function, [right, left, topLeft, top, topRight, bottomLeft, bottom, bottomRight])) / 8
      
      redAverage = colorAverage(getRed)
      greenAverage = colorAverage(getGreen)
      blueAverage = colorAverage(getBlue)
      
      blurColor = makeColor(redAverage, greenAverage, blueAverage)
      setColor(pixel, blurColor)
      
  show(picture)
