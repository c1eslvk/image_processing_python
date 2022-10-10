from PIL import Image
import numpy as np


# 1st exercise
def get_colors(image):
    im = image
    rgb = im.load()
    return rgb


# 2nd exercise
def single_threshold_bw(im, rgb):
    width, height = im.size
    threshold = 255 / 2
    for x in range(width):
        for y in range(height):
            color = (rgb[x, y][0] + rgb[x, y][1] + rgb[x, y][2]) / 3
            if color > threshold:
                rgb[x, y] = (255, 255, 255)
            else:
                rgb[x, y] = (0, 0, 0)

    im.save("yoda_s_thresh.jpeg")


def double_threshold_bw(im, rgb):
    width, height = im.size
    lower_threshold = 100
    upper_threshold = 200
    for x in range(width):
        for y in range(height):
            color = (rgb[x, y][0] + rgb[x, y][1] + rgb[x, y][2]) / 3
            if lower_threshold < color < upper_threshold:
                rgb[x, y] = (255, 255, 255)
            else:
                rgb[x, y] = (0, 0, 0)

    im.save("yoda_d_thresh.jpeg")


# 3rd exercise
def enhance_contrast(im):
    rgb = get_colors(im)

    all_pixels = []
    cdf_sum = 0
    new_values = []

    for row in range(0, im.size[0]):
        for column in range(0, im.size[1]):
            pix_value = int(((rgb[row, column])[0] + (rgb[row, column])[1] + (rgb[row, column])[2]) / 3)
            rgb[row, column] = (pix_value, pix_value, pix_value)
    im.save('yoda_grey.jpg')

    grey = im.load()

    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            sum = ((grey[x, y])[0] + (grey[x, y])[1] + (grey[x, y])[2]) / 3
            sum = int(round(sum))
            all_pixels.append(sum)

    for i in range(0, 256):
        cdf_sum += all_pixels.count(i)
        new_values.append(round((cdf_sum - 1) * 255 / (im.size[0] * im.size[1] - 1)))

    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            sum = ((grey[x, y])[0] + (grey[x, y])[1] + (grey[x, y])[2]) / 3
            sum = int(round(sum))
            grey[x, y] = (new_values[sum], new_values[sum], new_values[sum])
    im.save("yoda_grey_enhanced.jpeg")


# 4th exercise
def mean_filter(im):
    rgb = im.load()

    pixels = np.empty((im.size[0], im.size[1]))

    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            pix_value = int(((rgb[x, y])[0] + (rgb[x, y])[1] + (rgb[x, y])[2]) / 3)
            rgb[x, y] = (pix_value, pix_value, pix_value)
    im.save('road_grey.jpg')

    grey = im.load()

    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            sum = ((grey[x, y])[0] + (grey[x, y])[1] + (grey[x, y])[2]) / 3
            sum = int(round(sum))
            pixels[x, y] = sum
    summed_area_table = pixels.cumsum(axis=0).cumsum(axis=1)

    for x in range(35, im.size[0] - 35):
        for y in range(35, im.size[1] - 35):
            cell_value = round((summed_area_table[35 + x][35 + y] - summed_area_table[x - 35][35 + y] -
                                summed_area_table[35 + x][y - 35] + summed_area_table[x - 35][y - 35]) / (71 * 71))
            grey[x, y] = (cell_value, cell_value, cell_value)

    im.save("road_filter.jpg")


def main():
    yoda = Image.open("yoda.jpeg")
    road = Image.open("road.jpg")

    # 2nd exercise
    # single_threshold_bw(yoda, get_colors(yoda))
    # double_threshold_bw(yoda, get_colors(yoda))

    # 3rd exercise
    # enhance_contrast(yoda)

    # 4th exercise
    # mean_filter(road)


if __name__ == "__main__":
    main()
