from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def playground(times=3):
    msg="welcome"
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html',times=times) 
    
@app.route('/<int:times>')
def multbox(times):
    return render_template("index.html",times=times)

@app.route('/<int:times>/<color>')
def change_color(times,color):
    return render_template('index.html',times=times,color=color)
# import statements, maybe some other routes

# @app.route('/success')
# def success():
#     return "success"


    
# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":
    app.run(debug=True,port=5001)
# app.run(debug=True, host="localhost", port=8000)
