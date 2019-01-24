from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information",
      author="Ivan Wahlrab",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
        }
      )