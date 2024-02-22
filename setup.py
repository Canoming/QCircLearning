from setuptools import setup,find_packages

setup(name='QCircLearning',
      version='0.2',
      description='Qiskit based variational circuit',
      url='https://github.com/Canoming/CircTraining',
      author='Canoming',
      author_email='canoming@163.com',
      license='MIT',
      packages=find_packages(exclude=["*.tests","*.tests.*","tests.*","tests"]),
      install_requires=[
          'qiskit >= 0.4.0',
      ],
      zip_safe=False)