import time


def timeit(function):
    def wrapper():
        startTime = time.time()
        function()
        executionTime = round(time.time() - startTime, 6)
        print("Execution time: " + str(executionTime) + " seconds")

    return wrapper
