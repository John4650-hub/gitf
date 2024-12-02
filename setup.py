from setuptools import setup, find_packages

setup(
    name="gitf",  # Name of your package
    version="1.0.2",  # Package version
    description="A utility program to use to modify a single file from you github repository",  # Short description
    author="John Delvin",  # Author name,
    author_email="johndelvin51@gmail.com",  # Author email
    url="https://github.com/john4650-hub/gitf",  # URL to your project (e.g., GitHub repo)
    packages=find_packages(),  # Automatically find and include all packages
    entry_points={
        'console_scripts': [
            'gitf=gitf.main:main',
        ]},
    install_requires=[  # List of dependencies your project needs
        "requests"
    ],
    python_requires=">=3.5"  # Minimum Python version required
)
