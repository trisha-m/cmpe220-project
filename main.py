import jpype
import jpype.imports
from jpype.types import *
import subprocess
import logging
import argparse
import sys

JAVA_BENCHMARKS_DIR = 'java_benchmarks'
BENCHMARK_JAR_NAME = 'java_benchmarks-1.0-jar-with-dependencies.jar'

logging.basicConfig(
    format='[%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
)

parser = argparse.ArgumentParser(description='CMPE 220 DBMS Benchmarker')
parser.add_argument(
    '--no-java-compile',
    action='store_true',
    default=False,
    help='Skip compiliation of Java benchmarks',
)


def compile_java_benchmarks():
    logging.info('Compiling Java benchmarks...')
    try:
        ret = subprocess.run(
            'mvn package',
            cwd=JAVA_BENCHMARKS_DIR,
            shell=True,
            capture_output=True,
        )
        ret.check_returncode()
        logging.debug(str(ret.stdout))
    except subprocess.CalledProcessError:
        logging.error(str(ret.stderr))
        sys.exit(ret.returncode)


def main():
    args = parser.parse_args()

    # Run all Java benchmarks (in package com.cmpe220.benchmark, in jar)
    if args.no_java_compile is False:
        compile_java_benchmarks()
    jpype.startJVM(classpath=[
        f'{JAVA_BENCHMARKS_DIR}/target/{BENCHMARK_JAR_NAME}',
    ])
    java_benchmarks_object = jpype.JPackage('com.cmpe220.benchmark')
    java_benchmarks_list = list(dir(java_benchmarks_object))
    java_benchmarks_list.remove('AbstractBenchmark')
    for bm in java_benchmarks_list:
        logging.info(f'Running benchmark "{bm}"...')
        try:
            instance = getattr(java_benchmarks_object, bm)()
            time = instance.benchmark()
            logging.info('Time: ' + str(time))
        except Exception as e:
            logging.error(f'Benchmark "{bm}" failed!')
            logging.exception(e)
    jpype.shutdownJVM()

    # Run all Python benchmarks


if __name__ == '__main__':
    main()
