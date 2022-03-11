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

    from com.cmpe220.benchmark import Example1, Example2

    print(Example1().benchmark())
    # Example2().hello()

    jpype.shutdownJVM()


if __name__ == '__main__':
    main()
