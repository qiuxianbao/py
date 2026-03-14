# Pillow 是 Python 的图像处理库，它是 PIL(Python Imaging Library) 的分支和继承者
import random
from pathlib import Path
from PIL import Image, ImageFilter, ImageFont, ImageDraw

current_dir = Path(__file__).parent


def test_thumbnail():
    # 打开一个jpg图像文件，注意是当前路径:
    im = Image.open(current_dir.joinpath('google.png'))
    # 获得图像尺寸:
    w, h = im.size
    print('Original image size: %sx%s' % (w, h))

    # 缩放到50%:
    im.thumbnail((w // 2, h // 2))
    print('Resize image to: %sx%s' % (w // 2, h // 2))
    # 把缩放后的图像用jpeg格式保存
    im.save(current_dir.joinpath('thumbnail.jpg'), 'jpeg')


def test_filter():
    im = Image.open(current_dir.joinpath('google.png'))
    im2 = im.filter(ImageFilter.BLUR)
    im2.save(current_dir.joinpath('blur.jpg'), 'jpeg')


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255),
            random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127),
            random.randint(32, 127))


def test_draw():

    # 240 x 60:
    width = 60 * 4
    height = 60
    # 创建一张图片
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # 创建Font对象:
    font = ImageFont.truetype(current_dir.joinpath('arial.ttf'), 36)
    # 创建Draw对象
    draw = ImageDraw.Draw(image)

    # 填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    # 输出文字
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save(current_dir.joinpath('code.jpg') , 'jpeg')



def _main():
    # test_thumbnail()
    # test_filter()
    test_draw()


if __name__ == '__main__':
    _main()
