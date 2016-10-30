#Exception template

def emptyDict(dict):
    try:
        return "Hello!"
    except bool(dict) is False:
        print "Dict is empty"

emptyDict({})
