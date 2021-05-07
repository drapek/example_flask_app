import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file_get_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = '/var/files'
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        raise KeyError(f"Direcotry {app.config['UPLOAD_FOLDER']} doesn't exists. Please create this dir or change "
                       f"the value of app.config['UPLOAD_FOLDER']")
    app.run(host='0.0.0.0', port=5000, debug=True)
