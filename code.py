import web

urls = (
    '/', 'index',
    '/movie/(\d+)', 'movie',
    '/cast/(.*)', 'cast',
    '/director/(.*)', 'director',
)

db = web.database(dbn='sqlite', db='MovieSite.db')

render = web.template.render('templates/')

class index:
    def GET(self):
        movies = db.select('movie')
        return render.index(movies)

    def POST(self):
        data = web.input()
        condition = r'title like "%' + data.title + r'%"'
        movies = db.select('movie', where=condition)
        return render.index(movies)

class movie:
    def GET(self, movie_id):
        movie_id = int(movie_id)
        movie = db.select('movie', where='id=$movie_id', vars=locals())[0]
        return render.movie(movie)

class cast:
    def GET(self, cast_name):
        condition = r'casts like "%' + cast_name + r'%"'
        movies = db.select('movie', where=condition)
        return render.index(movies)

class director:
    def GET(self, director_name):
        condition = r'directors like "%' + director_name + r'%"'
        movies = db.select('movie', where=condition)
        return render.index(movies)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

