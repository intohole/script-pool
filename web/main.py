#!/usr/bin/env python
# coding:utf-8

import web

urls = (
    '/', 'Login',
    '/index.html', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')


class Index:

    def GET(self):
        return render.index(name='xx' , check = False)


class Login:
    login = web.form.Form(
        web.form.Textbox('username'),
        web.form.Password('password'),
        web.form.Button('login')
    )

    def GET(self):
        form = self.login()
        return render.testform(form)

    def POST(self):
        form = self.login()
        if not form.validates():
            return render.testform(form)
        if form.d.username == 'admin' and form.d.password == 'admin':
            raise web.seeother('/')
        else:
            raise web.seeother('/index.html')


if __name__ == "__main__":
    app.run()

#render = web
