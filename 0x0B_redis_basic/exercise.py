#!/usr/bin/env python3
"""Create a Cache class. In the __init__ method,
store an instance of the Redis client as a private
variable named _redis (using redis.Redis()) and
flush the instance using flushdb.

Create a store method that takes a data argument
and returns a string. The method should generate
a random key (e.g. using uuid), store the input
data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data
can be a str, bytes, int or float."""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """takes a single method Callable argument and returns a Callable"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for a particular function"""
    @wraps(method)
    def wrapper(self, *args):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(inputs_key, str(args))
        result = method(*args)
        self._redis.rpush(outputs_key, str(result))
        return result

    return wrapper


class Cache:
    """Cache class"""
    def __init__(self):
        """Init method for cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        key = str(uuid.uuid4)
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """take a key string argument and an optional Callable argument"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> str:
        """get string method"""
        value = self.get(key, str)
        return value

    def get_int(self, key: str) -> int:
        """get int method"""
        value = self.get(key, int)
        return value
