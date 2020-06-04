from setuptools import setup

setup(name='pycture',
      version='0.1',
      description='A test graphic application',
      url='https://github.com/da070116/pycture',
      author='AD',
      author_email='ad@example.com',
      license='MIT',
      dependency_links=['http://cs.mipt.ru/python/extra/lab3/graph.py'],
      install_requires=['graph', 'tk'],
      packages=['pycture'],
      zip_safe=False)
