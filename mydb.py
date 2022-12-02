#to perform read & write operations inside the db json file
import json


class Database:
    """this class will be used to perform complete I/O operations in the db.json file
    """
    def check_user_existence(self,name,email,password):
        with open('db.json','r') as rf:
            db=json.load(rf)
        if email in db:
            return 1
        else:
            with open('db.json','w') as wf: 
                db[email]=[name,password]
                json.dump(db,wf)
            return 0
        
    def login_checker(self,email,password):
        with open('db.json','r') as rf:
            db=json.load(rf)
        if email in db:
            if db[email][1]==password:
                return 1
            else:
                return 0
        else:
            return 0