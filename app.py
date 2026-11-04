from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/category')
def category():
    return render_template('category.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')






if __name__ == '__main__':
    # debug=True: автоматичний перезапуск після змін у коді та детальні повідомлення про помилки.
    # Використовується лише під час розробки.
    app.run(debug=True, use_reloader=False)
