from threading import Thread
import time
import threading
from time import perf_counter
from time import sleep
from venv import create


def wite_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        with open(file_name, 'w', encoding="utf-8") as file:
            for i in range(1, word_count + 1):
                file.write(f"Какое-то слово № {i}\n")
                sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time = perf_counter()

wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")

end_time = perf_counter()
print(f"Время выполнения последовательной записи: {end_time - start_time:.6f} секунд")


# Параллельный вызов функций через потоки

start_time = perf_counter()

# Создание потоков
t = Thread(target=wite_words, args=(10, "example5.txt"))
t.start()
t.join()
t = Thread(target=wite_words, args=(30, "example6.txt"))
t.start()
t.join()
t = Thread(target=wite_words, args=(200, "example7.txt"))
t.start()
t.join()
t = Thread(target=wite_words, args=(100, "example8.txt"))
t.start()
t.join()


end_time = perf_counter()
print(f"Время выполнения потоковой записи: {end_time - start_time:.6f} секунд")