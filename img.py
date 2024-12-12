import os

os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

from flask import Flask, request, render_template, send_file
import matplotlib.pyplot as plt
# import vtracer
from sam2.build_sam import build_sam2



app = Flask(__name__)

from cut2 import click_handler_bp, cutAtVector, cutAt

app.register_blueprint(click_handler_bp)


# @app.route('/')
# def index():
#     # 
#     return render_template('test.html')

@app.route('/success_page')
def success():
    import time
    
    start_time = time.time()
    # Your existing code for the success route goes here
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    print(f"Time elapsed: {time_elapsed:.4f} seconds")
    return "???"
    # return render_template('res.html')

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return process_uploaded_file(file_path)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part', 400
        
    file = request.files['file']
    x = request.form.get('x')
    y = request.form.get('y')
    
    if file.filename == '':
        return 'No selected file', 400
        
    if not (x and y):
        return 'Missing coordinates', 400
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Convert coordinates to integers
        try:
            x = int(x)
            y = int(y) 
        except ValueError:
            return 'Invalid coordinates format', 400
            
        return cutAtVector(filename, x, y), 200

        # cut = cutAt(filename, x, y), 200
        # return send_file(cut, mimetype='image/png')
        
    return 'Invalid file type', 400


def process_uploaded_file(file_path):
    # Get the filename from the file path
    filename = os.path.basename(file_path)
    return render_template('uploaded_image.html', filename=filename)


# @app.route('/get-coordinates', methods=['GET'])
# def get_coordinates():
#     x = request.args.get('x')
#     y = request.args.get('y')
#     print(f'Clicked coordinates: x={x}, y={y}')
#     return 'Coordinates received'

# if __name__ == '__main__':
#     app.run()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


#     <?xml version="1.0" encoding="UTF-8"?>
# <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="1024" height="683">
# <path d="M0 0 C337.92 0 675.84 0 1024 0 C1024 225.39000000000001 1024 450.78000000000003 1024 683 C686.0799999999999 683 348.15999999999997 683 0 683 C0 457.61 0 232.21999999999997 0 0 Z " fill="#FFFFFF" transform="translate(0,0)"/>
# <path d="M0 0 494932432432421 0 0 Z " fill="#78BCFF" transform="translate(556,74)"/>
# </svg>