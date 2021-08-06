#import a liberary
from flask import Flask,render_template,request
import joblib

#instance of an app
app=Flask(__name__)

#loading the model
model=joblib.load("dib_79.pkl")

@app.route('/' )
def hello():
    return render_template("form.html")
@app.route('/submit', methods=["POST"])
def form_data():
    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')
    test=request.form.get('test')

    pred=model.predict([[preg,plas,pres,skin,mass,test,pedi,age]])
    print(pred)
    
    if pred[0]==1:
        out="diabatic"
    else:
        out="not daibatic"
    return render_template("index.html",data=f'person is {out}')



#run the app
if __name__=="__main__":
    app.run(debug=True)
