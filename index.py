from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os
import PyPDF2


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'documentos'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['pdf']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'Documento enviado com sucesso!'

@app.route('/documentos')
def documentos():
    documentos = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('documentos.html', documentos=documentos)



@app.route('/validador')
def download():
    return render_template('validador.html')
    

@app.route('/arquivo', methods=['POST', 'GET'])
def arquivo():
    filename = request.form['filename']
    file_path = os.path.join('c:/projetos/diplomas/documentos', filename +'.pdf')

    if os.path.isfile(file_path):
        return send_file(file_path, as_attachment=True)
 
    else:
        return 'Arquivo não encontrado.'
 



if __name__ == '__main__':
    app.run(debug=True)
