import timeit

py = timeit.timeit('loop_py.run(10000)', setup='import loop_py', number= 100)
cy = timeit.timeit('loop_cy.run(10000)', setup='import loop_cy', number= 100)

print("py:", py, "cy:", cy)
print("cy is {}x times faster.".format(py/cy))