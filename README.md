How to use this...
==================

    > mkproject {{project_name}}
    > pip install django
    > django-admin.py startproject --template=http://git.io/vgemLQ {{project_name}}

Side note about the url shortening

    curl -i http://git.io -F "url=https://github.com/aaronromeo/basic_django_project_template/archive/master.zip"

    HTTP/1.1 100 Continue
    
    HTTP/1.1 201 Created
    Server: GitHub.com
    Date: Mon, 05 May 2014 02:34:37 GMT
    Content-Type: text/html;charset=utf-8
    Connection: keep-alive
    Status: 201 Created
    Location: http://git.io/vgemLQ
    Content-Length: 78
    X-Runtime: 0.006981
    X-Node: gitio2
    X-Revision: 0ace8fca85ae89568bdd379a963882226b51e21c

    https://github.com/aaronromeo/basic_django_project_template/archive/master.zip%

