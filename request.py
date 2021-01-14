import requests
import json
import threading
def api_request() :
    response = requests.get("https://covid19.th-stat.com/api/open/timeline")
    data = response.json()
    api_data = data["Data"]
    for i in api_data :
        ##columns = []
        ##values = []
        for k,v in i.items() :
            if k == "Date" :
                Date = v
            if k == "NewConfirmed" :
                NewConfirmed = v
            if k == "NewRecovered" :
                NewRecovered = v
            if k == "NewHospitalized" :
                NewHospitalized = v
            if k == "NewDeaths" :
                NewDeaths = v
            if k == "Confirmed" :
                Confirmed = v
            if k == "Recovered" :
                Recovered = v
            if k == "Hospitalized" :
                Hospitalized = v
            if k == "Deaths" :
                Deaths = v

        columns = ['Date','NewConfirmed','NewRecovered','NewHospitalized','NewDeaths','Confirmed','Recovered','Hospitalized','Deaths']
        values = ["'"+str(Date)+"','"+str(NewConfirmed)+"','"+str(NewRecovered)+"','"+str(NewHospitalized)+"','"+str(NewDeaths)+"','"+str(Confirmed)+"','"+str(Recovered)+"','"+str(Hospitalized)+"','"+str(Deaths)+"'"]
    
      
        column = ','.join('"'+str(c)+'"' for c in columns)
        value = ','.join(v for v in values)
        
        #insert_sql = ' INSERT INTO ' +schema+"."+table+' (' + column +"," + value + ') '   
          
        print(column)
        print(value)
api_request()






    













    ###request n time from api###
    #t = threading.Timer( 300.0, timer_request ) 
    #t.start()
    #print( (data) )
    #############################






