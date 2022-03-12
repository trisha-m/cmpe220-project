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

Results are saved to a json file (todo).

See `python main.py --help` for available arguments.

## How to add benchmarks

### Java

Add a new Java file to `java_benchmarks/src/.../benchmark/` that implements the abstract class `AbstractBenchmark.java`. See `Example1.java` for an example.

### Python

Add a new Python file to `python_benchmarks/` that implements the abstract class in `AbstractBenchmark.py`. See `Example1.py` for an example.
