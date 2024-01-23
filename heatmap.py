import matplotlib.pyplot as plt
import numpy as np


def charts(table1, table2, table3):
    # OBLICZENIA

    # wiersze
    avg_rows_u = np.mean(table1, axis=1)
    dev_rows_u = np.std(table1, axis=1)
    avg_dev_rows_u = np.mean(dev_rows_u)
    avg_avg_rows_u = np.mean(avg_rows_u)

    avg_rows_w1 = np.mean(table2, axis=1)
    dev_rows_w1 = np.std(table2, axis=1)
    avg_dev_rows_w1 = np.mean(dev_rows_w1)
    avg_avg_rows_w1 = np.mean(avg_rows_w1)

    avg_rows_w2 = np.mean(table3, axis=1)
    dev_rows_w2 = np.std(table3, axis=1)
    avg_dev_rows_w2 = np.mean(dev_rows_w2)
    avg_avg_rows_w2 = np.mean(avg_rows_w2)

    # kolumny
    dev_columns_u = np.std(table1, axis=0)
    avg_columns_u = np.mean(table1, axis=0)
    avg_dev_columns_u = np.mean(dev_columns_u)
    avg_avg_columns_u = np.mean(avg_columns_u)

    avg_columns_w1 = np.mean(table2, axis=0)
    dev_columns_w1 = np.std(table2, axis=0)
    avg_dev_columns_w1 = np.mean(dev_columns_w1)
    avg_avg_columns_w1 = np.mean(avg_columns_w1)

    avg_columns_w2 = np.mean(table3, axis=0)
    dev_columns_w2 = np.std(table3, axis=0)
    avg_dev_columns_w2 = np.mean(dev_columns_w2)
    avg_avg_columns_w2 = np.mean(avg_columns_w2)

    # wsp zmiennosci obliczanie
    fact_u = dev_rows_u / avg_rows_u
    fact_w1 = dev_rows_w1 / avg_rows_w1
    fact_w2 = dev_rows_w2 / avg_rows_w2
    print("sredni wspolczynnik zmiennosci u:", np.mean(fact_u))
    print("sredni wspolczynnik zmiennosci w1:", np.mean(fact_w1))
    print("sredni wspolczynnik zmiennosci w2:", np.mean(fact_w2))

    # WYKRESY

    # rzedy srednia i odchylenie std
    print("srednia srednich rzedy u:", avg_avg_rows_u)
    print("srednia srednich rzedy w1:", avg_avg_rows_w1)
    print("srednia srednich rzedy w2:", avg_avg_rows_w2)
    print("srednia srednich kolumny u:", avg_avg_columns_u)
    print("srednia srednich kolumny w1:", avg_avg_columns_w1)
    print("srednia srednich kolumny w2:", avg_avg_columns_w2)
    print("srednia odchylen std w rzedach u:", avg_dev_rows_u)
    print("srednia odchylen std w rzedach w1:", avg_dev_rows_w1)
    print("srednia odchylen std w rzedach w2:", avg_dev_rows_w2)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(avg_rows_u, label="bity niewybielone", color="blue")
    plt.plot(avg_rows_w1, label="bity wybielone jednokrotnie", color="orange")
    plt.plot(avg_rows_w2, label="bity wybielone dwukrotnie", color="green")
    plt.title("Średnie wartości w rzędach")
    plt.ylabel("Średnia wartość")
    plt.xlabel("Numer rzędu mapy ciepła")
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(dev_rows_u, label="bity niewybielone", color="blue")
    plt.plot(dev_rows_w1, label="bity wybielone jednokrotnie", color="orange")
    plt.plot(dev_rows_w2, label="bity wybielone dwukrotnie", color="green")
    plt.ylabel("Wartość odchylenia standardowego")
    plt.xlabel("Numer rzędu mapy ciepła")
    plt.title("Odchylenie standardowe w rzędach")
    plt.tight_layout()
    plt.show()

    # kolumny srednia i odchylenie std
    print("srednia odchylen std w kolumnach u:", avg_dev_columns_u)
    print("srednia odchylen std w kolumnach w1:", avg_dev_columns_w1)
    print("srednia odchylen std w kolumnach w2:", avg_dev_columns_w2)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(avg_columns_u, label="bity niewybielone", color="blue")
    plt.plot(avg_columns_w1, label="bity wybielone jednokrotnie", color="orange")
    plt.plot(avg_columns_w2, label="bity wybielone dwukrotnie", color="green")
    plt.title("Średnie wartości w kolumnach")
    plt.ylabel("Średnia wartość")
    plt.xlabel("Numer kolumny na mapie ciepła")
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(dev_columns_u, label="bity niewybielone", color="blue")
    plt.plot(dev_columns_w1, label="bity wybielone jednokrotnie", color="orange")
    plt.plot(dev_columns_w2, label="bity wybielone dwukrotnie", color="green")
    plt.ylabel("Wartość odchylenia standardowego")
    plt.xlabel("Numer kolumny na mapie ciepła")
    plt.title("Odchylenie standardowe w kolumnach")
    plt.tight_layout()
    plt.show()

    # wspolczynnik zmiennosci wykres
    plt.figure(figsize=(12, 6))
    plt.plot(fact_u, label="bity niewybielone", color="blue")
    plt.plot(fact_w1, label="bity wybielone jednokrotnie", color="orange")
    plt.plot(fact_w2, label="bity wybielone dwukrotnie", color="green")
    plt.title("Współczynnik zmienności obliczony dla rzędów")
    plt.ylabel("Współczynnik zmienności")
    plt.xlabel("Numer rzędu mapy ciepła")
    plt.legend()
    plt.tight_layout()
    plt.show()


