package com.cmpe220.benchmark;

import com.datastax.oss.driver.api.core.CqlSession;
import com.datastax.oss.driver.api.core.cql.*;

public class Example1 extends AbstractBenchmark {

    private CqlSession session;

    public Example1() {
        category = "Read";
        description = "This is an example";
    }

    public void setupQuery() {
        System.out.println("Connecting to cassandra...");
        session = CqlSession.builder().build();
    }

    public void endQuery() {
        System.out.println("Closing...");
        session.close();
    }

    public void runQuery() {
        ResultSet rs = session.execute("select release_version from system.local");
        Row row = rs.one();
        System.out.println(row.getString("release_version"));
    }
}
