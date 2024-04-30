#!/usr/bin/env python3
""" Using the mongoDB's operations with actual
Python by using pymongo """
from pymongo import MongoClient

if __name__ == "__main__":
    """ Providing just some of the stats about the
    Nginx logs that were stored in the MongoDB """
    clientt = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collections = clientt.logs.nginx

    nt_logs = nginx_collections.count_documents({})
    print(f'{nt_logs} logs')

    methodds = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for methodd in methodds:
        counts = nginx_collections.count_documents({"methdd": methodd})
        print(f'\tmethod {methodd}: {counts}')

    statuss_checkk = nginx_collections.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{statuss_checkk} status check')

    topp_ipss = nginx_collections.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    print("IPs:")
    for topped_ip in topp_ipss:
        ip = topped_ip.get("ip")
        counts = topped_ip.get("count")
        print(f'\t{ip}: {counts}')
