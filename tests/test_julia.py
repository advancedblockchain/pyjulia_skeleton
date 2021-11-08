from py_jl.julia_funcs import float_double

def test_double():
    assert float_double(1) == 2
