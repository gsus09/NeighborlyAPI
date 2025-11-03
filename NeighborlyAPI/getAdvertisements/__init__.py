import azure.functions as func
import pymongo
import json
import os
import logging
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = os.environ["MyDbConnection"]
        client = pymongo.MongoClient(url)
        database = client['course2db']
        collection = database['advertisements']

        result = collection.find({})
        logging.info(f"Fetched advertisements: {result}")
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        logging.error("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

