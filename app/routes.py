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

    if request.method == 'POST':
        critere = request.form['recherche-form']

        art = rechercheQuery(critere)
        art_text = re.sub(critere, f"<U><strong>{critere}</strong></U>", art['text'], flags=re.I)
        print(art['titre'])
        
        context = {
        'titre': art['titre'],
        'soustitre': art['soustitre'],
        'author': art['author'],
        'text': art_text,
        'lien': art['lien']
        }

        return render_template('recherche.html', **context)


    # article = rechercheQuery(critere)

    # c

    # context = {
    #     'titre': article['titre'],
    #     'soustitre': article['soustitre'],
    #     'author': article['author'],
    #     'text': article_text,
    #     'lien': article['lien']
    # }

    
    return render_template('recherche.html')

