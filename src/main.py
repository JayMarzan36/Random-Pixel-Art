import random, os
from PIL import Image


def get_closest(color_list, current_pixel):
    if not current_pixel == (0, 0, 0) or not current_pixel == (255, 255, 255):
        differences = {}
        current_r, current_g, current_b = current_pixel
        for i in color_list:
            list_r, list_g, list_b = i
            result = abs((list_r - current_r) + (list_g - current_g) + (list_b - current_b))
            differences.update({result: i})
        sorted_differences = sorted(differences.keys())
        selected_color = differences.get(sorted_differences[0])
        return selected_color
    else:
        return current_pixel

def save_file(file_name, image):
    dir_name = os.path.dirname(__file__)
    file_path = dir_name + f"/output/{file_name}.jpg"
    image.save(file_path)

def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


def color_list(amount_of_colors=5):
    final_list = []
    for i in range(amount_of_colors):
        final_list.append(random_color())
    return final_list


def make_noise():
    new_image = Image.new("RGB", (300, 300))  # 60, 60

    new_image_pixels = new_image.load()
    for i in range(new_image.size[0]):  # X axis
        for j in range(new_image.size[1]):  # Y axis
            color = random_color()
            new_image_pixels[i, j] = color
    save_file("output_noise", new_image)


def remake():
    dir_name = os.path.dirname(__file__)
    noise_path = dir_name + "/output/output_noise.jpg"

    noise_image = Image.open(noise_path)
    noise_image_pixels = noise_image.load()

    colors = color_list(2)

    for i in range(noise_image.size[0]):
        for j in range(noise_image.size[1]):
            current_pixel = noise_image_pixels[i, j]
            new_color = get_closest(colors, current_pixel)

            noise_image_pixels[i, j] = new_color
    save_file("remake_output", noise_image)


make_noise()
remake()
