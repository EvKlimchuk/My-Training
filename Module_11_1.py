from PIL import Image, ImageOps, ImageDraw

# Load the uploaded image
input_path = "1024 (27).jpg"
output_path = "circular_image.png"

# Open the image
image = Image.open(input_path).convert("RGBA")

# Create a circular mask
size = min(image.size)
mask = Image.new("L", (size, size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, size, size), fill=255)

# Apply the mask to the image
result = ImageOps.fit(image, (size, size), centering=(0.5, 0.5))
result.putalpha(mask)

# Save the output
result.save(output_path)
output_path
