

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />


|newpage|

Boost/Math: Root Finding and Minimization Algorithms
===============================================================================



Root Finding Without Derivatives (TOM 748 algorithm)
-------------------------------------------------------------------------------

.. method:: ctxboost.BracketRoot(f, guess, factor, is_rising, get_digits, maxit)

    where ``ctx`` is ``ctxboost``.

    :param f: the function for which a root is determined.
    :param guess: an intial guess.
    :param factor: a multiplication factor used when searching for the bracket.
    :param is_rising: an indicator whether the function is rising.
    :param get_digits: the targeted number of accurate digits.
    :param maxit: the  maximal number of iterations.

    :returns: a tuple (*root, error, iter*), where *root* is  an approximation to a root of the function *f*, using the TOM 748 algorithm for finding a zero; *error* is an estimate of the modulus of the error of the approximation; and *iter* is the actual number of iterations.


    See also:  BoostMath :cite:p:`BoostAlg26`, :cite:t:`Alefeld1995`.





    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> f = lambda x: x * x * x - 28
        >>> guess = 2.33;  factor = 2.0; is_rising = True; get_digits = 64;  maxit = 20
        >>> res = ereal.BracketRoot(f, guess, factor, is_rising, get_digits, maxit)
        >>> print("res (x0, error, iter): ", res)





    .. code-block:: none

        boost.bracket_root(f, guess, factor, is_rising, get_digits, maxit
        result:  3.036588971875662








|newpage|


Root Finding With Derivatives: Newton-Raphson
-------------------------------------------------------------------------------

.. method:: ctxboost.NewtonRaphson(f, df, guess, xmin, xmax, get_digits, maxit)

    where ``ctx`` is ``ctxboost``.

    :param f: the function for which a root is determined.
    :param df: the first derivative of the function *f*.
    :param guess: an intial guess.
    :param xmin: the left border of the search interval.
    :param xmax: the right border of the search interval.
    :param get_digits: the targeted number of accurate digits.
    :param maxit: the  maximal number of iterations.

    :returns: a tuple (*root, iter*), where *root* is an approximation to a root of the function *f* in the interval (*xmin, xmax*), using the Newton algorithm for finding a zero; and *iter* is the actual number of iterations.


    See also:  Wikipedia :cite:p:`WikipediaAlg20`,  BoostMath :cite:p:`BoostAlg20`, MathWorld :cite:p:`WolframAlg20`.





    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> f = lambda x: x * x * x - 28
        >>> df1 = lambda x: 3 * x * x
        >>> guess = 2.33; xmin = 1.0; xmax = 4.0; get_digits = 64;  maxit = 20
        >>> result3 = ereal.NewtonRaphson(f, df1, guess, xmin, xmax, get_digits, maxit)
        >>> print("res2 (x0, iter): ", result3)




    .. code-block:: none

        boost.newton_raphson(f, df, guess, xmin, xmax, get_digits, maxit)
        result:  3.0365889718756627






|newpage|


Root Finding With Derivatives: Halley
-------------------------------------------------------------------------------


.. method:: ctxboost.Halley(f, df, d2f, guess, xmin, xmax, get_digits, maxit)

    where ``ctx`` is ``ctxboost``.

    :param f: the function for which a root is determined.
    :param df: the first derivative of the function *f*.
    :param df2: the second derivative of the function *f*.
    :param guess: an intial guess.
    :param xmin: the left border of the search interval.
    :param xmax: the right border of the search interval.
    :param get_digits: the targeted number of accurate digits.
    :param maxit: the  maximal number of iterations.

    :returns: a tuple (*root, iter*), where *root* is an approximation to a root of the function *f* in the interval (*xmin, xmax*), using the Halley algorithm for finding a zero; and *iter* is the actual number of iterations.


    See also:  Wikipedia :cite:p:`WikipediaAlg22`,  BoostMath :cite:p:`BoostAlg20`, MathWorld :cite:p:`WolframAlg22`.





    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> f = lambda x: x * x * x - 28
        >>> df1 = lambda x: 3 * x * x
        >>> df2 = lambda x: 6 * x
        >>> guess = 2.33; xmin = 1.0; xmax = 4.0; get_digits = 64;  maxit = 20
        >>> res = ereal.Halley(f, df1, df2, guess, xmin, xmax, get_digits, maxit)
        >>> print("res (x0, iter): ", res)





    .. code-block:: none

        boost.halley(f, df, df2, guess, xmin, xmax, get_digits, maxit)
        result:  3.0365889718756627






|newpage|


Root Finding With Derivatives: Schröder
-------------------------------------------------------------------------------

.. method:: ctxboost.Schroeder(f, df, d2f, guess, xmin, xmax, get_digits, maxit)

    where ``ctx`` is ``ctxboost``.

    :param f: the function for which a root is determined.
    :param df: the first derivative of the function *f*.
    :param df2: the second derivative of the function *f*.
    :param guess: an intial guess.
    :param xmin: the left border of the search interval.
    :param xmax: the right border of the search interval.
    :param get_digits: the targeted number of accurate digits.
    :param maxit: the  maximal number of iterations.

    :returns: a tuple (*root, iter*), where *root* is an approximation to a root of the function *f* in the interval (*xmin, xmax*), using the Schröder algorithm for finding a zero; and *iter* is the actual number of iterations.

    See also:  BoostMath :cite:p:`BoostAlg20`, MathWorld :cite:p:`WolframAlg23`, :cite:t:`Schröder1870`.




    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> f = lambda x: x * x * x - 28
        >>> df1 = lambda x: 3 * x * x
        >>> df2 = lambda x: 6 * x
        >>> guess = 2.33; xmin = 1.0; xmax = 4.0; get_digits = 64;  maxit = 20
        >>> res = ereal.Schroeder(f, df1, df2, guess, xmin, xmax, get_digits, maxit)
        >>> print("res (x0, iter): ", res)





    .. code-block:: none

        boost.schroder(f, df, df2, guess, xmin, xmax, get_digits, maxit)
        result:  3.0365889718756627






|newpage|


Locating Function Minima using Brent's algorithm
-------------------------------------------------------------------------------

.. method:: ctx.BrentMinimum(f, a, b, get_digits, maxit)

    where ``ctx`` is ``ctxboost``.

    :param f: the function for which a local minimum is determined.
    :param a: the left border of the search interval.
    :param b: the right border of the search interval.
    :param get_digits: the targeted number of accurate digits.
    :param maxit: the  maximal number of iterations.

    :returns: a tuple (*localmin, fx0, iter*), where *localmin* is  an approximation to a local minimum of the function f in the interval (*a,b*), using Brent's algorithm; *fx0* is  the value of *f(localmin)*; and *iter* is the  number of iterations.


    See also:  Wikipedia :cite:p:`WikipediaAlg28`, :cite:t:`Zhang2011`, :cite:t:`Brent1973`,  BoostMath :cite:p:`BoostAlg28`.






    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> f = lambda x: (x + 3) * (x - 1) * (x - 1)
        >>> bracket_min = 0.5; bracket_max = 1.5;  bits = 125;  maxit = 20
        >>> res = ereal.Brent_Minimum(f, bracket_min, bracket_max, bits, maxit)
        >>> print("res5 (x0, fx0, iter): ", result3)




    .. code-block:: none

        boost.brent_minimum(f3, a, b, get_digits, maxit)
        x0:  2.9086877250246185e-09





