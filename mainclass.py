#!/usr/bin/python
import MySQLdb



#Open database connection
db = MySQLdb.connect("localhost", "root", "root", "taskstock")
# prepare a cursor object using cursor() method
cursor = db.cursor()


count=0

def query(query1):

    q1=query1

    try:
        cursor.execute(q1)
        results =cursor.fetchall()
    except:
        print "Unable to fetch data"

    return results
    
   
def validation(k2):

    global count
    us = raw_input("Username::")
    psw1 = raw_input("password::")
    k3=k2
    sql2 = "SELECT username,passw,team from empcred where username=\"%s\";" %us
    results1=query(sql2)
    
    if len(results1) == 0 :

        print "Credentials are wrong.Enter valid credentials"

        count=count+1
        if count != 3:
            
            validation(k2)
        else:
            print "No.of attempts reached 3"
            return None
        

    else:

        re=results1[0]

        if k3 == re[2]:
            if psw1 == re[1]: 
                print "You are from %s team" %k3
                return k3
                
            else:
                print "Credentials are wrong.Enter valid credentials"

                count=count+1
                if count != 3: 
                    validation(k2)
                else:
                    print "No.of attempts reached 3"
                    return None
                
        else:

            print "You are not from %s team" %k3
            return None
    
            




def authenticate():

    
    while(1):
        k1 = raw_input("Are you from sales/purchase:")
        if k1 == "sales":
           k3=validation(k1)
           break
        elif k1 == "purchase":
            k3=validation(k1)
            break
        else:
          print "Please select sales/purchase:"
    return k3

 

class company(object):

    def __init__(self,team):

        self.team1=team;


    def insert(self):
        
        pass

    def update(self):
        pass

    def delete(self):

        
        if self.team1 == "sales":

            modelname = raw_input("Enter model you want to buy::")
            units = raw_input("No.of units you want to purchase::")

            sql1 = "select brand,model,price,retailstock from warehouse where model=\"%s\" and retailstock is NOT NULL ;" %modelname
            result = query(sql1)
            if len(result) == 0:

                print "product not exist. Select correct choice"
                
            else:

                re =result[0]
                if productname in re:
                    if units <= re[3] :

                        print "Thanks for purchasing"
                        sql2  = "select stockcount from warehouse where %s;" %productname

                    else:
                        print "No.of units entered are more than the retail available"
                    
                        
            print result

        else:

            sql1 = "select id,brand,model,price,stockcount from warehouse;"
            result = query(sql1)
            print result

            

    def display(self):

    
        if self.team1 == "sales":

            sql1 = "select brand,model,price,retailstock from warehouse where retailstock is NOT NULL;"
            result = query(sql1)

            for i in result:
                print "Brand=%s Model=%s price=%d units=%d" %(i[0],i[1],int(i[2]),int(i[3]))

        else:

            sql1 = "select id,brand,model,price,stockcount from warehouse;"
            result = query(sql1)
            print result

k2=authenticate()
print k2
c1=company(k2)
c1.display()



    
    
