from setuptools import setup

setup(
    name='autotraffic',
    version='0.0.1',
    description='A Python package that provides you with up-to-date information about all German highways (Autobahn)',
    py_modules=["autotraffic"],
    package_dir={'':'src'},
)

classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "License :: OSI Approved :: MIT License",
    "Development Status :: 3 - Alpha"
]