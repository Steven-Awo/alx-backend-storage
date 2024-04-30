#!/usr/bin/env python3
""" Using the mongoDB's operations with actual
Python by using pymongo """


def schools_by_topic(mongo_collection, topic):
    """ ReturnING the actual list of all the schools
    having a specific topic """
    documentts = mongo_collection.find({"topics": topic})
    listt_docss = [a for a in documentts]
    return listt_docss
