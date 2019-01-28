from setuptools import setup


setup(
        author='Rohan Banerjee',
        author_email='banerjee.rohan98@gmail.com',
        name='error101',
        description='Python package for a cli tool for seamless debugging on the go.',
        url='https://github.com/rohanbanerjee/solverror',
        license='MIT',
        packages=['error101'],
        install_requires=[
            'bs4', 'requests',
            ],
        entry_points={
            'console_scripts': [
                'error101=error101:main',
                ]
            },
)