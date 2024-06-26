import os, fnmatch
import shutil
from config import PATH_IMG, FILE
from PIL import Image


def find_files(directory, pattern):
    """
    Генератор для сбора всех изображений из всех каталогов
    где directory-Путь до директории с изображениями
    pattern-формат который вы хотите собирать
    Лучше использовать формат '*.j*' где будет собираться все форматы начиная с буквы j
    """
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)

                yield filename


for filename in find_files(PATH_IMG, '*.j*'):
    shutil.copy(filename, FILE)


def stich_tile(path_to_file, xx, yy):
    """
    Функция записи всех изхображений в один файл .tiff
    При вызове функции необходимо указать:
    path_to_file - путь до папки где лежать все папки, по умолчанию после скрипта
    сохраняются все изображения в папке 'image'
    хх-количесвто колонок которые мы хотим получить
    уу-количесвто фотографий в калонке
    """
    images = []
    for i in os.listdir(path_to_file):
        images.append(i)

    if len(images) >= xx * yy:
        pass

    else:
        raise ValueError('недостаточно изображений в пути_к_файлу !')

    sq_x = xx
    sq_y = yy
    img_x = (Image.open(path_to_file + '/' + images[0]).size[0])
    img_y = (Image.open(path_to_file + '/' + images[0]).size[1])
    img_mode = (Image.open(path_to_file + '/' + images[0]).mode)

    new_image = Image.new(img_mode, (img_x * sq_x, img_y * sq_y))

    x = 0
    y = 0
    cnt = 0
    for i in images:
        with Image.open(path_to_file + '/' + i) as img:
            new_image.paste(img, (x, y))
            cnt += 1
            x += img_x
            if cnt == sq_x:
                x = 0
                y += img_y
                cnt = 0
            else:
                pass

    return new_image.save('Result.tiff', format='tiff')


if __name__ == '__main__':
    find_files(PATH_IMG, '*/.j')
    stich_tile(FILE, 3, 2)

