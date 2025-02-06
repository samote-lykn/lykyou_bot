from flask import Flask, send_file

app = Flask(__name__)

@app.route('/rss')
def serve_rss():
    return send_file('tiktok_feed.xml')

# if __name__ == '__main__':
   # app.run(host='0.0.0.0', port=8080)
