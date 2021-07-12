from flask import Flask, render_template, request
import pytesseract
import cv2, os
from gtts import gTTS
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")

app= Flask(__name__)
UPLOAD_FOLDER = os.path.basename(',')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if 'image' not in request.files:
            return 'There is no image in the form'
        image = request.files['image']
        file1 = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(file1)
        abc = cv2.imread(UPLOAD_FOLDER+"/"+image.filename)
        os.remove(UPLOAD_FOLDER+"/"+image.filename)
        Textdata = pytesseract.image_to_string(abc)
        print(Textdata)
        language = 'en'
        result = gTTS(text=Textdata, lang=language, slow=True)
        result.save("result.mp3")
        os.system("start result.mp3")
        return Textdata
        return render_template('Frontend.html')

if __name__ == "__main__":
    app.run(debug=True)
        
