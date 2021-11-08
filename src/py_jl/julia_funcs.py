from pathlib import Path
from julia.api import Julia
jl = Julia(compiled_modules=False)
from julia import Main, Pkg

p = Path(__file__).parent / "julia_funcs.jl"
Pkg.activate(str(p.parent.parent))
Main.include(str(p))

def hello():
    """
    Say hello using Julia.
    """
    return Main.hello()

def float_double(n):
    """
    Return the number n doubled.
    Args:
        n: the number you want to double
    """
    tmp = float(n)
    return Main.float_double(tmp)