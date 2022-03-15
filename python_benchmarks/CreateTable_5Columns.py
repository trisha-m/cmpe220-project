'''
REQUIRED: have Cassandra DB already running
pip install cassandra-driver (https://docs.datastax.com/en/developer/python-driver/3.25/)

(This is run from the parent directory, so
"python_benchmarks.AbstractBenchmark"
is required instead of "AbstractBenchmark")
'''
from python_benchmarks.AbstractBenchmark import AbstractBenchmark
from cassandra.cluster import Cluster


class CreateTable_5Columns(AbstractBenchmark):

    def __init__(self):
        self.category = 'Read'
        self.description = 'This is an example'

    def setupQuery(self):
        print('Connecting to cassandra...')
        cluster = Cluster()
        self.session = cluster.connect()

        self.session.execute("CREATE KEYSPACE cmpe220KS WITH replication={'class':'SimpleStrategy','replication_factor':1}")
        self.session.execute("USE cmpe220KS")

    def endQuery(self):
        # print('Closing...')
        # Delete keyspace (also deletes table)
        self.session.execute("DROP KEYSPACE cmpe220KS")

    def runQuery(self):
        self.session.execute('CREATE TABLE fivecolumns(col1 TEXT PRIMARY KEY, col2 TEXT, col3 TEXT, col4 TEXT, col5 TEXT)')
