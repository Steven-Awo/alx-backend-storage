#!/usr/bin/env python3
""" Using the mongoDB's operations with actual
Python by using pymongo """


def top_students(mongo_collection):
    """ Returning all of the students that were sorted
    by their average score """

    topp_std = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return topp_std
