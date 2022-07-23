from flask import Flask, make_response, render_template, request, redirect, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photowall_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Photo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/')
def home():
    photos = Photo.query.all()
    return render_template('index.html', photos=photos[::-1])


@app.route('/delete/<int:sno>')
def delete(sno):
    try:
        photo = Photo.query.filter_by(sno=sno).first()
        db.session.delete(photo)
        db.session.commit()
    except:
        resp = make_response(404)
        return resp

    return redirect('/')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        url = request.form.get('url')
        photo = Photo(title=title, url=url)
        db.session.add(photo)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form.get('title')
        url = request.form.get('url')
        photo = Photo.query.filter_by(sno=sno).first()
        photo.title = title
        if url:
            photo.url = url
        db.session.add(photo)
        db.session.commit()
        return redirect('/')
    photo = Photo.query.filter_by(sno=sno).first()
    return render_template('update.html', photo=photo)


@app.route('/view/<int:sno>', methods=['GET', 'POST'])
def view(sno):
    photo = Photo.query.filter_by(sno=sno).first()
    return render_template('view.html', photo=photo)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
