from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Scripts for the essay classification'
LONG_DESCRIPTION = 'My first Python package, scripts for the essay classification. Just for demonstration and testing, no actual support will be done in the future'

setup(
        name="src", 
        version=VERSION,
        author="Matheus Henrique Cajueiro Tobias de Souza",
        author_email="1MHCTDS8@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["matplotlib.pyplot","numpy","pandas","seaborn","sklearn","tqdm","nltk"],
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)