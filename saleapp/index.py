from flask import Flask,render_template,request
import dao
app = Flask(__name__)


@app.route('/')
def hello():
    q = request.args.get("q")
    category_id = request.args.get('category_id')
    categories = dao.get_categories()
    products = dao.get_products(q,category_id)
    return render_template("index.html", categories=categories,products=products)


@app.route('/product/<int:id>/')
def detail(id):
    product = dao.get_product_by_id(id)
    return render_template("details.html",product=product)


@app.context_processor
def context_processor():
    return {
        "categories": dao.get_categories()
    }


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)