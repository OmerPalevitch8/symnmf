from setuptools import Extension, setup

setup(
     name='mysymnmf',
     version='1.0',
     description='Python wrapper for custom C extension',
     ext_modules = [
          Extension(
          'mysymnmf',
               sources=[
               "symnmf.c",
               "symnmfmodule.c"
])])