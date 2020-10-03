from setuptools import setup


setup(

    # mandatory
    name='Organizer',
    # mandatory
    version='0.1',
    # mandatory
    author_email='mulaza@Gmail.com',
    install_requires=['Click'],
    py_modules=['File-Organizer'],
    entry_points="""
        [console_scripts] 
        Organizer=main:main
        """

)
