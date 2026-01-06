from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  

#db config.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

db = SQLAlchemy(app)

#model creation
class studinfo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    city = db.Column(db.String(20))
    email = db.Column(db.String(100))

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        nm= request.form["name"]
        ct = request.form["city"]
        em = request.form["email"]

        st=studinfo(name=nm,city=ct,email=em)
        db.session.add(st)
        db.session.commit()
        print("record inserted!")
        return redirect('showdata')
    else:
        print("Error!")
    return render_template('index.html')

@app.route('/showdata',methods=['GET'])
def showdata():
    stdata=studinfo.query.all()
    return render_template('showdata.html',stdata=stdata)

@app.route('/delete/<int:id>')
def delete(id):
    data = studinfo.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/showdata')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    data = studinfo.query.get(id)

    if request.method == 'POST':
        data.name = request.form['name']
        data.city = request.form['city']
        data.email = request.form['email']
        db.session.commit()
        return redirect('/showdata')

    return render_template('update.html', data=data)


if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)