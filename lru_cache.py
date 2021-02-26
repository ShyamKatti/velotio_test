from collections import OrderedDict


class MyLRUCache(object):
    def __init__(self, cache_capacity):
        if cache_capacity is None:
            raise ValueError("cache_capacity should be a number")
        self.__cache_capacity = cache_capacity
        self.__ord_dict = OrderedDict()

    def get(self, search_key):
        if search_key in self.__ord_dict:
            self.__ord_dict.move_to_end(search_key, last=False)
            return self.__ord_dict.get(search_key)
        else:
            return -1


    def set(self, key, value):
        if key in self.__ord_dict:
            self.__ord_dict[key] = value
        elif len(self.__ord_dict) == self.__cache_capacity:
            self.__ord_dict.popitem(last=True)
            self.__ord_dict[key] = value
        else:
            self.__ord_dict[key] = value

    def __repr__(self):
        return repr(self.__ord_dict)

    __slots__ = (
        "__cache_capacity",
        "__ord_dict"
    )


if __name__ == "__main__":
    lru_cache = MyLRUCache(3)
    lru_cache.set(1, 'test1')
    lru_cache.set(2, 'test2')
    lru_cache.set(3, 'test3')
    print(lru_cache)
    print(lru_cache.get(3))
    print(lru_cache)
    lru_cache.set(4, 'test4')
    print(lru_cache)

