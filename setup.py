from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(

    name='organizer-cli',
    version='0.0.3',
    description='A CLI tool that scans through a directory and sorts all ungrouped files into folders by file type.',
    url="https://github.com/Mulaza/File-Organizer",
    author="Mulaza Jacinto",
    author_email='mulazajacinto@Gmail.com',
    py_modules=['main'],
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7'
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['Click', 'colorama', 'progress'],

    entry_points=""" 
        [console_scripts] 
        Organize=main:main
        """

)
