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
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/''' +\
                        '''bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo''' +\
                        '''8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" ''' +\
                        '''crossorigin="anonymous">
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
        return '''<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/''' +\
                        '''bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo''' +\
                        '''8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" ''' +\
                        '''crossorigin="anonymous">
                        <title>it's title</title>
                      </head>
                      <body>
                        <h1>{}!</h1>
                        <h2>Истощённые ресурсы</h2>
                        <blockquote class="blockquote text-center">
                          <h2 class="mb-0 blockquote font-weight-bold">В основном безвредна</h2>
                          <footer class="blockquote-footer">Дуглас Адамс, <cite>
                          Автостопом по галактике</cite></footer>
                        </blockquote>
                        <h2>Это <i>близко</i></h2>
                       </body>
                    </html>'''.format(planet_name)

    elif planet_name_lower in PLANETS:
        return '''<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/''' +\
                        '''bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo''' +\
                        '''8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" ''' +\
                        '''crossorigin="anonymous">
                <h1 class="p-3 mb-2 bg-primary text-white">{}?</h1>
                <h2 class="shadow-lg p-3 mb-5 bg-white rounded">Представляет интерес!</h2>
                <h2>Имеет историю открытия,</h2>
                <h2>Имеет потенциал.</h2>'''.format(planet_name)
    elif planet_name_lower == 'плутон':
        return f'''<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/''' +\
                        '''bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo''' +\
                        '''8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" ''' +\
                        '''crossorigin="anonymous">
                <h1 class='ml-3'>{}?</h1>
                <h2 class="ml-5">Это</h2>
                <h2 class="text-danger ml-5">не</h2>
                <h2 class="text-monospace ml-5">планета.</h2>'''.format(planet_name)
    else:
        return '''<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/''' +\
                        '''bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo''' +\
                        '''8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" ''' +\
                        '''crossorigin="anonymous">
                        <title>it's title</title>
                      </head>
                      <body>
                        <h1>{}? Неожиданный выбор!</h1>
                        <h2>Изученна хуже Земли</h2>
                        <p class="font-italic text-right">Далеко расположенна.....</p>
                        <p class="p-3 mb-2 bg-warning text-dark">Вам не дадут грант на её изучение</p>
                      </body>
                    </html>'''.format(planet_name)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return '''<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/''' +\
                        '''bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo''' +\
                        '''8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" ''' +\
                        '''crossorigin="anonymous">
                        <title>it's title</title>
                      </head>
                      <body>
                        <h1 class="p-3 bg-dark text-white">Здравствуйте, {}!</h1>
                        <h2 class="text-info">Ваш этап отбора: {}.</h2>
                        <h2 class="text-info">Ваш рейтинг: {}.</h2>
                        <h3 class="d-inline m-1 bg-primary text-white">Желаем удачи!</h2>
                      </body>
                    </html>'''.format(nickname, level, rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
