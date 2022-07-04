# Date Posted : 18 Oct 2021

These were, loosely, the different sections in [PEP-484](https://www.python.org/dev/peps/pep-0484/), the original introduction to TypeHints for Python3.5:

0) History - POST 2-1✔️
1) Introduction , Acceptable type hints - POST 2-1✔️
2) Type aliases, Callable - POST 2-1✔️
3) Generics, User-defined generic types - POST 2-1✔️
4) Scoping rules for type variables
5) Instantiating generic classes and type erasure
6) Arbitrary generic types as base classes
7) Abstract generic types
8) Type variables with an upper bound
9) Covariance and contravariance
10) The numeric tower
11) Forward references
12) Union types
13) Support for singleton types in unions
14) The Any type
15) The NoReturn type
16) The type of class objects
17) Annotating instance and class methods
18) Version and platform checking
19) Runtime or type checking?
20) Arbitrary argument lists and default argument values
21) Positional-only arguments
22) Annotating generator functions and coroutines
23) Compatibility with other uses of function annotations
24) Casts
25) NewType helper function
26) Stub Files
27) Function/method overloading
28) Storing and distributing stub files
29) The Typeshed Repo
30) The typing Module

This code repo accompanies the blog post explaining some of these sections.

Try out stuff as mypy would interpret it at - https://mypy-play.net/?mypy=latest&python=3.10
