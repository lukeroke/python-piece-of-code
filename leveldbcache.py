# coding: utf-8
import atexit
import json
import os
import plyvel


@atexit.register
def close():
    DATABASE.close()


def b(obj):
    return obj if type(obj) == bytes else str(obj).encode('utf-8')


def s(b):
    return b.decode('utf-8')


def put(key, value):
    DATABASE.put(b(key), b(json.dumps(value)))


def get(key):
    res = DATABASE.get(b(key))
    return res if res is None else json.loads(s(res))


def _mkdir(newdir):
    """
    works the way a good mkdir should :)
        - already exists, silently complete
        - regular file in the way, raise an exception
        - parent directory(ies) does not exist, make them as well
    """
    if type(newdir) is not str:
        newdir = str(newdir)
    if os.path.isdir(newdir):
        pass
    elif os.path.isfile(newdir):
        raise OSError("a file with the same name as the desired " \
                      "dir, '%s', already exists." % newdir)
    else:
        head, tail = os.path.split(newdir)
        if head and not os.path.isdir(head):
            _mkdir(head)
        if tail:
            os.mkdir(newdir)



DB_PATH = '/tmp/leveldbcache'
_mkdir(DB_PATH)
DATABASE = plyvel.DB(DB_PATH, create_if_missing=True)

# usage:
# >>> from . import leveldbcache
# >>> vec_dict = leveldbcache.get(file)
# >>> if vec_dict is None:
# >>>     vec_dict = {foo:'bar'}
# >>>     leveldbcache.put(file, vec_dict)
# >>> print(vec_dict)










