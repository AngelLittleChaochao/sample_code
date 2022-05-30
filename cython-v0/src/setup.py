from setuptools import Extension, setup
from Cython.Build import cythonize


setup(
    ext_modules=cythonize([Extension("loop_cy", ['loop_cy.pyx'])])
    #ext_modules=cythonize([Extension("loop_py", ['loop_py.py'])])
)