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
from flask import Flask, render_template, url_for, session, request, redirect
from controller import spoDAO

# spo is a instance of flask,
# template_folder is a directory of contents html sources from view
# static_folder is a static contents like a css, js, etc...
spo = Flask(__name__, template_folder="templates", static_folder="static")
# key of access for wsgi
# use if necessary, we are running spo in a local daemon
# but u can use spo as server, if u don't want use a mod_proxy
# on apache for example, use this key for wsgi
spo.secret_key = 'ˆˆß∂……å¬ßøøøø∑ßˆˆß∆˚¬˜˜≤'

#instance of data access object
dao = spoDAO.SpoDAO()

#for timeout session on 2 minutes
@spo.before_request
def make_session_permanent():
    session.permanent = True
    spo.permanent_session_lifetime = timedelta(minutes=2)

#for logout
@spo.route("/exit")
def exit():
    session.pop('user', None)
    return redirect(url_for("login"))

#errors
@spo.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@spo.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403
@spo.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500



"""
+-------------------------------------------------+
|                                                 |
|                 Login screen                    |
|                                                 |
+-------------------------------------------------+
Function that is responsible for managing login and 
user creation for the first access by opening the cookie 
session and dealing with sqli attacks ex: a ' or 1 = 1#
"""
@spo.route("/", methods=['GET','POST'])
def login():
    #on first access redirect to firstLogin.html
    if dao.testFirstAccess() == True:

        if request.method == 'POST':
            #recive user from html
            getUser = request.form.get('user')
            #recive password from html
            getPasswd = str(request.form.get('password'))
            #insert in to DB
            dao.insertUser(getUser,getPasswd)

            return render_template("firstLogin.html")
    else:
        if request.method == 'POST':
            # recive user from html
            getUser = request.form.get('user')
            # recive password from html
            getPasswd = str(request.form.get('password'))

            #test login
            if dao.testLogin(getUser,getPasswd) == True:
                return redirect('dashboard')
            else:
                return render_template("passwordFail.html")

        #render login.html
        return render_template("login.html")

"""
+-------------------------------------------------+
|                                                 |
|                 User Dashboard                  |
|                                                 |
+-------------------------------------------------+
Function that is responsible for principal page
"""
@spo.route("/dashboard", methods=['GET','POST'])
def dashboard():



    return render_template("dashboard.html")

"""
+-------------------------------------------------+
|                                                 |
|                 Investigation                   |
|                                                 |
+-------------------------------------------------+
Function that is responsible for start a new investigation.
"""
@spo.route("/investigation")
def investigation():
    return render_template("investigation.html")

"""
+-------------------------------------------------+
|                                                 |
|                 Search Servers                  |
|                                                 |
+-------------------------------------------------+
Function that is responsible for search a servers and services.
Here we'll use the shodan key and others tools for search,
and crawlers and etc.. 
"""
@spo.route("/searchServers")
def searchServers():
    return render_template("searchServers.html")

"""
+-------------------------------------------------+
|                                                 |
|                Personal Trace                   |
|                                                 |
+-------------------------------------------------+
Function that is responsible for search a person, on facebook
instagram, twitter and whatever public data allow on internet 
about especific people.
"""
@spo.route("/personalTrace")
def personalTrace():
    return render_template("personalTrace.html")

"""
+-------------------------------------------------+
|                                                 |
|                   About OSINT                   |
|                                                 |
+-------------------------------------------------+
Function about educational articles
"""
@spo.route("/aboutOSINT")
def aboutOSINT():
    return render_template("aboutOSINT.html")

"""
+-------------------------------------------------+
|                                                 |
|                    Manual                       |
|                                                 |
+-------------------------------------------------+
Function for help
"""
@spo.route("/manual")
def manual():
    return render_template("manual.html")


"""
+-------------------------------------------------+
|                                                 |
|                Insert Keys                      |
|                                                 |
+-------------------------------------------------+
Function that is responsible for insert a credentials
for social media when we using for search on crawlers
"""
@spo.route("/insertKeys")
def insertKeys():
    return render_template("insertKeys.html")



"""
+-------------------------------------------------+
|                                                 |
|                   About US                      |
|                                                 |
+-------------------------------------------------+
The best function on this software, because here is
a bitcoin wallet ♥ ♥ ♥ ♥ uheuheuheu 
"""
@spo.route("/about")
def aboutUS():
    return render_template("aboutus.html")

"""
+-------------------------------------------------+
|                                                 |
|                   Run SPO                       |
|                                                 |
+-------------------------------------------------+
Function that is responsible for start SPO, on documentation
is describled how to configure a daemon spod and execute.
We disponibilizing a web service for SPO, send-me a email
for talk about this!
"""
if __name__ == '__main__':
    # spo run in 1337 port tcp
    # For real use disallow debug mode, set False
    spo.run(port=1337, debug=True)
    __author__='Victor de Queiroz'

