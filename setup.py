from setuptools import setup, find_packages

setup(
    name='debuggt-personal-web-browser',  # Replace with your package name
    version='0.1',  # Initial release version
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Define command line scripts here, if any
        ],
    },
    # Additional metadata
    author='RAsheed Ali Phiri',  
    author_email='shidahaliphiri@gmail.com',  
    description='A secure Python-based web application designed for showcasing personal portfolios, featuring controlled access to content.',  # Replace with a description
    license='MIT',  # Choose an appropriate license
)
