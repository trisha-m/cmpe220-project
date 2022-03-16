package com.cmpe220.benchmark;

import com.datastax.oss.driver.api.core.CqlSession;
import com.datastax.oss.driver.api.core.cql.*;

/**
* REQUIRED: have Cassandra DB already running
*/
public class CassandraCreateTable5Columns extends AbstractBenchmark {

    private CqlSession session;

    public CassandraCreateTable5Columns() {
        category = "Read";
        description = "This is an example";
    }

    public void setupQuery() {
        System.out.println("Connecting to cassandra...");
        session = CqlSession.builder().build();

        session.execute(
            "CREATE KEYSPACE cmpe220KS "+
            "WITH replication="+
            "{'class':'SimpleStrategy','replication_factor':1}"
        );
        session.execute("USE cmpe220KS");
    }

    public void endQuery() {
        System.out.println("Closing...");

        session.execute("DROP KEYSPACE cmpe220KS");

        session.close();
    }

    public void runQuery() {
        session.execute(
            "CREATE TABLE fivecolumns("+
            "col1 TEXT PRIMARY KEY,"+
            "col2 TEXT,"+
            "col3 TEXT,"+
            "col4 TEXT,"+
            "col5 TEXT)"
        );
    }
}
