# -*- coding:UTF-8 -*-
__author__ = 'Victor de Queiroz'
"""
        
             ██████  ██▓███   ▒█████  
           ▒██    ▒ ▓██░  ██▒▒██▒  ██▒
           ░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒
             ▒   ██▒▒██▄█▓▒ ▒▒██   ██░
           ▒██████▒▒▒██▒ ░  ░░ ████▓▒░
           ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░ 
           ░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░ 
           ░  ░  ░  ░░       ░ ░ ░ ▒  
                 ░               ░ ░
                   
        S n e a k    P e e k   O S I N T
        
SPO is a software for search OSINT content.
SPO is a opensource code, please don't use this with
other license different than GPLv2.

Developed by Victor de Queiroz
Contact: victordequeiroz37@gmail.com

+------------- ♥ For donations ♥ -----------------+
|                                                 |
| ŁTC = LPE5DsjA2YcMuGGZspvRzEEvdoAjvTRzvF        |
| ɃTC = 1FtBj9QbT7gDcxSCygTnUop4N3bd75bwRZ        |
| ɃCH = qr6gn0r20p9s9kjm5yuvqw53mhmzx87q0vecqn6xhj|
|                                                 |
+-------------------------------------------------+


"""
from datetime import timedelta
from flask import Flask, render_template, url_for, session, request


# spo is a instance of flask,
# template_folder is a directory of contents html sources from view
# static_folder is a static contents like a css, js, etc...
spo = Flask(__name__, template_folder="templates", static_folder="static")
# key of access for wsgi
# use if necessary, we are running spo in a local daemon
# but u can use spo as server, if u don't want use a mod_proxy
# on apache for example, use this key for wsgi
spo.secret_key = 'ˆˆß∂……å¬ßøøøø∑ßˆˆß∆˚¬˜˜≤'

#for timeout session on 2 minutes
@spo.before_request
def make_session_permanent():
    session.permanent = True
    spo.permanent_session_lifetime = timedelta(minutes=2)




"""
+-------------------------------------------------+
|                                                 |
|                 Login screen                    |
|                                                 |
+-------------------------------------------------+

"""
@spo.route("/", methods=['GET','POST'])
def login():



    return render_template("login.html")

"""
+-------------------------------------------------+
|                                                 |
|                 User Dashboard                  |
|                                                 |
+-------------------------------------------------+

"""
@spo.route("/dashboard", methods=['GET','POST'])
def dashboard():



    return render_template("dashboard.html")


"""
+-------------------------------------------------+
|                                                 |
|                   About US                      |
|                                                 |
+-------------------------------------------------+

"""
@spo.route("/about", methods=['GET','POST'])
def aboutUS():



    return render_template("aboutus.html")

"""
+-------------------------------------------------+
|                                                 |
|                   Run SPO                       |
|                                                 |
+-------------------------------------------------+

"""
if __name__ == '__main__':
    # spo run in 1337 port tcp
    # For real use disallow debug mode, set False
    spo.run(port=1337, debug=True)
    __author__='Victor de Queiroz'

