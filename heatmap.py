import matplotlib.pyplot as plt
import numpy as np

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
        file.seek(0, 2)
        num_of_bytes = file.tell()
    for _ in range((num_of_bytes // bits_to_analyze) - 1):
        x = int(bits[counter : counter + bits_to_analyze], 2)
        y = int(bits[counter + bits_to_analyze : counter + 2 * bits_to_analyze], 2)
        add_point(x, y, heatmap_u)
        counter = counter + bits_to_analyze
    plt.imshow(heatmap_u, cmap="hot", interpolation="lanczos")
    plt.colorbar()
    plt.show()

    heatmap_w1 = np.zeros(heatmap_size)
    counter = 0
    with open("C:/Users/User/Desktop/Dokumenty/inzynierka/whitened1.txt", "rb") as file:
        bits = file.read()
        file.seek(0, 2)
        num_of_bytes = file.tell()
    for _ in range(num_of_bytes // (2 * bits_to_analyze)):
        x = int(bits[counter : counter + bits_to_analyze], 2)
        y = int(bits[counter + bits_to_analyze : counter + 2 * bits_to_analyze], 2)
        add_point(x, y, heatmap_w1)
        counter = counter + 2 * bits_to_analyze
    plt.imshow(heatmap_w1, cmap="hot", interpolation="lanczos")
    plt.colorbar()
    plt.show()

    heatmap_w2 = np.zeros(heatmap_size)
    counter = 0
    with open("C:/Users/User/Desktop/Dokumenty/inzynierka/whitened2.txt", "rb") as file:
        bits = file.read()
        file.seek(0, 2)
        num_of_bytes = file.tell()
    for _ in range(num_of_bytes // (2 * bits_to_analyze)):
        x = int(bits[counter : counter + bits_to_analyze], 2)
        y = int(bits[counter + bits_to_analyze : counter + 2 * bits_to_analyze], 2)
        add_point(x, y, heatmap_w2)
        counter = counter + 2 * bits_to_analyze
    plt.imshow(heatmap_w2, cmap="hot", interpolation="lanczos")
    plt.colorbar()
    plt.show()


delay_var_method()
