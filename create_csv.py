import sys
import os.path
from PIL import Image

SIZE = (1280, 720)
IMAGE_EXT = '.png'
SEPARATOR = ";"


def resize_image(filepath):
    image = Image.open(filepath)
    new_image = image.resize(SIZE)
    dir_path = os.path.dirname(os.path.abspath(filepath))
    file_name = os.path.splitext(os.path.basename(filepath))[0]
    new_filepath = '%s/%s%s' % (dir_path, file_name, IMAGE_EXT)
    new_image.save(new_filepath)
    return new_filepath


def create_csv(base_path):
    label = 0
    images = []
    for dirname, dirnames, filenames in os.walk(base_path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for dirname2, sessionDirs, subjectFiles in os.walk(subject_path):
                for sessionDir in sessionDirs:
                    session_path = os.path.join(subject_path, sessionDir)
                    for filename in os.listdir(session_path):
                        abs_path = "%s/%s" % (session_path, filename)
                        filepath, file_extension = os.path.splitext(abs_path)
                        if file_extension == '.bmp':
                            abs_path = resize_image(abs_path)
                            images.append("%s%s%d" % (abs_path, SEPARATOR, label))
                            print("%s%s%d" % (abs_path, SEPARATOR, label))
            label += 1

    outfile = open("./faces.csv", "w")
    outfile.write("\n".join(images))
    outfile.close()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("usage: create_csv <base_path>")
        sys.exit(1)

    create_csv(sys.argv[1])

