from flask import Flask

app = Flask(__name__, static_folder = 'static', static_url_path='')

@app.route('/report')
def report():
    return app.send_static_file('report.html')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)