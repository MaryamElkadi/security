from PIL import Image, ImageDraw, ImageFont

def add_visible_watermark(input_image_path, output_image_path, watermark_text):
    # Open the original image
    original = Image.open("test.jpg").convert("RGBA")
    width, height = original.size

    # Make the image editable
    watermark_image = original.copy()
    draw = ImageDraw.Draw(watermark_image)

    # Define the font and size
    font_size = int(min(width, height) / 10)  # Adjust size relative to image size
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Calculate the position for the watermark (center of the image)
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Apply the watermark with semi-transparency
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))  # White text with 50% transparency

    # Convert to RGB (removing alpha channel) and save the result
    watermarked_image = watermark_image.convert("RGB")
    watermarked_image.save(output_image_path)

if __name__ == "__main__":
    input_image_path = "test.jpg"  # Path to your input image
    output_image_path = "visible_watermarked_output1.jpg"  # Path to save the watermarked image
    watermark_text = "Sample Watermark"  # Your watermark text
    add_visible_watermark(input_image_path, output_image_path, watermark_text)
