from PIL import Image
import time
from multiprocessing import Process


def reverse_image(image, start, end, i):
    cols, rows = image.size
    for y in range(start, end):
        for x in range(cols):
            pix = image.load()
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            pix[x, y] = (255 - r, 255 - g, 255 - b)
    box = (0, start, cols, end)
    cropped = image.crop(box)
    cropped.save(str(i) + '_multi.jpg')


def main():
    image = Image.open("C:/Users/Layan/PycharmProjects/hasub-backend-exercise1/scalability/reverse_image/img1.jpg")
    cols, rows = image.size
    threads_num = 3
    chunk_size = rows // threads_num
    start = time.perf_counter()
    processes = []

    for i in range(threads_num):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size if i < 2 else rows
        process = Process(target=reverse_image, args=(image, start_idx, end_idx, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    res = Image.new(mode='RGB', size=image.size)
    for i in range(threads_num):
        name = str(i) + "_multi.jpg"
        image = Image.open("C:/Users/Layan/PycharmProjects/hasub-backend-exercise1/scalability/reverse_image/" + name)
        res.paste(image, (0, i * chunk_size))

    res.save("reversed_multi_thread.jpg")
    end = time.perf_counter()
    print(f"Total time to run multi thread is: {end - start}")


if __name__ == "__main__":
    main()
