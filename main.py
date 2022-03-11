import jpype
import jpype.imports
from jpype.types import *
import subprocess

JAVA_BENCHMARKS_DIR = 'java_benchmarks'
BENCHMARK_JAR_NAME = 'java_benchmarks-1.0-jar-with-dependencies.jar'


def compile_java_benchmarks():
    print('Compiling Java benchmarks...')
    subprocess.run(
        'mvn package',
        cwd=JAVA_BENCHMARKS_DIR,
        shell=True,
        capture_output=True,
    ).check_returncode()


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
        print(f'Running {bm}...')
        instance = getattr(java_benchmarks_object, bm)()
        print('Time: ' + str(instance.benchmark()))

    jpype.shutdownJVM()


if __name__ == '__main__':
    main()
