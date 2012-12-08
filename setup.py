from setuptools import setup

classifiers = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Development Status :: 1 - Planning',
    'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
]

setup(name='pypcb',
      version='0.1',
      description='PCB Layout Swiss Army Knife',
      classifiers=classifiers,
      long_description='',
      keywords='pcb eagle cad kicad geda eda',
      url='http://github.com/storborg/pypcb',
      author='Scott Torborg',
      author_email='scott@cartlogic.com',
      install_requires=[
          'lxml',
          # These are for tests.
          'coverage',
          'nose>=1.1',
          'nose-cover3',
      ],
      license='MIT',
      packages=['pypcb'],
      entry_points=dict(console_scripts=[
          'pypcb-read=pypcb.cmd:read_main',
      ]),
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
