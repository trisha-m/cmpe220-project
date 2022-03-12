# DBMS Performance Evaluation - CMPE 220

Framework to benchmark different DBMS software, drivers, etc. in different scenarios.

## Prerequisites

```
Python3 (3.9.5)
Java (11)
Maven (3.8.3)
```

## How it works

`main.py` runs all the benchmarks in `java_benchmarks/`, `python_benchmarks/`, and ...

Data of results are saved to a .json file and visualizations of data to directory ... (todo).

See `python main.py --help` for available arguments.

## How to add benchmarks

`java_benchmarks`, `python_benchmarks`, and ... have an abstract benchmark class. To add benchmarks, create a new file that implements this abstract class.

Specifically, only abstract function `runQuery()` is required to be implemented. `startQuery()` and `endQuery()` may optionally be implemented.

Ultimately, `main.py` calls function `benchmark()` to run the benchmark which relies on the mentioned functions. I.e. `benchmark()` is implemented as follows in Java:

```
// AbstractBenchmark.java
public long benchmark() {
    setupQuery();

    long startTime = System.currentTimeMillis();
    runQuery();
    long endTime = System.currentTimeMillis();

    endQuery();
    return endTime - startTime;
}
```

Python's, and ...'s implementation of `benchmark()` follow the same logic.

### Adding Java Benchmarks

Add a new Java file to `java_benchmarks/src/.../benchmark/` that implements the abstract class `AbstractBenchmark.java`. See `Example1.java` for an example.

### Adding Python Benchmarks

Add a new Python file to `python_benchmarks/` that implements the abstract class in `AbstractBenchmark.py`. See `Example1.py` for an example.

## Our Results

todo
