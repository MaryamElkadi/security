from PIL import Image

def embed_fragile_watermark(input_image_path, output_image_path, watermark_text):
    original = Image.open("test.jpg").convert('RGB')
    width, height = original.size #store original size
    pixels = original.load()

    watermark_bits = ''.join(format(ord(char), '08b') for char in watermark_text) #convert to binary string (ASCII Code)
    watermark_bits += '0' * (width * height * 3 - len(watermark_bits))  # ensure its length matches the total number of bits available in the image 

    bit_index = 0
    for y in range(height): #loop over pixels (rows)
        for x in range(width): #(columns)
            r, g, b = pixels[x, y]
            if bit_index < len(watermark_bits):
                r = (r & ~1) | int(watermark_bits[bit_index])
                bit_index += 1
            if bit_index < len(watermark_bits):
                g = (g & ~1) | int(watermark_bits[bit_index])
                bit_index += 1
            if bit_index < len(watermark_bits):
                b = (b & ~1) | int(watermark_bits[bit_index])
                bit_index += 1
            pixels[x, y] = (r, g, b)

    original.save(output_image_path)

if __name__ == "__main__":
    input_image_path = "test.jpg"
    output_image_path = "watermarked_image.jpg"
    watermark_text = "fragile_watermark"
    embed_fragile_watermark(input_image_path, output_image_path, watermark_text)
