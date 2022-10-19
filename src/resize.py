from PIL import Image
import os

def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print('The resized image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    resized_image.save(output_image_path)

path = "src\\art\\assets"
folders = ['Blue', 'Camo', 'Desert', 'Purple', 'Red'] 
foldersDeep = ['Bodies', 'Towers', 'Weapons']
paths = []
files = []

for folder in folders:
    for folder1 in foldersDeep:
        paths.append(path + "\\" + folder + "\\" + folder1)

for path in paths:
    files.append(os.listdir(path))

for i, l in enumerate(files):
    for file in l:
        split = os.path.splitext(file)
        if '.png' in file:
            if Image.open(paths[i] + '\\' + file).size == (128,128) and not os.path.exists(paths[i] + '\\' + split[0] + "_32x32" + split[1]):
                resize_image(paths[i] + '\\' + file, paths[i] + '\\' + split[0] + "_32x32" + split[1], (32,32))
            if Image.open(paths[i] + '\\' + file).size == (256,128) and not os.path.exists(paths[i] + '\\' + split[0] + "_64x32" + split[1]):
                resize_image(paths[i] + '\\' + file, paths[i] + '\\' + split[0] + "_64x32" + split[1], (64,32))


 