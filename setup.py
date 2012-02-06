from setuptools import setup
from setuptools import find_packages

setup(
    name='geoimage',
    version='0.1',
    author='Pratik Hublikar, Kristoffer Snabb',
    url='https://github.com/geonition/django_geoimage',
    packages=find_packages(),
    include_package_data=True,
    package_data = {
        "geoimage": [
            "*.png"
        ],
    },
    zip_safe=False,
    install_requires=['django']
)
