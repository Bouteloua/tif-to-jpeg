import glob, os
try:
	import PIL
	import PIL.Image, PIL.ImageFile
except:
	raise Exception('Install PIL from http://www.pythonware.com/products/pil/')
from exceptions import IOError

def main():
	createFolders()
	tifImages = [x[5:]for x in glob.glob('tiff/*.tif')]

	for tifImage in tifImages:
		try:
			img = PIL.Image.open('tiff/' + tifImage)
			jpegResize(img, tifImage)
			jpegThumbnailResize(img, tifImage)
		except:
			pass

def saveImage(img, destination, quality):
	try:
	    img.save(destination, "JPEG", quality=quality, optimize=True, progressive=True)

	except IOError:
	    PIL.ImageFile.MAXBLOCK = img.size[0] * img.size[1]
	    img.save(destination, "JPEG", quality=quality, optimize=True, progressive=True)

def jpegResize(img, tifImage):
	quality = 95
	img.MAXBLOCK = 2**10
	destination = "jpeg/" + tifImage[:-4] + ".jpeg"
	widthImage, heightImage =  img.size[0] / 2, img.size[1] / 2
	newImageSize = img.resize((widthImage, heightImage))
	saveImage(newImageSize, destination, quality)

def jpegThumbnailResize(img, tifImage):
	quality = 70
	img.MAXBLOCK = 2**50
	destination = "thumbnail_jpeg/" + tifImage[:-4] + ".jpeg"
	widthImage, heightImage =  img.size[0] / 10, img.size[1] / 10
	newImageSize = img.resize((widthImage, heightImage))
	saveImage(newImageSize, destination, quality)

def createFolders():
	requiredFolders = ('jpeg', 'thumbnail_jpeg', 'tiff')
	for folders in requiredFolders:
	#Check if required folders have been created
		try:
			os.stat(folders)
		except:
			os.mkdir(folders)

if __name__ == '__main__':
  main()