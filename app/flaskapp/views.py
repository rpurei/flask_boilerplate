from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

index_page = Blueprint('index_page', __name__, template_folder='templates')


@index_page.route('/', defaults={'page': 'index'})
@index_page.route('/<page>')
def show(page):
    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        return render_template(f'404.html')
