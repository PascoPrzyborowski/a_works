
class A:

    def __init__(self, name, location):
        self._name = name
        self.__location = location

    def get_location(self) -> str:
        return self.__location


if __name__ == '__main__':
    a = A('test', 'Berlin')

    print(a._A__location)
    # SYNTAX: <instance>._<class name>__<class instance variable>