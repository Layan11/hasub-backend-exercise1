from PIL import Image
import time


def reverse_image(image):
    pix = image.load()
    cols, rows = image.size
    for y in range(rows):
        for x in range(cols):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            pix[x, y] = (255 - r, 255 - g, 255 - b)
    image.save('reversed_single_thread.jpg')


if __name__ == '__main__':
    image = Image.open("C:/Users/Layan/PycharmProjects/hasub-backend-exercise1/scalability/reverse_image/img1.jpg")
    start = time.perf_counter()
    reverse_image(image)
    end = time.perf_counter()
    print(F"Time took using one thread: {end - start}")

