import csv
from flask import Flask,jsonify,request
from storage import all_articles,liked_articles,unliked_articles 
app = Flask(__name__)
@app.route("/get-articles")
def get_articles():
    article_data={
        "title":all_articles[0][19],
        "release_date":all_articles[0][13] or "n/a",
        "rating":all_articles[0][20],
        "overview":all_articles[0][19]
    }
    return jsonify({
        "data":article_data,
        "status":"success"
    })

@app.route("liked-articles",methods=['POST'])
def liked_articles():
    article=all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"Success"
    }),200

@app.route("unliked-articles",methods=['POST'])
def unliked_articles():
    article=all_articles[0]
    unliked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"Success"
    }),200
    
if __name__ == "__main__":
    app.run