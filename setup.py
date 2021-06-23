from setuptools import setup, find_packages

setup(
    name='pele_client',
    version='1.0.3',
    long_description='Client for REST API for HySDS Datasets',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    # Note: gdal must be conda installed from conda-forge.
    install_requires=[
        'requests',
    ]
)
