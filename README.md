Image Compression Algorithm
This is the backend of an image compression algorithm developed using Flask, a popular Python web framework, and the Python Imaging Library (Pillow).
1.1	Functionality
The code provides a web service that compresses an image file uploaded to the server. The endpoint /compress_image accepts a POST request with an image file, compresses the image, and returns the compressed image file along with its original and compressed sizes in JSON format. The compression is done using the Pillow library and the JPEG format with a quality of 50 is used for compression.

1.2	Installation
To run this code, you need to have Python and the following Python packages installed on your machine:
•	Flask
•	Pillow
You can install these packages using pip, a package manager for Python, by running the following command in your terminal:
pip install flask pillow

1.3	Usage
Save the code in a Python file with a .py extension.
Run the Python file by typing python <filename>.py in your terminal.
Once the server is up and running, you can test the API by sending a POST request to the /compress_image endpoint with an image file in the request body.

1.4	Sample request

import requests
url = 'http://localhost:5000/compress_image'
files = {'image': open('path/to/image.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.json())

1.5	Sample response
{
    "compressed_image": "\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffdJFIF\ufffd\ufffd\ufffd\ufffd\ufffdExif\ufffd\ufffd\x00MM\ufffe*\x00\x00\x00\x08\x00\x11\x01\x0f\x00\x02\x00\x00\x00",
    "original_size": 123456,
    "compressed_size": 65432
}
