# Image Security 

# Project Overview
This project demonstrates the implementation of image security techniques to embed and verify security codes in images using three distinct algorithms: Visible,
Fragile, and Detect. These algorithms aim to protect images from unauthorized modifications and provide an easy way to detect any tampering or alteration of the image content. 
The project uses Python and various libraries for image processing.

# Features
# 1. Visible Security Code
A visible watermark (security code) is embedded directly into the image in such a way that it is perceptible to the human eye.
This approach ensures that anyone viewing the image can clearly see the embedded security code, making it an easily verifiable form of protection.
# 2. Fragile Security Code
A fragile watermark is embedded into the image in such a way that it is highly sensitive to alterations or tampering.
If the image is modified, the fragile watermark will be altered or destroyed, signaling that the image has been tampered with.
This algorithm ensures the integrity of the image and can be used to detect any unauthorized changes.
# 3. Detectable Security Code
A detectable watermark is embedded in the image but is not visible to the human eye.
This invisible watermark can be detected using a special algorithm and is useful for proving ownership or validating authenticity without visually altering the image.
It remains intact even if the image is resized, cropped, or slightly altered.

#How It Works
The security codes are applied to images using a combination of image processing techniques. Each of the algorithms described above is designed to serve a specific purpose:

# Visible Security Code:

The visible watermark is embedded in the image by adjusting the pixel values of certain regions in the image.
This watermark is visible, meaning it will not go unnoticed but serves as an immediate identification of authenticity.
Fragile Security Code:

The fragile watermark uses algorithms such as altering the least significant bits (LSB) of the image data to embed the security code.
This watermark is highly sensitive to any changes in the image, so even small modifications will destroy or distort the code.
Detectable Security Code:

The invisible watermark is encoded into the image in such a way that it does not change the image's appearance.
Special detection algorithms are used to read and verify the watermark, even if the image is altered or compressed.
