import os
import subprocess

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def upload_file():
    proc = subprocess.Popen(['ls', app.config["UPLOAD_FOLDER"]], stdout=subprocess.PIPE)
    cmd_response = proc.stdout.read().decode("utf-8")
    cmd_response = cmd_response.replace('\n', '<br>')
    response = f"<h2>Files uploaded to server:</h2> {cmd_response if cmd_response else 'No files'}"
    return response


if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = '/opt/shared/server_files'
    app.run(host='0.0.0.0', port=7000, debug=True)
