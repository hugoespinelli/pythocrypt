from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pythocrypt',
      version='0.1',
      description='Several ciphers for python',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/hugoespinelli/pythocrypt',
      author='Hugo Espinelli',
      author_email='hugoespinelli@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
      )
