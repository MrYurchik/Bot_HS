from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
# from scrape import z
# response1 = requests.get('https://www.yaytears.com/static/media/NEW1_003_2.e9773a36.png')
# response2 = requests.get('https://www.yaytears.com/static/media/CS2_072.d649e9a1.png')
# image1 = Image.open(BytesIO(response1.content))
# image2 = Image.open(BytesIO(response2.content))
# draw = ImageDraw.Draw(image1)
# draw2 = ImageDraw.Draw(image2)

def merge_images(image1, image2):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = max(width1, width2)
    result_height = height1 + height2

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(0, height1))
    return result


#z = ['https://www.yaytears.com/static/media/NEW1_003_2.e9773a36.png', 'https://www.yaytears.com/static/media/EX1_302_2.b39744a8.png', 'https://www.yaytears.com/static/media/ULD_717_2.95ae45b4.png', 'https://www.yaytears.com/static/media/EX1_066_2.31fb013c.png', 'https://www.yaytears.com/static/media/DRG_205_2.1b4bab45.png', 'https://www.yaytears.com/static/media/ULD_003.89fac546.png', 'https://www.yaytears.com/static/media/DRG_071_2.509e05f3.png', 'https://www.yaytears.com/static/media/DRG_204_2.f6aa2334.png', 'https://www.yaytears.com/static/media/DRG_202_2.6aed252f.png', 'https://www.yaytears.com/static/media/DRG_050_2.cff9424a.png', 'https://www.yaytears.com/static/media/DRG_250.ad5ec2b0.png', 'https://www.yaytears.com/static/media/DRG_203_2.8f502c14.png', 'https://www.yaytears.com/static/media/DRG_201_2.8b4fcb1f.png', 'https://www.yaytears.com/static/media/DRG_242_2.3edc38a9.png', 'https://www.yaytears.com/static/media/DRG_099.bc136089.png', 'https://www.yaytears.com/static/media/DRG_600.6db4cd70.png', 'https://www.yaytears.com/static/media/EX1_561.2546d585.png', 'https://www.yaytears.com/static/media/DRG_089.de7b7581.png']


def merge_im(z, name):
    for i in range(len(z)):
        z[i] = requests.get(z[i])
        z[i] = Image.open(BytesIO(z[i].content))
        # z[i] = ImageDraw.Draw(z[i])

    im = merge_images(z[0], z[1])
    for i in range(2, len(z)):
        im = merge_images(im, z[i])
    im = im.save("images/{}.jpg".format(name))
    return im




# im.show()