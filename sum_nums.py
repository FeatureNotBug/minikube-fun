from flask import Flask, render_template, flash, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_nums():
  return render_template('input.html')

@app.route('/result', methods=['GET', 'POST'])
def sum_nums():
  if request.method == 'POST':
    x = request.form['x']
    y = request.form['y']
  #return int(x)+int(y)
  return render_template('output.html', result = int(x)+int(y))

if __name__ == '__main__':
  app.run(debug = True)

