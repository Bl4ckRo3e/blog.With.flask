from flask import Blueprint, render_template, request
from models import Article, User, category, db
from search_system import SearchEngine
from autoLog import Log



# this is for setting up the blue prints
route = Blueprint('route', __name__)


# this is for routing.
# this is home route
# # # add treadings ...
@route.route('/')
@route.route('/home/')
def home():
    ip   = request.headers.get('X-Forwarded-For', request.remote_addr)
    Log(ip, 'open home')
    items = list(Article.query.order_by(Article.id.desc()).limit(3).all())
    treads = list(Article.query.order_by(Article.count.desc()).limit(3).all())
    if items == 0 :
        items, treads = [], []
    return render_template('home.html', cat=list(category.query.all()), writer=list(User.query.filter_by(mode="writer")), photo=list(User.query.filter_by(mode="photo")), posts=items, trading=treads)

# this is for post show route
@route.route('/show_post/<int:id>/')
def show_post(id):
    ip   = request.headers.get('X-Forwarded-For', request.remote_addr)
    post = list(Article.query.filter_by(id=id))
    if len((post)) == 1 :
        new_post = post[0]
        new_post.count = new_post.count + 1
        db.session.commit()
        Log(ip, f'open {post[0].title}')
        return render_template('article.html',item=post[0], cat=list(category.query.all()), writer=list(User.query.filter_by(mode="writer")), photo=list(User.query.filter_by(mode="photo")))
    else:
        Log(ip, 'Get 404 Error')
        return render_template('404.html')

# this is for search route
@route.route("/search/", methods=['POST'])
def search():
    ip   = request.headers.get('X-Forwarded-For', request.remote_addr)
    word = request.form['search']
    if len(word) > 0:
        search = (SearchEngine(word=word))
        search, count = search.main()
        Log(ip, f'Get all article search -> {word}')
        return render_template("search.html", word=word,cat=list(category.query.all()), writer=list(User.query.filter_by(mode="writer")), photo=list(User.query.filter_by(mode="photo")), result=search, count=count)
    else:
        return render_template('404.html')

# this is for show all Article of user
@route.route("/show_all_article/<string:user>/")
def show_all_article(user):
    ip   = request.headers.get('X-Forwarded-For', request.remote_addr)
    all_articles = Article.query.filter_by(writer=user)
    if len(list(all_articles)) > 0:
        Log(ip, f'Get all article user -> {user}')
        return render_template('search.html',word=user, count=len(list(all_articles)), result=list(all_articles), cat=list(category.query.all()), writer=list(User.query.filter_by(mode="writer")), photo=list(User.query.filter_by(mode="photo")))
    else:
        Log(ip, f'Get all article user -> {user}')
        return render_template('search.html',word=user, count=0, result=[], cat=list(category.query.all()), writer=list(User.query.filter_by(mode="writer")), photo=list(User.query.filter_by(mode="photo")))
    
# this is for show all Article by category
@route.route("/show_all_article_by_cat/<string:name>/")
def show_all_article_by_cat(name):
    ip   = request.headers.get('X-Forwarded-For', request.remote_addr)
    all_articles = Article.query.filter_by(category=name)
    if len(list(all_articles)) > 0:
        Log(ip, f'Get all article cat -> {name}')
        return render_template('search.html', word=name, count=len(list(all_articles)), result=list(all_articles), cat=list(category.query.all()), writer=list(User.query.filter_by(mode="writer")), photo=list(User.query.filter_by(mode="photo")))
    else:
        Log(ip, f'Get all article cat -> {name}')
        return render_template('search.html', word=name, count=0, result=[], cat=list(category.query.all()), writer=list(User.query.filter_by(mode="writer")), photo=list(User.query.filter_by(mode="photo")))
    




if __name__ == '__main__':
    print("Wrong File Run this is routes")