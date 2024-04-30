#!/usr/bin/env python3
""" Using mongoDB's operations with actual
Python using the pymongo """


def list_all(mongo_collection):
    """ Listing all the documents with Python """
    documentts = mongo_collection.find()

    if documentts.count() == 0:
        return []

    return documentts
