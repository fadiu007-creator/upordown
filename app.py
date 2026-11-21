from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    try:
        # Ensure scheme
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        resp = requests.get(url, timeout=5)
        return jsonify({'url': url, 'status_code': resp.status_code, 'up': True})
    except Exception as e:
        return jsonify({'url': url, 'error': str(e), 'up': False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
