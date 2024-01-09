import matplotlib.pyplot as plt
import numpy as np
import serial

ser = serial.Serial("COM4", baudrate=115200)

bits_to_count = 10000000

count_nw_zeros = 0
count_nw_ones = 0
count_w1_zeros = 0
count_w1_ones = 0
count_w2_zeros = 0
count_w2_ones = 0

# czyszczenie plikow
with open("C:/Users/User/Desktop/Dokumenty/inzynierka/unwhitened.txt", "w", encoding="utf-8") as unwhitened_w:
    pass
with open("C:/Users/User/Desktop/Dokumenty/inzynierka/whitened1.txt", "w", encoding="utf-8") as whitened1_w:
    pass
with open("C:/Users/User/Desktop/Dokumenty/inzynierka/whitened2.txt", "w", encoding="utf-8") as whitened2_w:
    pass

while int(ser.read(1)) != 4:
    continue

while True:
    with open("C:/Users/User/Desktop/Dokumenty/inzynierka/unwhitened.txt", "a", encoding="utf-8") as unwhitened_w:
        while True:
            data = int((ser.read(1)))
            if data == 1 or data == 0:
                if data == 0:
                    count_nw_zeros = count_nw_zeros + 1
                    unwhitened_w.write(str(0))
                else:
                    count_nw_ones = count_nw_ones + 1
                    unwhitened_w.write(str(1))
            else:
                break
    with open("C:/Users/User/Desktop/Dokumenty/inzynierka/whitened1.txt", "a", encoding="utf-8") as whitened1_w:
        while True:
            data = int((ser.read(1)))
            if data == 1 or data == 0:
                if data == 0:
                    count_w1_zeros = count_w1_zeros + 1
                    whitened1_w.write(str(0))
                else:
                    count_w1_ones = count_w1_ones + 1
                    whitened1_w.write(str(1))
            else:
                break
    with open("C:/Users/User/Desktop/Dokumenty/inzynierka/whitened2.txt", "a", encoding="utf-8") as whitened2_w:
        while True:
            data = int((ser.read(1)))
            if data == 1 or data == 0:
                if data == 0:
                    count_w2_zeros = count_w2_zeros + 1
                    whitened2_w.write(str(0))
                else:
                    count_w2_ones = count_w2_ones + 1
                    whitened2_w.write(str(1))
            else:
                break

    # liczenie rozkladu procentowego bitow do stworzenia wykresow
    if count_nw_zeros + count_nw_ones >= bits_to_count:
        # Obliczanie niwybielonych
        nw_zeros_percentage = round((count_nw_zeros / (count_nw_zeros + count_nw_ones)) * 100, 4)
        nw_ones_percentage = round((count_nw_ones / (count_nw_zeros + count_nw_ones)) * 100, 4)

        # Obliczanie wybielonych raz
        w1_zeros_percentage = round((count_w1_zeros / (count_w1_ones + count_w1_zeros)) * 100, 4)
        w1_ones_percentage = round((count_w1_ones / (count_w1_ones + count_w1_zeros)) * 100, 4)

        # Obliczanie wybielonych dwa razy
        w2_zeros_percentage = round((count_w2_zeros / (count_w2_ones + count_w2_zeros)) * 100, 4)
        w2_ones_percentage = round((count_w2_ones / (count_w2_ones + count_w2_zeros)) * 100, 4)

        # Tworzenie wykresów
        labels = ["Zera", "Jedynki"]
        colors = ["blue", "red"]
        percentages_nw = [nw_zeros_percentage, nw_ones_percentage]
        percentages_w1 = [w1_zeros_percentage, w1_ones_percentage]
        percentages_w2 = [w2_zeros_percentage, w2_ones_percentage]

        plt.figure(figsize=(12, 6))
        plt.ylabel("Procent")

        plt.subplot(1, 3, 1)
        plt.bar(labels, percentages_nw, color=colors)
        for i, percentage in enumerate(percentages_nw):
            plt.annotate(f"{percentage}%", (i, percentage), ha="center", va="bottom")
        plt.title("bity niewybielone")

        plt.subplot(1, 3, 2)
        plt.bar(labels, percentages_w1, color=colors)
        for i, percentage in enumerate(percentages_w1):
            plt.annotate(f"{percentage}%", (i, percentage), ha="center", va="bottom")
        plt.title("bity wybielone raz")

        plt.subplot(1, 3, 3)
        plt.bar(labels, percentages_w2, color=colors)
        for i, percentage in enumerate(percentages_w2):
            plt.annotate(f"{percentage}%", (i, percentage), ha="center", va="bottom")
        plt.title("bity wybielone dwa razy")

        print(count_nw_ones)
        print(count_nw_zeros)
        print(count_w1_ones)
        print(count_w1_zeros)
        print(count_w2_ones)
        print(count_w2_zeros)

        plt.show()

        # while 1:
        #     continue
        break
