import time
import flask
import pytube
import youtubesearchpython as ysp

app = flask.Flask(__name__, static_url_path='/')

def is_using_client():
    flask.request.headers.get('User-Agent') != 'MUSE Client'

@app.route('/')
def home():
    return flask.redirect('/search?q=Official+Music+Video')

@app.route('/search')
def search():
    query = flask.request.args.get('q')
    results = ysp.VideosSearch(query, limit=10).result()['result']

    return flask.render_template('index.html', query=query, results=results)

@app.route('/watch')
def watch():
    video_id = flask.request.args.get('v')

    fetcher = ysp.StreamURLFetcher()
    video = ysp.Video.get(video_id)
    data = ysp.Video.getInfo(video_id)
    url = fetcher.get(video, 251)
    
    return flask.render_template('player.html', url=url, data=data)

app.run(port=7777, debug=True)