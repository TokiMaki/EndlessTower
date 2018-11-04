
# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[],[]]


def add_object(o, layer):
    global objects
    objects[layer].append(o)


def remove_object(o):
    global objects
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o


def clear():
    global objects
    for o in all_objects():
        del o
    objects.clear()
    objects = [[],[]]


def all_objects():
    global objects
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

