from PIL import Image

def detect_watermark_changes(original_image_path, watermarked_image_path, watermark_text):
    original = Image.open("test.jpg").convert('RGB')
    watermarked = Image.open("visible_watermarked_output1.jpg").convert('RGB')
    width, height = original.size
    original_pixels = original.load()
    watermarked_pixels = watermarked.load()

    watermark_bits = ''.join(format(ord(char), '08b') for char in watermark_text)
    watermark_bits += '0' * (width * height * 3 - len(watermark_bits))

    bit_index = 0
    changes_detected = False
    for y in range(height):
        for x in range(width):
            original_r, original_g, original_b = original_pixels[x, y]
            watermarked_r, watermarked_g, watermarked_b = watermarked_pixels[x, y]

            if bit_index < len(watermark_bits):
                if (original_r & 1) != (watermarked_r & 1):
                    changes_detected = True
                    break
                bit_index += 1
            if bit_index < len(watermark_bits):
                if (original_g & 1) != (watermarked_g & 1):
                    changes_detected = True
                    break
                bit_index += 1
            if bit_index < len(watermark_bits):
                if (original_b & 1) != (watermarked_b & 1):
                    changes_detected = True
                    break
                bit_index += 1

        if changes_detected:
            break

    if changes_detected:
        print("Changes detected in the watermarked image.")
    else:
        print("No changes detected in the watermarked image.")

if __name__ == "__main__":
    original_image_path = "test.jpg"
    watermarked_image_path = "test.jpg"
    watermark_text = "fragile_watermark"
    detect_watermark_changes(original_image_path, watermarked_image_path, watermark_text)
