from setuptools import setup, find_packages

setup(name='btc-python-client',
      version='0.1',
      description='Python client for btc-trade API',
      keywords='',
      url='https://github.com/maxidrum/btc-python-client.git',
      author='Maksym Vyshnevskiy',
      author_email='maxksidrum@gmail.com',
      license='',
      packages=find_packages(),
      install_requires=[
          'requests==2.18.4',
      ],
      )
