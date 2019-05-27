from pymongo import MongoClient
from flask import Flask


app=Flask(__name__)

def dbMigration():
    #In this script , db1 is the source database and db2 is the target database
    #Connection to the source Database
    client1 = MongoClient(host="sjc-wwdl-pmp1", 
                        port=27017, 
                        username="pmpengg", 
                        password="pmpengg123",
                        authSource="pmpdetails")
    db1 = client1["pmpdetails"]

    #Connection to the target database
    client2 = MongoClient(host="sjc-wwdl-pmp1", 
                        port=27017, 
                        username="qwdevuser", 
                        password="qwdevuser123",
                        authSource="scrmodetails")
    db2 = client2["scrmodetails"]

    #Removing data from target collection
    db2.ProcessCompliance2.remove()

    #Inserting data into target collection from source collection
    for a in db1.ProcessCompliance.find():
        try:
            print(a)
            db2.ProcessCompliance2.insert(a)
        except:
            print('did not copy')            
    #Closing the connections
    client1.close()
    client2.close()

@app.route('/')
def ping():
    return "Flask API for DB migration is up",200

@app.route('/migrate')
def migrate():
    try:
        dbMigration()
    except Exception as e:
        print(str(e))
        return "Error in Migration",500
    
    return "Migration done successfully",200

if __name__ == "__main__":
    app.run(port=5025, host="0.0.0.0", debug=True)