from PIL import Image

def convert_image(input_path, output_path):
    img = Image.open(input_path)
    rgb_img = img.convert("RGB")
    rgb_img.save(output_path)
