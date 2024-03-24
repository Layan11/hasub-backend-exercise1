from soupsieve.util import lower
import time


def count_occurrence(word, text):
    for i in range(100):
        for item in text:
            if type(item) != str:
                return -1
    counter = 0
    for item in text:
        if lower(item) == word:
            counter += 1
    return counter


def count_occurrence_optimized(word, text):
    counter = 0
    for item in text:
        if lower(item) == word:
            counter += 1
    return counter


if __name__ == '__main__':
    files = ['size1', 'size10', 'size100', 'size500', 'size1000', 'size5000', 'size10000']
    occurrence = occurrence_opt = 0
    word = 'word'
    total_not_optimized = total_optimized = 0
    for file in files:
        data = []
        with open('C:/Users/Layan/PycharmProjects/hasub-backend-exercise1/scalability/basic_time_performance'
                  '/word_occurrence/input_textfiles/' + str(file), 'r') as f:
            # split the file into words and save them in the array 'data'
            for line in f:
                data.extend(line.split())
            for i in range(len(data)):
                data[i] = data[i].rstrip(",")
                data[i] = data[i].rstrip(".")
            start = time.perf_counter()
            occurrence += count_occurrence(word, data)
            end = time.perf_counter()
            total_not_optimized += (end - start)

            start = time.perf_counter()
            occurrence_opt += count_occurrence_optimized(word, data)
            end = time.perf_counter()
            total_optimized += (end - start)

    print(f"Occurrence of the word '{word}' in all the text files is {occurrence_opt}")

    file = open('C:/Users/Layan/PycharmProjects/hasub-backend-exercise1/scalability/basic_time_performance'
                '/word_occurrence/time_results', 'a+')
    file.write("Count occurrence not optimized average time : " + str(total_not_optimized / len(files)) + "\n")
    file.write("Count occurrence optimized average time : " + str(total_optimized / len(files)))
