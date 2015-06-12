#Mould
Yet another static site generator.
this is inspired by [jekyllrb](http://jekyllrb.com).
Mould is written in python. it's still in beta. so there might be few errors.
check the code on [Github](https://github.com/zeroth/mould)

> Static site generator is a software that takes some text + templates as 
input and produces html files on the output.


    |------|   |-----------|   |-------------|
    | text | + | templates | = | .html files |
    |------|   |-----------|   |-------------|


mould is written in python,
currently moudl uses 
- [Markdown](https://en.wikipedia.org/wiki/Markdown): for text to html
- [Jinja2](http://jinja.pocoo.org/docs/dev/): to render templates

It has plugin architecture in place so one can add different functionalities. 
for now only new actions can be added as plugins.

Actions are the main argument to the mould, like build and new.

how to use:

1. get mould

    git clone https://github.com/zeroth/mould.git
    cd mould
    pip install -r requirements.txt
    cd ..

2. create new structure
    
    `python mould/main.py new` `<dir_name>`

3. generate site

    `cd` `<dir_name>`
    `python ../mould/main.py build`


what's inside new <dir_name>

    |-- assets
    |   |-- apple-touch-icon-144-precomposed.png
    |   |-- css
    |   |   |-- mould_style.css
    |   |-- favicon.ico
    |-- config.json
    |-- index.html
    |-- _layouts
    |   |-- _includes
    |   |   |-- head.html
    |   |   |-- sidebar.html
    |   |-- default.html
    |   |-- page.html
    |   |-- post.html
    |   |-- post_list.html
    |-- _posts
        |-- welcome.md

###require template files
index.html
page.html
post.html
post_list.html

where

    -index.html
        root index file its the home page of the site
    - page.html 
        is use to render single page
    - post.html
        is use to render single post
    - post_list.html
        is use to render the list of post on the blog home page

