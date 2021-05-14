from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    readme_text = readme_file.read()


setup_args = dict(
    name='parallelizer',
    version='0.1',
    description="Parallel execution of your tasks simplified! Analog to concurrent.futures executors",
    keywords=['executor', 'thread', 'process', 'parallel', 'multiprocessing', 'multithreading'],
    long_description=readme_text,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    author="Leo Ertuna",
    author_email="leo.ertuna@gmail.com",
    url="https://github.com/jpleorx/parallelizer",
    download_url='https://pypi.org/project/parallelizer/'
)


install_requires = [
    'simplestr'
]


if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
