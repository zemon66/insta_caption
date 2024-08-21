from flask import Flask, render_template, request, jsonify, session
import requests
from bs4 import BeautifulSoup
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Securely generated key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_caption():
    instagram_url = request.form['instagram_url']
    print(f"Received URL: {instagram_url}")  # Debug print
    response = requests.get(instagram_url)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        caption = soup.find('meta', property='og:description')
        if caption:
            caption_text = caption['content']
            print(f"Extracted Caption: {caption_text}")  # Debug print
            session['caption'] = caption_text
            return jsonify({'caption': caption_text})
        else:
            print("Caption meta tag not found.")  # Debug print
            return jsonify({'error': 'Caption meta tag not found.'}), 400
    else:
        print(f"Failed to fetch Instagram page. Status code: {response.status_code}")  # Debug print
        return jsonify({'error': 'Failed to fetch Instagram page.'}), 400

@app.route('/show_caption')
def show_caption():
    caption = session.get('caption', "No caption found")  
    return render_template('show_caption.html', caption=caption)

if __name__ == '__main__':
    app.run(debug=True)
