#!/usr/bin/env python3
"""All the log stats thats from the collection
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """ A script that helps provides some of the stats
    thats about Nginx logs tthat are stored in MongoDB
    """
    itemms = {}
    if option:
        valuee = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {valuee}")
        return

    resultt = mongo_collection.count_documents(itemms)
    print(f"{resultt} logs")
    print("Methods:")
    for methodd in METHODS:
        log_stats(nginx_collection, methodd)
    statuss_checkk = mongo_collection.count_documents({"path": "/status"})
    print(f"{statuss_checkk} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
