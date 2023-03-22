from flask import Flask, render_template
import os

app = Flask(__name__)

# Define the list of image files
images = []
for filename in os.listdir('static/images'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        images.append(filename)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', images = images)

@app.route('/shop')
def shop():
    return render_template('shop.html')

if __name__ == '__main__':
    app.run()
