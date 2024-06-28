from models import Article


# this is search Engin
class SearchEngine:
    def __init__(this, word):
        this.word = word

    def findCategory(this):
        all_category = Article.query.filter_by(category=this.word)
        return list(all_category)
    
    def findUser(this):
        all_users = Article.query.filter_by(writer=this.word)
        return list(all_users)
    
    def findArticle(this):
        all_articles = Article.query.filter_by(title=this.word)
        return list(all_articles)

        
    def main(this):
        for i in [this.findCategory(), this.findUser(), this.findArticle()]:
            if len(i) > 0:
                return i, len(i)
        return [], 0


if __name__ in '__main__':
    print("This is for Search Engine")