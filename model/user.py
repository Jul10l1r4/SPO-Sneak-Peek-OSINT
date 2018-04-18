__Author__ = 'Victor de Queiroz'
"""

Class for model users for access and manage SPO

"""

class User(object):

        #set user id
        def setUserID(self,userID):
            self.setUser = userID
        #set user
        def setUser(self,user):
            self.setUser = user
        #set password
        def setPasswd(self,passwd):
            self.setPasswd = passwd


        #get user id
        def getUserID(self):
            return self.userID
        #get user
        def getUser(self):
            return self.user
        #get password
        def getPasswd(self):
            return self.passwd









"""
CREATE TABLE user_spo(
id_user integer PRIMARY KEY AUTO_INCREMENT,
login varchar(100) not null,
password varchar(300) not null,
constraint user_pk primary key(id_user)
);
"""