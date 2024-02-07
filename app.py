from flask import Flask, request, Response, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user_agent = request.headers.get('User-Agent', '').lower()
    if 'twitterbot' in user_agent:
        response = Response(status=302)
        response.headers['Location'] = "https://www.apple.com"
        return response
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

