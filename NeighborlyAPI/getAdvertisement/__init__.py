import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import logging
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    # example call http://localhost:7071/api/getAdvertisement/?id=5eb6cb8884f10e06dc6a2084

    id = req.params.get('id')
    print("--------------->", id)
    
    if id:
        try:
            url = os.environ["MyDbConnection"]
            client = pymongo.MongoClient(url)
            database = client['course2db']
            collection = database['advertisements']
            
            query = {'_id': id}
            result = collection.find_one(query)
            if not result:
                return func.HttpResponse("Not found", status_code=404)
            print("----------result--------")

            result = dumps(result)
            print(result)
            return func.HttpResponse(dumps(result), mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)
