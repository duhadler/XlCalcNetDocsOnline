

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}





|newpage|




Mpmath: Rootfinding and optimization
====================================================================================




.. _rst_mpm_findroot: 

General root-finding interface
-------------------------------------------------------------------------------

.. method:: ctx.findroot(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Find a solution to `f(x) = 0`, using *x0* as starting point or interval for *x*.



    Multidimensional overdetermined systems are supported.
    You can specify them using a function or a list of functions.

    If the found root does not satisfy `|f(x)|^2 \leq \mathrm{tol}`,
    an exception is raised (this can be disabled with *verify=False*).

    **Arguments**

    *f*
        one dimensional function
    *x0*
        starting point, several starting points or interval (depends on solver)
    *tol*
        the returned solution has an error smaller than this
    *verbose*
        print additional information for each iteration if true
    *verify*
        verify the solution and raise a ValueError if `|f(x)|^2 > \mathrm{tol}`
    *solver*
        a generator for *f* and *x0* returning approximative solution and error
    *maxsteps*
        after how many steps the solver will cancel
    *df*
        first derivative of *f* (used by some solvers)
    *d2f*
        second derivative of *f* (used by some solvers)
    *multidimensional*
        force multidimensional solving
    *J*
        Jacobian matrix of *f* (used by multidimensional solvers)
    *norm*
        used vector norm (used by multidimensional solvers)

    solver has to be callable with ``(f, x0, **kwargs)`` and return an generator
    yielding pairs of approximative solution and estimated error (which is
    expected to be positive).
    You can use the following string aliases:
    'secant', 'mnewton', 'halley', 'muller', 'illinois', 'pegasus', 'anderson',
    'ridder', 'anewton', 'bisect'





Bisection algorithm
---------------------------------------------------------------------------------

.. method:: ctx.bisection(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Find a solution to `f(x) = 0`, using *x0* as starting point or interval for *x*.

    1d-solver generating pairs of approximative root and error. See also: Wikipedia :cite:p:`WikipediaAlg24`.

    Uses bisection method to find a root of f in [a, b].
    Might fail for multiple roots (needs sign change).

    Pro:

    * robust and reliable

    Contra:

    * converges slowly
    * needs sign change




Secant algorithm
---------------------------------------------------------------------------------

.. method:: ctx.secant(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Find a solution to `f(x) = 0`, using *x0* as starting point or interval for *x*.


        1d-solver generating pairs of approximative root and error. See also: Wikipedia :cite:p:`WikipediaAlg21`.

        Needs starting points x0 and x1 close to the root.
        x1 defaults to x0 + 0.25.

        Pro:

        * converges fast

        Contra:

        * converges slowly for multiple roots

    
    The function :func:`~mpmath.findroot` locates a root of a given function using the
    secant method by default. A simple example use of the secant method is to
    compute `\pi` as the root of `\sin x` closest to `x_0 = 3`:

    .. code-block:: pycon

        >>> from mpmath import *
        >>> mp.dps = 30; mp.pretty = True
        >>> findroot(sin, 3)
        3.14159265358979323846264338328

    The secant method can be used to find complex roots of analytic functions,
    although it must in that case generally be given a nonreal starting value
    (or else it will never leave the real line):

    .. code-block:: pycon

        >>> mp.dps = 15
        >>> findroot(lambda x: x**3 + 2*x + 1, j)
        (0.226698825758202 + 1.46771150871022j)

    A nice application is to compute nontrivial roots of the Riemann zeta
    function with many digits (good initial values are needed for convergence):

    .. code-block:: pycon

        >>> mp.dps = 30
        >>> findroot(zeta, 0.5+14j)
        (0.5 + 14.1347251417346937904572519836j)

    The secant method can also be used as an optimization algorithm, by passing
    it a derivative of a function. The following example locates the positive
    minimum of the gamma function:

    .. code-block:: pycon

        >>> mp.dps = 20
        >>> findroot(lambda x: diff(gamma, x), 1)
        1.4616321449683623413










Illinois, Pegasus, Anderson algorithms
---------------------------------------------------------------------------------

.. method:: ctx.illinois(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Find a solution to `f(x) = 0`, using *x0* as starting point or interval for *x*.


    1d-solver generating pairs of approximative root and error. See also: Wikipedia :cite:p:`WikipediaAlg25`,  :cite:t:`Dowell1972`,  Wikipedia :cite:p:`WikipediaAlg26`.

    Uses Illinois method or similar to find a root of f in [a, b].
    Might fail for multiple roots (needs sign change).
    Combines bisect with secant (improved regula falsi).

    The only difference between the methods is the scaling factor m, which is
    used to ensure convergence (you can choose one using the 'method' keyword):

    Illinois method ('illinois'):
        m = 0.5

    Pegasus method ('pegasus'):
        m = fb/(fb + fz)

    Anderson-Bjoerk method ('anderson'):
        m = 1 - fz/fb if positive else 0.5

    Pro:

    * converges very fast

    Contra:

    * has problems with multiple roots
    * needs sign change



    **Intersection methods**

    When you need to find a root in a known interval, it's highly recommended to
    use an intersection-based solver like ``'anderson'`` or ``'ridder'``.
    Usually they converge faster and more reliable. They have however problems
    with multiple roots and usually need a sign change to find a root:

    .. code-block:: pycon

        >>> findroot(lambda x: x**3, (-1, 1), solver='anderson')
        0.0

    Be careful with symmetric functions:

    .. code-block:: pycon

        >>> findroot(lambda x: x**2, (-1, 1), solver='anderson') #doctest:+ELLIPSIS
        Traceback (most recent call last):
            ...
        ZeroDivisionError

    It fails even for better starting points, because there is no sign change:

    .. code-block:: pycon

        >>> findroot(lambda x: x**2, (-1, .5), solver='anderson')
        Traceback (most recent call last):
            ...
        ValueError: Could not find root within given tolerance. (1.0 > 2.16840434497100886801e-19)
        Try another starting point or tweak arguments.








Muller algorithm
---------------------------------------------------------------------------------

.. method:: ctx.muller(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Find a solution to `f(x) = 0`, using *x0* as starting point or interval for *x*.

    1d-solver generating pairs of approximative root and error. See also: Wikipedia :cite:p:`WikipediaAlg23`.

    Needs starting points x0, x1 and x2 close to the root.
    x1 defaults to x0 + 0.25; x2 to x1 + 0.25.
    Uses Muller's method that converges towards complex roots.

    Pro:

    * converges fast (somewhat faster than secant)
    * can find complex roots

    Contra:

    * converges slowly for multiple roots
    * may have complex values for real starting points and real roots



    **Complex roots**

    For complex roots it's recommended to use Muller's method as it converges
    even for real starting points very fast:

    .. code-block:: pycon

        >>> findroot(lambda x: x**4 + x + 1, (0, 1, 2), solver='muller')
        (0.727136084491197 + 0.934099289460529j)








Ridder algorithm
---------------------------------------------------------------------------------

.. method:: ctx.ridder(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Find a solution to `f(x) = 0`, using *x0* as starting point or interval for *x*.

    1d-solver generating pairs of approximative root and error. See also: Wikipedia :cite:p:`WikipediaAlg27`.

    Ridders' method to find a root of f in [a, b].
    Is told to perform as well as Brent's method (see Wikipedia :cite:p:`WikipediaAlg28`) while being simpler.

    Pro:

    * very fast
    * simpler than Brent's method

    Contra:

    * two function evaluations per step
    * has problems with multiple roots
    * needs sign change



    Finally, a useful application is to compute inverse functions, such as the
    Lambert W function which is the inverse of `w e^w`, given the first
    term of the solution's asymptotic expansion as the initial value. In basic
    cases, this gives identical results to mpmath's built-in ``lambertw``
    function:

    .. code-block:: pycon

        >>> def lambert(x):
        ...     return findroot(lambda w: w*exp(w) - x, log(1+x))
        ...
        >>> mp.dps = 15
        >>> lambert(1); lambertw(1)
        0.567143290409784
        0.567143290409784
        >>> lambert(1000); lambert(1000)
        5.2496028524016
        5.2496028524016










Brent algorithm (to be implemented from Scipy brent)
---------------------------------------------------------------------------------

.. method:: ctx.brent(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Find a solution to `f(x) = 0`, using *x0* as starting point or interval for *x*.



    



Newton algorithm
---------------------------------------------------------------------------------

.. method:: ctx.newton_c(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    1d-solver generating pairs of approximative root and error. See also Wikipedia :cite:p:`WikipediaAlg20`, MathWorld :cite:p:`WolframAlg20`.

    Needs starting points x0 close to the root.

    Pro:

    * converges fast
    * sometimes more robust than secant with bad second starting point

    Contra:

    * converges slowly for multiple roots
    * needs first derivative
    * 2 function evaluations per iteration

    **Multiple roots**


    For multiple roots all methods of the Newtonian family (including secant)
    converge slowly. Consider this example:

    .. code-block:: pycon

        >>> f = lambda x: (x - 1)**99
        >>> findroot(f, 0.9, verify=False)
        0.918073542444929

    Even for a very close starting point the secant method converges very
    slowly. Use ``verbose=True`` to illustrate this.






Newton-Steffenson algorithm (ANewton)
---------------------------------------------------------------------------------

.. method:: ctx.newton_steffenson_c(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.



    EXPERIMENTAL 1d-solver generating pairs of approximative root and error.

    Uses Newton's method modified to use Steffensens method when convergence is
    slow. (I.e. for multiple roots.)


    Steffensen's method for quadratic convergence of a linear converging sequence. See also Wikipedia :cite:p:`WikipediaAlg29`.
    Don not use it for higher rates of convergence.
    It may even work for divergent sequences.

    Definition:
    F(x) = (x*f(f(x)) - f(x)**2) / (f(f(x)) - 2*f(x) + x)


    **Multiple roots**


    For multiple roots all methods of the Newtonian family (including secant)
    converge slowly. Consider this example:

    .. code-block:: pycon

        >>> f = lambda x: (x - 1)**99
        >>> findroot(f, 0.9, verify=False)
        0.918073542444929

    Even for a very close starting point the secant method converges very
    slowly. Use ``verbose=True`` to illustrate this.


    Alternatively you can use an experimental Newtonian solver that keeps track
    of the speed of convergence and accelerates it using Steffensen's method if
    necessary:

    .. code-block:: pycon

        >>> findroot(f, -10, solver='anewton', verbose=True)
        x:     -9.88888888888888888889
        error: 0.111111111111111111111
        converging slowly
        x:     -9.77890011223344556678
        error: 0.10998877665544332211
        converging slowly
        x:     -9.67002233332199662166
        error: 0.108877778911448945119
        converging slowly
        accelerating convergence
        x:     -9.5622443299551077669
        error: 0.107778003366888854764
        converging slowly
        x:     0.99999999999999999214
        error: 10.562244329955107759
        x:     1.0
        error: 7.8598304758094664213e-18
        ZeroDivisionError: canceled with x = 1.0
        1.0









Modified Newton algorithm (MNewton)
---------------------------------------------------------------------------------

.. method:: ctx.mnewton_c(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    1d-solver generating pairs of approximative root and error. See also: Wikipedia :cite:p:`WikipediaAlg20`.

    Needs starting point x0 close to the root.
    Uses modified Newton's method that converges fast regardless of the
    multiplicity of the root.

    Pro:

    * converges fast for multiple roots

    Contra:

    * needs first and second derivative of f
    * 3 function evaluations per iteration



    **Multiple roots**


    For multiple roots all methods of the Newtonian family (including secant)
    converge slowly. Consider this example:

    .. code-block:: pycon

        >>> f = lambda x: (x - 1)**99
        >>> findroot(f, 0.9, verify=False)
        0.918073542444929

    Even for a very close starting point the secant method converges very
    slowly. Use ``verbose=True`` to illustrate this.

    It is possible to modify Newton's method to make it converge regardless of
    the root's multiplicity:

    .. code-block:: pycon

        >>> findroot(f, -10, solver='mnewton')
        1.0






Halley algorithm
---------------------------------------------------------------------------------

.. method:: ctx.halley_c(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    1d-solver generating pairs of approximative root and error. See also: Wikipedia :cite:p:`WikipediaAlg22`, MathWorld :cite:p:`WolframAlg22`.

    Needs a starting point x0 close to the root.
    Uses Halley's method with cubic convergence rate.

    Pro:

    * converges even faster the Newton's method
    * useful when computing with *many* digits

    Contra:

    * needs first and second derivative of f
    * 3 function evaluations per iteration
    * converges slowly for multiple roots







Roots of a vector function (MDNewton, to be implemented)
---------------------------------------------------------------------------------

.. method:: ctx.md_newton_c(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.



    Find the root of a vector function numerically using Newton's method.

    f is a vector function representing a nonlinear equation system.

    x0 is the starting point close to the root.

    J is a function returning the Jacobian matrix for a point.

    Supports overdetermined systems.

    Use the 'norm' keyword to specify which norm to use. Defaults to max-norm.
    The function to calculate the Jacobian matrix can be given using the
    keyword 'J'. Otherwise it will be calculated numerically.

    Please note that this method converges only locally. Especially for high-
    dimensional systems it is not trivial to find a good starting point being
    close enough to the root.


    Multidimensional functions are also supported:

    .. code-block:: pycon

        >>> f = [lambda x1, x2: x1**2 + x2,
        ...      lambda x1, x2: 5*x1**2 - 3*x1 + 2*x2 - 3]
        >>> findroot(f, (0, 0))
        [-0.618033988749895]
        [-0.381966011250105]
        >>> findroot(f, (10, 10))
        [ 1.61803398874989]
        [-2.61803398874989]

    You can verify this by solving the system manually.

    Please note that the following (more general) syntax also works:

    .. code-block:: pycon

        >>> def f(x1, x2):
        ...     return x1**2 + x2, 5*x1**2 - 3*x1 + 2*x2 - 3
        ...
        >>> findroot(f, (0, 0))
        [-0.618033988749895]
        [-0.381966011250105]








    See also: https://numerary.readthedocs.io/en/latest/newton-method.html

    See also: https://en.wikipedia.org/wiki/Newton%27s_method#Systems_of_equations

    See also powel hybrid method

    See also: https://github.com/mateuv/MetodosNumericos/blob/master/python/NumericalMethodsInEngineeringWithPython/goldSearch.py

    See also: https://github.com/mateuv/MetodosNumericos/blob/master/python/NumericalMethodsInEngineeringWithPython/powell.py







Levenberg-Marquardt algorithm
---------------------------------------------------------------------------------

.. method:: ctx.levenberg_marquardt_c(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.



    See also: https://lmfit.github.io/lmfit-py/

    See also: https://github.com/lmfit/lmfit-py/tree/master





BFGS algorithm.
---------------------------------------------------------------------------------

.. method:: ctx.bfgs_c(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    See also: https://medium.com/@tru11631/bfgs-and-l-bfgs-with-code-2fcaeee7b225





L-BFGS algorithm.
---------------------------------------------------------------------------------

.. method:: ctx.lbfgs_c(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    See also: https://medium.com/@tru11631/bfgs-and-l-bfgs-with-code-2fcaeee7b225






Conjugate gradient.
---------------------------------------------------------------------------------

.. method:: ctx.conj_grad_c(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.



    See also: https://gregorygundersen.com/blog/2022/03/20/conjugate-gradient-descent/



    See also: https://indrag49.github.io/Numerical-Optimization/conjugate-gradient-methods-1.html


    See also: https://indrag49.github.io/Numerical-Optimization/conjugate-gradient-methods-1.html#nonlinear-conjugate-gradient-algorithm


    See also: https://en.wikipedia.org/wiki/Nonlinear_conjugate_gradient_method









