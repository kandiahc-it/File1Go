from PIL import Image

def compress_image(input_path, output_path, quality=40):
    img = Image.open(input_path)
    img.save(output_path, optimize=True, quality=quality)
