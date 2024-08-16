from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/github', methods=['POST'])
def github_api():
    data = request.json
    access_token = data.get('access_token')
    username = data.get('username')
    github_url = data.get('github_url')

    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get(github_url, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': response.json()}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)