from flask import Flask

from posts.views import posts_blueprint
from api.api import api_blueprint

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# Регистрируем блюпринты
app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def page_not_found(_):
	return "Страница не найдена"


@app.errorhandler(500)
def page_not_found(_):
	return "На сервере что то пошло не так"


if __name__ == "__main__":
    app.run()
