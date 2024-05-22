def task1_2():
    import os
    from PIL import Image, ImageFilter

    images_folder = "foto/"
    filters_folder = "filters/"

    if not os.path.exists(filters_folder):
        os.makedirs(filters_folder)

    for img_file in os.listdir(images_folder):
        if img_file.endswith(".jpg") or img_file.endswith(".png"):
            img_path = os.path.join(images_folder, img_file)
            image = Image.open(img_path)
            imgfilt = image.filter(ImageFilter.BLUR)
            filtered_img_path = os.path.join(filters_folder, img_file)
            imgfilt.save(filtered_img_path)


task1_2()


def task3():
    total = 0
    print("Купить:")
    with open('danoo.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]
        for line in lines:
            product, quantity, price = line.strip().split(',')
            total += int(quantity) * int(price)
            print(f"{product} - {quantity} шт. за {price} руб.")

    print(f"Итоговая сумма: {total} руб.")


task3()