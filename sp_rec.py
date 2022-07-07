from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html'), 201
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      r = sr.Recognizer()
      with sr.AudioFile(f) as source:
         audio = r.listen(source)
         text = r.recognize_google(audio, language='th-TH')
      #txtFile = open('text2.txt', 'a')
      #txtFile.writelines(text)
      f.save(secure_filename(f.filename))
      return jsonify({"text":text})

		
if __name__ == '__main__':
   app.run(debug = True)