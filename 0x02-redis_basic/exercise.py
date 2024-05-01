#!/usr/bin/env python3
"""Redis and Python exercise"""
import uuid
from functools import wraps
from typing import Callable, Union

import redis


def count_calls(method: Callable) -> Callable:
    """the decorator that help takes in a single method
     of a Callable argument and then returns a Callable"""
    keyys = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """This increments the total count for that specific key every time that the method is called and then returns
        the value then returned by the actual original
        method """
        self._redis.incr(keyys)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """This helps in storing the history of all the inputs and
    the outputs for thaats particular function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """saves the input and outputt of each function in redis
        """
        inputed_key = method.__qualname__ + ":inputs"
        outputed_key = method.__qualname__ + ":outputs"

        outputt = method(self, *args, **kwargs)

        self._redis.rpush(inputed_key, str(args))
        self._redis.rpush(outputed_key, str(outputt))

        return outputt

    return wrapper


def replay(fn: Callable):
    """Displaying all the history of all the calls of that
    particular function"""
    rr = redis.Redis()
    fil_name = fn.__qualname__
    numb_calls = rr.get(fil_name)
    try:
        numb_calls = numb_calls.decode('utf-8')
    except Exception:
        numb_calls = 0
    print(f'{fil_name} was called {numb_calls} times:')

    insd = rr.lrange(fil_name + ":inputs", 0, -1)
    outds = rr.lrange(fil_name + ":outputs", 0, -1)

    for a, b in zip(insd, outds):
        try:
            a = a.decode('utf-8')
        except Exception:
            a = ""
        try:
            b = b.decode('utf-8')
        except Exception:
            b = ""

        print(f'{fil_name}(*{a}) -> {b}')


class Cache():
    """A Cache's class thats with redis"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """The storing methods

        Args:
            data (Union[str, bytes, int, float]): Any data can be stored

        Returns:
            str: As string
        """
        keyys = str(uuid.uuid4())
        self._redis.set(keyys, data)
        return keyys

    def get(self, key: str, fn: Callable = None)\
            -> Union[str, bytes, int, float]:
        """ Getting the data from the redis and then transforming
        it into its actual python type """
        datta = self._redis.get(key)
        if fn:
            return fn(datta)
        return datta

    def get_str(self, key: str) -> str:
        """ Transforming the redis type's variablee into an actual
        str of python type """
        variablee = self._redis.get(key)
        return variablee.decode("UTF-8")

    def get_int(self, key: str) -> int:
        """ Transforming the redis type's variablee into an
        actual str of python type"""
        variablee = self._redis.get(key)
        try:
            variablee = int(variablee.decode("UTF-8"))
        except Exception:
            variablee = 0
        return variablee
