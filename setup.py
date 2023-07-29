from setuptools import setup
from pathlib import Path


# Version number
directory = Path(__file__).absolute().parent
with open(directory / "sparqldataframe/__init__.py") as f:
    for line in f:
        if "__version__" in line:
            version = line.split("=")[1].strip().strip('"').strip("'")
            continue

# The text of the README file
with open(directory / "README.md") as f:
    README = f.read()

# Requirements
try:
    with open((directory / 'requirements.txt'), encoding='utf-8') as f:
        requirements = f.readlines()
    requirements = [line.strip() for line in requirements]
except FileNotFoundError:
    requirements = []

# This call to setup() does all the work
setup(
    name="sparqldataframe",
    version=version,
    description="Get a Pandas dataframe from SPARQL queries",
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/njanakiev/sparqldataframe",
    author="Nikolai Janakiev",
    author_email="nikolai.janakiev@gmail.com",
    license="MIT",
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    platforms='any',
    packages=['sparqldataframe'],
    include_package_data=True,
    install_requires=["pandas", "requests", "simplejson"],
)
