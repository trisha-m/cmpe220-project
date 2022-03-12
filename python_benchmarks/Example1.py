'''
REQUIRED: have Cassandra DB already running
pip install cassandra-driver (https://docs.datastax.com/en/developer/python-driver/3.25/)

(This is run from the parent directory, so
"python_benchmarks.AbstractBenchmark"
is required instead of "AbstractBenchmark")
'''
from python_benchmarks.AbstractBenchmark import AbstractBenchmark
from cassandra.cluster import Cluster


class Example1(AbstractBenchmark):

    def __init__(self):
        self.category = 'Read'
        self.description = 'This is an example'

    def setupQuery(self):
        print('Connecting to cassandra...')
        cluster = Cluster()
        self.session = cluster.connect()

    def endQuery(self):
        print('Closing...')
        self.session.close()

    def runQuery(self):
        result = self.session.execute(
            'SELECT release_version FROM system.local')
        print(result.one())
