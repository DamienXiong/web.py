import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return 'Hello, world!'

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

#在命令行运行python code.py会输出http://0.0.0.0:8080/，firefox浏览器无法打开此地址，
#运行python code.py 127.0.0.1,然后访问http://127.0.0.1:8080/