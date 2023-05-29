from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        n = int(request.form['number'])
        results = []
        for i in range(1, 11):
            result = f'{n} x {i} = {n * i}'
            results.append(result)
        return render_template('result.html', number=n, results=results)
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def show_result():
    n = int(request.form['number'])
    results = []
    for i in range(1, 11):
        result = f'{n} x {i} = {n * i}'
        results.append(result)
    return render_template('result.html', number=n, results=results)

if __name__ == '__main__':
    app.run()
