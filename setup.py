
from setuptools import setup, find_packages

classifiers = [
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

setup(name="vinyl_mysql",
      version="0.1.0",
      author="Vitalii Abetkin",
      author_email="abvit89s@gmail.ru",
      packages=find_packages(),
      description="vinyl_mysql (backend)",
      long_description='vinyl_mysql (backend)',
      license="MIT",
      classifiers=classifiers)
