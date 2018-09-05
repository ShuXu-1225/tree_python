def application(environ, start_response):
    start_response('200 ok', [('Content-type', 'text/html')])

    # return [b'<h1>Hello and Hi, python and wsgiref</h1>',
    #         b'<a href=\'http://www.baidu.com\' target=\'_blank\'>baidu</a>']

    body = '<h1>Hello, %s !</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
