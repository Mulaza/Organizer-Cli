from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(

    name='organizer-cli',
    version='0.0.4',
    description='A Python CLI tool that runs throught a given directory and organizes all un-folder bound files into folders by file extension.',
    url="https://github.com/Mulaza/File-Organizer",
    author="Mulaza Jacinto",
    author_email='mulazajacinto@Gmail.com',
    py_modules=['main'],
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['Click', 'colorama', 'progress'],

    entry_points=""" 
        [console_scripts] 
        Organize=main:main
        """

)
