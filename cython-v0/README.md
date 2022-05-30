# Links

[cython website](https://cython.readthedocs.io/en/latest/#)
[cython github](https://github.com/cython/cython)
[cython FAQ](https://github.com/cython/cython/wiki/FAQ)
[cpython github](https://github.com/python/cpython)
[pyrex](https://wiki.python.org/moin/Pyrex)

# Run

```
pip3 install cython
python3 setup.py build_ext --inplace
python3 test.py
```
sample output:

```
py: 0.025550199672579765 cy: 6.100162863731384e-06
cy is 4188.445496183206x times faster.
```

# Files

generated files:
* loop_py.c
* loop_cy.c
* loop_cy.cpython-36m-x86_64-linux-gnu.so
* loop_py.cpython-36m-x86_64-linux-gnu.so

source files:
* loop_py.py
* loop_cy.pyx
* setup.py
* test.py

When defining variable type explicitly, it makes the execution faster. We can compare the difference for the generated c code.

