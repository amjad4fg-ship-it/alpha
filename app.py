from flask import Flask, render_template, abort

app = Flask(__name__)

# قائمة الألعاب - هنا تضيف أي لعبة جديدة
GAMES = {
    "gta5": {"title": "Grand Theft Auto V", "size": "75 GB", "link": "https://gofile.io/d/1zaSuN"},
    "minecraft": {"title": "Minecraft Mobile", "size": "500 MB", "link": "https://t.me/asoloyt6/259"}
}

@app.route('/')
def home():
    return render_template('index.html', games=GAMES)

@app.route('/game/<game_id>')
def game_page(game_id):
    game = GAMES.get(game_id)
    if not game:
        abort(404)
    return render_template('game.html', game=game)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
