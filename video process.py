import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
from PIL import Image, ImageDraw, ImageStat
import imageio
import threading

video_list = '/home/tony/Downloads/test_list.txt'

# read list .txt file
def ReadVideoList(list_path):
    with open(video_list) as file:
        lines = file.readlines()

    return lines

# strip "\n" at end of line, and read video
def LoadVideo(video_path):   
    video_path_good = video_path.rstrip('\n')

    reader = imageio.get_reader(video_path_good)

    return reader

def VideoProcessing(reader):
    # get frame data
    frame = reader.get_next_data()

    # transfer to PIL format
    im_rgb = Image.fromarray(frame).resize((425, 240))

    # convert to grayscale
    im_gray = im_rgb.convert("L")

    # x increase to right, y increase to bottom
    # set rectangle and crop
    (left, upper, right, lower) = (20, 20, 100, 100)
    im_crop = im_gray.crop((left, upper, right, lower))
    meanval = ImageStat.Stat(im_crop).mean

    # draw rectangle
    draw_im = ImageDraw.Draw(im_gray)
    draw_im.rectangle([left, upper, right, lower], None, "red") 
    # PIL image show 
    im_gray.show()   

def main():
    lines = ReadVideoList(video_list)
    for line in lines:
        reader = LoadVideo(line)
    
        VideoProcessing(reader)
    
#  imageio image output
#imageio.imwrite('/home/tony/Downloads/test_frame.jpg', frame)


if __name__ == '__main__':
    main()
