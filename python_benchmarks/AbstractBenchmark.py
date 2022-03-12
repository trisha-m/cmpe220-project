
from abc import ABC, abstractmethod
from time import time_ns


class AbstractBenchmark(ABC):

    def __init__(self):
        self.category = ''
        self.description = ''

    def startQuery(self):
        '''
        Operations before the actual query
        e.g. connection, initializations, etc.
        '''
        pass

    def endQuery(self):
        '''
        Operations after the query
        e.g. cleanup, shutdown, etc.
        '''
        pass

    @abstractmethod
    def runQuery(self):
        '''
        Operations before the actual query
        e.g. connection, initializations, etc.
        '''
        pass

    def benchmark(self):
        '''
        :return: milliseconds that the query took
        '''
        self.setupQuery()

        start_time = time_ns()
        self.runQuery()
        end_time = time_ns()

        return (end_time - start_time) / 1000000


    def getCategory(self):
        return self.category


    def getDescription(self):
        return self.description
