from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", x = 8, y = 8 ) 

@app.route('/<int:num_x>')
def tablaXnum(num_x):
    return render_template("index.html", x = num_x, y = 8 )

@app.route('/<int:num_x>/<int:num_y>')
def tablaXandYnum(num_x, num_y):
    return render_template("index.html", x = num_x, y = num_y )

@app.route('/<int:num_x>/<int:num_y>/<string:colorOne>/<string:colorTwo>')
def tablaXYcolor(num_x, num_y, colorOne, colorTwo):
    return render_template("index.html", x = num_x, y = num_y, colorOne = colorOne, colorTwo = colorTwo)

if __name__=="__main__":
    app.run(debug=True)