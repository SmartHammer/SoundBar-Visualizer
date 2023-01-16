# This Python file uses the following encoding: utf-8


def singleton(class_):
    instances = {}

    def getInstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getInstance
