from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def title():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def motto():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    agitation = ['Даёшь новые горизонты!',
                 'Даёшь уменьшение риска вымирания человечества!',
                 'Даёшь колонизацию Марса!']
    return '</br>'.join(agitation)


@app.route('/image_mars')
def image():
    return """<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{}" alt="*картинка*">
                    <h2>Марс</h2>
                  </body>
                </html>""".format(url_for('static', filename='img/spirit.png'))


@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    </br>
                    <img src="{url_for('static', filename='img/spirit.png')}" alt="*картинка*">
                    <ul class="list-group">
                    <li class="list-group-item">Даёшь новые горизонты!</li>
                    <li class="list-group-item">Даёшь уменьшение риска вымирания человечества!</li>
                    <li class="list-group-item">Даёшь колонизацию Марса!</li>
                    </ul>
                    </br>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def apply():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="ru">
                              <head>
                                <meta charset="utf-8">
                                <title>it's title</title>
                              </head>
                              <body>
                                <h1>Запишись добровольцем!</h1>
                                <form method="post">
                                    <label for='surname'>Фамилия</label>
                                    <input type="text" id='surname'>
                                    <br>
                                    <label for='name'>Имя</label>
                                    <input type="text" id='name'>
                                    <br>
                                    <label for='email'>Почта</label>
                                    <input type='email' id='email'>
                                    <br>
                                    <label for="education">Образование</label>
                                    <select id="education">
                                      <option>есть</option>
                                      <option>нет</option>
                                    </select>
                                    <br>
                                    <label>Профессия</label>
                                    <br>
                                      <input type="radio" name="profession" id="researcher" checked>
                                      <label for="researcher">Исследователь</label>
                                      <br>
                                      <input type="radio" name="profession" id="sapper">
                                      <label for="sapper">Сапёр</label>
                                      <br>
                                      <input type="radio" name="profession" id="rover">
                                      <label for="rover">Ровер</label>
                                    <br>
                                    <label>Пол</label>
                                    <br>
                                      <input type="radio" name="gender" id="male" value="male" checked>
                                      <label for="male">Мужской</label>
                                      <br>
                                      <input type="radio" name="gender" id="female">
                                      <label for="female">Женский</label>
                                      <br>
                                      <input type="radio" name="gender" id="other">
                                      <label for="other">Другое</label>
                                    <br>
                                    <label>Мотивация</label><br>
                                    <textarea></textarea>
                                    <br>
                                    <input type="checkbox"><label>Хотите на Марс?</label>
                                    <br>
                                    <button type="submit">Записаться</button>
                                </form>
                                <h2>Спасибо за участие!</h2>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        return '<h2>Спасибо за участие!</h2>'


@app.route('/choice/<planet_name>')
def choice(planet_name):
    PLANETS = 'Меркурий, Венера, Земля, Марс, Юпитер, Сатурн, Уран, Нептун'.lower().split(', ')
    planet_name_lower = planet_name.lower()
    if planet_name_lower == PLANETS[2]:
        return f'''<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.
                        com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha38
                        4-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf2
                        3Q9Ifjh" crossorigin="anonymous">
                        <title>it's title</title>
                      </head>
                      <body>
                        <h1>{planet_name}!</h1>
                        <h2>Истощённые ресурсы</h2>
                        <blockquote>
                          <h2 class="blockquote">В основном безвредна</h2>
                          <footer class="blockquote-footer">Дуглас Адамс, <cite>
                          Автостопом по галактике</cite></footer>
                        </blockquote>
                        <h2>Это близко</h2>
                       </body>
                    </html>'''

    elif planet_name_lower in PLANETS:
        return f'''<h1>{planet_name}?</h1>
                <h2>Представляет интерес!</h2>
                <h2>Имеет историю открытия,</h2>
                <h2>Имеет потенциал.</h2>'''
    elif planet_name_lower == 'плутон':
        return f'''<h1>{planet_name}?</h1>
                <h2>Это</h2>
                <h2>не</h2>
                <h2>планета.</h2>'''
    else:
        return f'''<h1>{planet_name}? Неожиданный выбор!</h1>
                <h2>Изученна хуже Земли</h2>
                <h2>Далеко расположенна</h2>
                <h2>Вам не дадут грант на её изучение</h2>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
