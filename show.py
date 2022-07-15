#AKSHAR PATEL
#!C:\Users\akshp\AppData\Local\Programs\Python\Python310\python.exe
import cgi,os
import time

# get the start time
st = time.time()
from zipfile import ZipFile

print('content-type:text/html\r\n\r\n')

form=cgi.FieldStorage()
quality_image=int(str(form.getvalue("quality")))
total_quality_image=100-quality_image
fle=form['filename']
# dow="dow.jpg"

fn=os.path.basename(fle.filename)
split_tup = os.path.splitext(fle.filename)

open("./tem/"+fn,"wb").write(fle.file.read())

import PIL
from PIL import Image  
store_original_img="./tem/"+fn
img1=PIL.Image.open("./tem/"+fn)
myheight,mywidth=img1.size

img1=img1.resize((myheight,mywidth),PIL.Image.ANTIALIAS)
if(split_tup[1]==".jpg"):
  x_img=fn.split(".jpg")
  dowimagename=x_img[0]+"_Compress.jpg"
  dowimage="./tem/"+x_img[0]+"_Compress.jpg"
  img1.save(dowimage,quality=total_quality_image,optimize=True)

elif(split_tup[1]==".png"):
  x_img=fn.split(".png")
  dowimagename=x_img[0]+"_Compress.png"
  dowimage="./tem/"+x_img[0]+"_Compress.png"
  img1.save(dowimage,quality=total_quality_image,optimize=True)

  img1.save(dowimage,quality=total_quality_image,optimize=True)

print('<html>')
print('<head><style>input[type=checkbox] {'+
        'display: none;'+
        '}'+

        'img {'+
        'transition: transform 0.25s ease;'+
        'cursor: zoom-in;'+
        '}'+

        'input[type=checkbox]:checked ~ label > img {'+
        'transform: scale(2);'+
        'cursor: zoom-out;'+
        '}</style></head>')
print('<body><center>')


original_size=os.path.getsize(store_original_img)
compress_size = os.path.getsize(dowimage)

zipObj = ZipFile('Compress.zip', 'w')
# Add multiple files to the zip
zipObj.write(store_original_img)
zipObj.write(dowimage)
# close the Zip File
zipObj.close()


print('<table>')
print('<tr>')
print('<th><h1>Original Image</h1></th>')
print('<th></th>')
print('<th><h1>Compress Image</h1></th>')
print('</tr>')
print('<tr>')
print('<td>')
print('<input type="checkbox" id="zoomCheck">')
print('<label for="zoomCheck">')
print('<img src=tem/%s width="500" height="600">'%fn)
print('<label>')
print('</td>')
print('<td><img src="./assets/arrow.png" width="200" height="200"></td>')
print("&nbsp")
print('<td>')
print('<input type="checkbox" id="zoomCheck1">')
print('<label for="zoomCheck1">')
print('<img src=%s width="500" height="600">'%dowimage)
print('<label>')
print('</td>')
print('</tr>')
print('<tr>')
print('<td style="text-align: center;vertical-align: middle">')
print("Image Name: "+fn)
print('</td>')
print('<td></td>')
print('<td style="text-align: center;vertical-align: middle">')
print("Compress Image Name: "+dowimagename)
print('</td>')
print('</tr>')
print('<tr>')
print('<td style="text-align: center;vertical-align: middle">')
print("Dimension: ",myheight,"*",mywidth)
print('</td>')
print('<td></td>')
print('<td style="text-align: center;vertical-align: middle">')
print("Dimension: ",myheight,"*",mywidth)
print('</td>')
print('</tr>')
print('<tr>')
print('<td style="text-align: center;vertical-align: middle">')
print("Original Image Size: ",+round(original_size/1024),"KB")
print('</td>')
print('<td></td>')
print('<td style="text-align: center;vertical-align: middle">')
print("Compressed Image Size: ",round(compress_size/1024),"KB")
print('</td>')
print('</tr>')

print('</table>')
print('<br>')
print('<a href="'+dowimage+'" download=%s>Download From Here</a>'%dowimagename)
print("<br>")
zip_name="Compress.zip"
print('<a href=%s>Download Zip File</a>'%zip_name)
et = time.time()

# get the execution time
elapsed_time = et - st
print('<br>')
print("Time to be taken for compression is:",round(elapsed_time,2),"second")
print('<form method="post" action="imagecompresser.html">')
print('<input type="submit" value="Compress New Image" />')
print('</form>')
print('</center></body></html>')

