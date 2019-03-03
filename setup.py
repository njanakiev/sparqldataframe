from setuptools import find_packages, setup
import os.path


# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.rst")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="sparqldataframe",
    version="0.1.0",
    description="Get a Pandas dataframe from SPARQL queries",
    long_description=README,
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
    install_requires=["pandas", "requests"],
)
