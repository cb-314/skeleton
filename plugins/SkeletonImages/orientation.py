from pelican import signals
from PIL import Image
import logging
import os

logging.Logger(__name__)

def isclose(a, b, rtol=1e-2):
  db = abs(b)*float(rtol)
  return a > b-db and a < b+db

def rewrite_images(p):
  for dirName, subdirList, fileList in os.walk(p.output_path):
    for fileName in fileList:
      path = os.path.join(dirName, fileName)
      with open(path, "r+") as infile:
        base_path = path[:path.rfind("/")+1]
        content = infile.readlines()
        images = {}
        for i, line in enumerate(content):
          if "<img" in line:
            img_start = line.find("<img")
            if img_start >= 0:
              source_start = line.find("src=", img_start)
              source_start = line.find("\"", source_start) + 1
              source_end = line.find("\"", source_start)
              with Image.open(base_path+line[source_start:source_end]) as image:
                images[i] = image.size
        for i in images.keys():
          line = content[i]
          img_start = line.find("<img")
          w = images[i][0]
          h = images[i][1]
          if w > h:
            content[i] = line[:img_start+5] + "class=\"landscape\" " + line[img_start+5:]
          elif isclose(w, h):
            content[i] = line[:img_start+5] + "class=\"square\" " + line[img_start+5:]
          else:
            if isclose(h, 1.5*w):
              content[i] = line[:img_start+5] + "class=\"portrait32\" " + line[img_start+5:]
            elif isclose(h, 4.0/3.0*w):
              content[i] = line[:img_start+5] + "class=\"portrait43\" " + line[img_start+5:]
            elif isclose(h, 5.0/4.0*w):
              content[i] = line[:img_start+5] + "class=\"portrait54\" " + line[img_start+5:]
            else:
              content[i] = line[:img_start+5] + "class=\"portrait\" " + line[img_start+5:]
        infile.seek(0)
        infile.truncate()
        infile.writelines(content)

def register():
  signals.finalized.connect(rewrite_images)
