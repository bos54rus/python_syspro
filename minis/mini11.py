class SingletonMixin:
    con = None

    @classmethod
    def instance(cls):
        if not cls.con:
            cls.con = cls()
        return cls.con

    def __new__(cls, *args, **kwargs):
        if not cls.con:
            cls.con = super().__new__(cls, *args, **kwargs)
        return cls.con


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


class GlobalCounter(SingletonMixin, Counter):
    pass


gc1 = GlobalCounter.instance()
gc2 = GlobalCounter.instance()
print(id(gc1) == id(gc2))
