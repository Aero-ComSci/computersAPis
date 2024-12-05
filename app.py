from flask import Flask, render_template, jsonify, request
import requests
import concurrent.futures

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.post('https://cs-api.pltw.org/computers/increment?id=1')
    return render_template('index.html')

'''def hello():
    response = requests.get('http://cs-api.pltw.org/computers')
    data = response.json()
    key2 = data.get('values',[])
    total_sum = sum(key2)
    response = requests.post('https://cs-api.pltw.org/computers/increment?id=1')
    return render_template('index.html', content=response.text)'''
   
@app.route('/api/data')
def get_data():
    response = requests.get('http://cs-api.pltw.org/computers')
    data = response.json()
    return jsonify(data)

@app.route('/api/button-click')
def button_click():
    
    param = request.args.get('param')
    response = requests.post(f'https://cs-api.pltw.org/computers?text={param}!')
    return response.text

@app.route('/reset')
def reset():
    response = requests.post('https://cs-api.pltw.org/computers/reset?password=7285')
    return response.text

if __name__ == '__main__':
    app.run(debug=True)