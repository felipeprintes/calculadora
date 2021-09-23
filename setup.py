import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='calculadora',
    version='0.0.1',
    author='Anderson Printes',
    author_email='felipeprintes@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/felipeprintes/calculadora',
    project_urls = {
        "Bug Tracker": "https://github.com/felipeprintes/calculadora/issues"
    },
    license='MIT',
    packages=['calculadora'],
    #install_requires=['requests'],
)