from flask import Flask, render_template
import board
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.datetime.now() 
    timeString = now.strftime("%Y-%m-%d %H:%M")
    template_data = {
        'title' : 'Hello',
        'time' : timeString,
    }
    return render_template('index.html', **template_data)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')


# templates / index.html
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{ title }}</title>
</head>
<body>
   <h1>Hello, World!</h1> 
   <h2>The date and Time on th server is : {{ time }}</h2>
</body>
</html>
'''
