import jpype
import jpype.imports
from jpype.types import *
import subprocess
import logging
import sys

JAVA_BENCHMARKS_DIR = 'java_benchmarks'
BENCHMARK_JAR_NAME = 'java_benchmarks-1.0-jar-with-dependencies.jar'

logging.basicConfig(
    format='[%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
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

    compile_java_benchmarks()

    jpype.startJVM(classpath=[
        f'{JAVA_BENCHMARKS_DIR}/target/{BENCHMARK_JAR_NAME}',
    ])

    # from com.cmpe220.benchmark import Example1
    # print(Example1().benchmark())

    # Run all benchmarks in com.cmpe220.benchmark
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


if __name__ == '__main__':
    main()
