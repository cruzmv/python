#https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-python
#python -m pip install --upgrade pip
#pip install --upgrade google-cloud-bigquery

import json
import os

from uuid import uuid4
from flask import Flask, jsonify, request
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "d:/git/python/googleBQuery/database-140419-be91503d4137.json"

class WebService():
    def __init__(self):
        self.query = ""

    def pesq_onys_xhb(self):
        client = bigquery.Client()

        query = (
            "SELECT ID,RAZAO FROM `database-140419.onys_erp.onys_xhb`"
        )

        query_job = client.query(query,location="US")

        ret = []
        for row in query_job:
            r = {
                "id" : row._xxx_values[0],
                "razao" : row._xxx_values[1]
            }
            ret.append(r)
            #print(row)
        return ret

    def ola_mundo(self):
        return ["Olá Mundo!"]


app = Flask(__name__)
node_identifier = str(uuid4()).replace('-','.')
webService = WebService()

@app.route('/pesq', methods=['GET'])
def pesq():
    sql = webService.pesq_onys_xhb()
    return jsonify(sql), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
