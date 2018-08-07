from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template('index.html') #"Render Dashboard!"

@app.route("/")
def presentation():
    return render_template('presentation.html') #"Render Presentation page!"

@app.route("/")
def tables():
    return render_template('tables.html') #"Render Tables page!"

@app.route("/")
def FEDRePORTER_table():
    return render_template('FEDReporter_table.html') #Render  NIH Federal RePORTER Tables page

@app.route("/")
def SunburstChart():
    return render_template('sunburst.html') # Render sunburst chart    

if __name__ == "__main__":
    app.run(debug=True)