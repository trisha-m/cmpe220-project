package com.cmpe220.benchmark;

abstract public class AbstractBenchmark {

    protected String category;
    protected String description;

    /**
    * Operations before the actual query
    * such as connection, initializations, etc.
    */
    protected void setupQuery() {

    }

    /**
    * Operations after the query
    */
    protected void endQuery() {

    }

    /**
    * Run the query to benchmark
    * Make sure that the query is synchronous!
    */
    abstract protected void runQuery();

    /**
    * @return milliseconds that the query took
    */
    public long benchmark() {
        setupQuery();

        long startTime = System.currentTimeMillis();
        runQuery();
        long endTime = System.currentTimeMillis();

        endQuery();
        return endTime - startTime;
    }

    public String getCategory() {
        return category;
    }

    public String getDescription() {
        return description;
    }
}
