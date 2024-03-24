from matplotlib import pyplot as plt

import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_optimized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci_optimized(n-1, memo) + fibonacci_optimized(n-2, memo)
    return memo[n]


def draw_results(res1, res2, inputs):
    plt.scatter(inputs, res1, label='Not optimized')
    plt.scatter(inputs, res2, label='Optimized', marker="*")
    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.title('Size vs Time')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    inputs = [1, 5, 10, 15, 20, 25, 30, 35]  # for an input bigger than 35 my computer gets stuck
    fib_results = []
    optimized_results = []
    file = open('C:/Users/Layan/PycharmProjects/hasub-backend-exercise1/scalability/basic_time_performance'
                '/fibonacci/time_results', 'a+')

    for input in inputs:
        start = time.perf_counter()
        fibonacci(input)
        end = time.perf_counter()
        fib_results.append(float(end - start))

        start = time.perf_counter()
        fibonacci_optimized(input)
        end = time.perf_counter()
        optimized_results.append(float(end - start))
    file.write("Fibonacci not optimized average time : " + str(sum(fib_results) / len(inputs)) + "\n")
    file.write("Fibonacci optimized average time : " + str(sum(optimized_results) / len(inputs)))
    draw_results(fib_results, optimized_results, inputs)


