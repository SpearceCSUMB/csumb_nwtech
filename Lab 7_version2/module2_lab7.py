#CST205
#Module 2: Lab 7

#Warm Up

def snowman(pic):
  #Snowman's body
  addOvalFilled(pic, 184, 213, 60, 60, white)
  addOvalFilled(pic, 162, 273, 104, 104, white)
  addRectFilled(pic, 196, 270, 36, 7, green)
  #Snowman's left arm
  addLine(pic, 143, 264, 175, 291, black)
  addLine(pic, 149, 260, 151, 271, black)
  addLine(pic, 140, 268, 148, 269, black)
  #Snowman's hat
  addRectFilled(pic, 191, 198, 46, 25, black)
  addRectFilled(pic, 177, 223, 71, 3, black)
  addRectFilled(pic, 191, 218, 46, 5, red)
  #Snowman's face
  addOvalFilled(pic, 202, 237, 6, 6, black)
  addOvalFilled(pic, 220, 237, 6, 6, black)
  addOvalFilled(pic, 211, 243, 6, 6, orange)
  addArc(pic, 201, 242, 25, 19, 180, 180, black)
  #Snowman's buttons
  addOvalFilled(pic, 210, 293, 8, 8, black)
  addOvalFilled(pic, 210, 311, 8, 8, black)
  addOvalFilled(pic, 210, 329, 8, 8, black)
  #Sign
  addRectFilled(pic, 286,239, 100, 70, yellow)
  addRect(pic, 286,239, 100, 70, black)
  #Sign text
  s = makeStyle(sansSerif, bold, 15)
  addTextWithStyle(pic, 295, 260, "North Pole", s, black)
  addTextWithStyle(pic, 330, 280, "or", s, black)
  addTextWithStyle(pic, 317, 300, "BUST", s, red) 
  #Snowman's right arm
  addLine(pic, 254, 292, 286, 284, black)
  addLine(pic, 285, 285, 293, 278, black)
  addLine(pic, 285, 285, 293, 288, black)
  return pic

#Problem 1

def testWarmup():
  rootPath = r'/Users/craigcalvert/Documents/GitHub/csumb_cst205/Lab 7/warmup_pictures'
  originalPath = os.path.join(rootPath, "desert.jpg")
  originalPic = makePicture(originalPath)
  originalPic = snowman(originalPic)
  writePictureTo(originalPic, '/Users/craigcalvert/Documents/GitHub/csumb_cst205/Lab 7/warmup_pictures/snowman_output.jpg')
  show(originalPic)
