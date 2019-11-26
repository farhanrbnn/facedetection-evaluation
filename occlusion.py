import face_recognition
import cv2
import glob
import os
import argparse
import numpy as np


class ImageOcclusion:

	def __init__(self, dirname,
		           foldername, face_location,
		           level, image,
		           name):

		self.dirname = dirname
		self.foldername = foldername
		self.face_locations = []
		self.level = level
		self.image = image
		self.name = name

	#generate folder that doesn't exist
	def GenerateFolder(self):
		try:
			os.mkdir(self.foldername)
			print('Directory successfully created')

		except FileExistsError:
			print('Directory already exist')

	def GetFaceLocation(self):
		os.chdir(self.dirname)
		for file in glob.glob('*.jpg'):
			print('get face location: {}'.format(file))

			self.name = file.split('.')[0]

			self.image = face_recognition.load_image_file(file)
			face_location = face_recognition.face_locations(self.image, number_of_times_to_upsample = 0, model='cnn')
			print(face_location)

			self.face_locations.append(face_location)

	#generate bounding box from face location
	def GenerateBoundingBox(self):

		for location in self.face_locations:

			count = 0

			top, right, bottom, left = location[0]
			print('location:TOP{},RIGHT:{},LEFT:{},BOTTOM:{}'.format(top, right, bottom, left))

			width = right-left

			width_one = int(width*0.75) #for 25% occlusion
			width_two = int(width*0.5) #for 50% occlusion
			width_three = int(width*0.25) #for 75% occlusion

			if self.level == '100':
				cv2.rectangle(self.image, (left, top), (right, bottom), (0, 0, 0), cv2.FILLED)
				image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
				cv2.imwrite('./{}/result_100_{}.jpg'.format(self.level, count), image_rgb)

				count += 1

			if self.level == '75':
				cv2.rectangle(self.image, (left, top), (right - width_three, bottom), (0, 0, 0), cv2.FILLED)
				image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
				cv2.imwrite('./{}/result_75_{}.jpg'.format(self.level, count), image_rgb)

				count += 1

			if self.level == '50':
				cv2.rectangle(self.image, (left, top), (right - width_two, bottom), (0, 0, 0), cv2.FILLED)
				image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
				cv2.imwrite('./{}/result_50_{}.jpg'.format(self.level, count), image_rgb)

				count += 1

			if self.level == '25':
				cv2.rectangle(self.image, (left, top), (right - width_one, bottom), (0, 0, 0), cv2.FILLED)
				image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
				cv2.imwrite('./{}/result_25_{}.jpg'.format(self.level, count), image_rgb)

				count += 1

		#return self.image


#main function
def main(dirname, level):

	foldername = level
	face_locations = []
	name = []
	image = []

	occlusion = ImageOcclusion(dirname, foldername,
		                        face_locations, level,
		                        image, name)
	occlusion.GetFaceLocation()
	occlusion.GenerateBoundingBox()
	occlusion.GenerateFolder()



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='process images into occluded')
	parser.add_argument('dirname',help='input the directory')
	parser.add_argument('level',  help='level for occlusion', type=str)
	args = parser.parse_args()
	parser.add_argument
	main(args.dirname, args.level)