bits_to_analyze = 8
heatmap_size = (2**bits_to_analyze - 1, 2**bits_to_analyze - 1)


def add_point(x, y, heatmap):
    if 0 <= x < heatmap_size[0] and 0 <= y < heatmap_size[1]:
        heatmap[y, x] += 1


def delay_var_method():
    heatmap_u = np.zeros(heatmap_size)
    counter = 0
    with open("C:/Users/User/Desktop/Dokumenty/inzynierka/unwhitened.txt", "rb") as file:
        bits = file.read()
        # file.seek(0, 2)
        # num_of_bytes = file.tell()
        num_of_bytes = 6240313
        print(num_of_bytes)
    for _ in range((num_of_bytes // bits_to_analyze) - 1):
        x = int(bits[counter : counter + bits_to_analyze], 2)
        y = int(bits[counter + bits_to_analyze : counter + 2 * bits_to_analyze], 2)
        add_point(x, y, heatmap_u)
        counter = counter + bits_to_analyze
    plt.imshow(heatmap_u, cmap="hot", interpolation="hanning")
    plt.colorbar()
    plt.show()

    heatmap_w1 = np.zeros(heatmap_size)
    counter = 0
    with open("C:/Users/User/Desktop/Dokumenty/inzynierka/whitened1.txt", "rb") as file:
        bits = file.read()
        # file.seek(0, 2)
        # num_of_bytes = file.tell()
        num_of_bytes = 6240313
        print(num_of_bytes)
    for _ in range((num_of_bytes // bits_to_analyze) - 2):
        x = int(bits[counter : counter + bits_to_analyze], 2)
        y = int(bits[counter + bits_to_analyze : counter + 2 * bits_to_analyze], 2)
        add_point(x, y, heatmap_w1)
        counter = counter + bits_to_analyze
    plt.imshow(heatmap_w1, cmap="hot", interpolation="hanning")
    plt.colorbar()
    plt.show()

    heatmap_w2 = np.zeros(heatmap_size)
    counter = 0
    with open("C:/Users/User/Desktop/Dokumenty/inzynierka/whitened2.txt", "rb") as file:
        bits = file.read()
        file.seek(0, 2)
        num_of_bytes = file.tell()
        print(num_of_bytes)
    for _ in range((num_of_bytes // bits_to_analyze) - 2):
        x = int(bits[counter : counter + bits_to_analyze], 2)
        y = int(bits[counter + bits_to_analyze : counter + 2 * bits_to_analyze], 2)
        add_point(x, y, heatmap_w2)
        counter = counter + bits_to_analyze
    plt.imshow(heatmap_w2, cmap="hot", interpolation="hanning")
    plt.colorbar()
    plt.show()
    charts(heatmap_u, heatmap_w1, heatmap_w2)


delay_var_method()
