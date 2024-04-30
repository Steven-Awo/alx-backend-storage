#!/usr/bin/env python3
""" Using the mongoDB operations with just
Python using just pymongo """


def insert_school(mongo_collection, **kwargs):
    """ Inserting just a new document into a
    collection thaats based on kwargs """
    documentt_id = mongo_collection.insert(kwargs)
    return documentt_id
