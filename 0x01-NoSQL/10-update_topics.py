#!/usr/bin/env python3
""" Using the mongoDB's operations with actual
Python by using pymongo """


def update_topics(mongo_collection, name, topics):
    """ Changing all the topics of a school's document
    thats based on theier name """
    querry = {"name": name}
    newer_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(querry, newer_values)
