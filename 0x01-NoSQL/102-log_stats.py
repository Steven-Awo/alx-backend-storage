#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient

if __name__ == "__main__":
    """ Providing just some of the stats about the
    Nginx logs that were stored in the MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    nt_logs = nginx_collection.count_documents({})
    print(f'{nt_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for methodd in methods:
        count = nginx_collection.count_documents({"method": methodd})
        print(f'\tmethod {methodd}: {count}')

    status_checkk = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_checkk} status check')

    topp_ips = nginx_collection.aggregate([
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
    for topp_ip in topp_ips:
        ip = topp_ip.get("ip")
        count = topp_ip.get("count")
        print(f'\t{ip}: {count}')
