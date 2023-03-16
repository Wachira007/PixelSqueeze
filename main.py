#This is the backend of an image compression algorithm

from flask import Flask, request, jsonify
import io
from PIL import Image

app = Flask(__name__)

@app.route('/compress_image', methods=['POST'])
def compress_image():
    # Get the uploaded image file
    image_file = request.files['image']

    # Load the image using Pillow
    image_content = image_file.read()
    image = Image.open(io.BytesIO(image_content))

    # Check the size of the image
    original_size = len(image_content)
    print('Original image size:', original_size)

    # Compress the image using Pillow
    compressed_image = io.BytesIO()
    image.save(compressed_image, format='JPEG', quality=50)

    # Calculate the size of the compressed image
    compressed_size = len(compressed_image.getvalue())
    print('Compressed image size:', compressed_size)

    # Return the compressed image and its size as JSON
    return jsonify({
        'compressed_image': compressed_image.getvalue(),
        'original_size': original_size,
        'compressed_size': compressed_size
    })

if __name__ == '__main__':
    app.run(debug=True)
