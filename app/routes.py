from app.functions import rechercheQuery
from flask import render_template
from app import app
from app import functions


@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Cristhian'
    }

    posts = [
        {
            'author': {
                'username':'Jhon'
                },
            'body': 'Beatiful'
        },
        {
            'author': {
                'username': 'Carl'
                },
            'body': 'The avengers'
        }
        
    ]
    return render_template('index.html', title='Recherche', username=user, posts=posts)


@app.route('/recherche/<critere>')
def recherche(critere):


    article = rechercheQuery(critere)

    return render_template('recherche.html', article=article)

