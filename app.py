from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_caption():

    instagram_url = request.form['instagram_url']


    response = requests.get(instagram_url)


    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')


        caption = soup.find('meta', property='og:description')['content']

        with open('caption.txt', 'w', encoding='utf-8') as file:
            file.write(caption)


        return redirect(url_for('show_caption'))
    else:
        return "Failed to fetch Instagram page"



@app.route('/show_caption')
def show_caption():

    with open('caption.txt', 'r', encoding='utf-8') as file:
        caption = file.read()

    return render_template('show_caption.html', caption=caption)



if __name__ == '__main__':
    app.run(debug=True)
