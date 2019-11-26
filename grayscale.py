import cv2
import os
import glob
import argparse


class GrayscaleImage:

    def __init__(self,dirname,
                 foldername):

        self.dirname = dirname
        self.foldername = foldername

    #generate new folder
    def generate_folder(self):

        try:
            os.mkdir(self.foldername)
            print('Directory successfully created')

        except FileExistsError:
            print('Directory already exists')

    #load image, processing image from RGB to GRAY and save to folder
    def processing_image(self):

        os.chdir(self.dirname)

        for file in glob.glob('*.jpg'):

            print('{} has been grayscalled'.format(file))

            img = cv2.imread(file)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            name = file.split('.')[0]
            cv2.imwrite('{}/gray_{}.jpg'.format(self.foldername, name), img_gray)


#main program
def main(dirname):

    foldername = 'gray'

    grayscale = GrayscaleImage(dirname, foldername)
    grayscale.processing_image()
    grayscale.generate_folder()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='grayscalling image')
    parser.add_argument('dirname', help='input directory')
    args = parser.parse_args()
    main(args.dirname)





