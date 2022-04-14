import img2pdf
import PIL.Image
import os
image = PIL.Image.open("img.jpg")
pdf_bytes = img2pdf.convert(image.filename)
file = open("file.pdf", "wb")
file.write("file.pdf")
image.close()
file.close()
