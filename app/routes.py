from app.functions import rechercheQuery
from flask import render_template, request
from app import app
from app import functions
import re


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


@app.route('/recherche', methods=['POST','GET'])
def recherche():

    
    critere = request.form['recherche-form']

    article = rechercheQuery(critere)

    article_text = re.sub(critere, f"<U><strong>{critere}</strong></U>", article['text'], flags=re.I)

    context = {
        'titre': article['titre'],
        'soustitre': article['soustitre'],
        'author': article['author'],
        'text': article_text,
        'lien': article['lien']
    }

    
    return render_template('recherche.html', **context)

