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
        # self.session.close()

    def runQuery(self):
        #self.session.execute('SELECT release_version FROM system.local')
        self.session.execute('CREATE TABLE fivecolumns(col1 TEXT PRIMARY KEY, col2 TEXT, col3 TEXT, col4 TEXT, col5 TEXT)')
        for i in range(0,500):
          self.session.execute("INSERT INTO fivecolumns(col1, col2, col3, col4, col5) VALUES (015219646, 'Trishala',0, 1, 0)")
        # result = self.session.execute(
        #     'SELECT release_version FROM system.local')
        # print(result.one())
