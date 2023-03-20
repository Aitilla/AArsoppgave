from flask import Flask

app = Flask('Translator')

@app.route('/raring')
def raring():
    print('raring')
    return 'raring'

if __name__ == '__main__':
    app.run(debug=True)