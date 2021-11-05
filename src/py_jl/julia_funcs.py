from pathlib import Path
from julia.api import Julia
jl = Julia(compiled_modules=False)
from julia import Main, Pkg

p = Path(__file__).parent / "julia_funcs.jl"
Pkg.activate(str(p.parent.parent))
Main.include(str(p))

def hello():
    return Main.hello()

def double(n):
    """
    Return the number n doubled.
    Args:
        n: the number you want to double
    """
    return n*2