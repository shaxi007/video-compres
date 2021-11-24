from flask import Flask, render_template, request, send_file
import os
import comp
import uuid


app = Flask('app')

UPLOAD_FOLDER = f'{os.path.dirname(os.path.realpath(__file__))}/uploads/'


@app.route('/')
def run():
    return '<h1>Hello, Server!</h1>'


@app.post('/upload')
def upload():
    videouuid = str(uuid.uuid4())
    f = request.files['file']
    print(f)
    filename = UPLOAD_FOLDER + videouuid + f.filename
    f.save(filename)
    comp.compressVideos(filename, UPLOAD_FOLDER)

    return f"""file uploaded successfully 
    <a href="/uploads/{videouuid}">Download</a>
    """



@app.route('/uploads/<path:filename>')
def download_file(filename):
    print(filename)
    return send_file(UPLOAD_FOLDER + 'compressed/' + filename, as_attachment=True)




app.run(host='0.0.0.0', port=os.environ['PORT'])
