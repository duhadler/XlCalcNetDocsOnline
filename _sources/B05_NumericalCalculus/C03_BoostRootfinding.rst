

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

        >>> from xlcalcnet import xreal
        >>> f = lambda x: x * x * x - 28
        >>> guess = 2.33;  factor = 2.0; is_rising = True; get_digits = 64;  maxit = 20
        >>> res = xreal.BracketRoot(f, guess, factor, is_rising, get_digits, maxit)
        >>> print("res (x0, error, iter): ", res)



    The same routine in Visual Basic:

    .. code-block:: vbnet

        Function F10 (ByVal x As xreal) As xreal
            Dim fx As New xreal
            fx = x*x*x - 27
            'Console.WriteLine("In F1: x: {0}, f(x): {1}", x, fx)
            Return fx
        End Function

        Sub DemoBracketRoot() 
            Console.WriteLine("BracketRoot")
            Dim guess = 2.33
            Dim factor = 2.0
            Dim is_rising = True
            Dim get_digits = 150
            Dim maxit = 14
            Dim res1  = xreal.BracketRoot(AddressOf F10, guess, factor, is_rising, get_digits, maxit)
            Console.WriteLine("res1 (x0, error, iter): {0}", res1)
        End Sub



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

        >>> from xlcalcnet import xreal
        >>> f = lambda x: x * x * x - 28
        >>> df1 = lambda x: 3 * x * x
        >>> guess = 2.33; xmin = 1.0; xmax = 4.0; get_digits = 64;  maxit = 20
        >>> result3 = xreal.NewtonRaphson(f, df1, guess, xmin, xmax, get_digits, maxit)
        >>> print("res2 (x0, iter): ", result3)



    The same routine in Visual Basic:

    .. code-block:: vbnet

        Function F10 (ByVal x As xreal) As xreal
            Dim fx As New xreal
            fx = x*x*x - 27
            'Console.WriteLine("In F1: x: {0}, f(x): {1}", x, fx)
            Return fx
        End Function

        Function DF10 (ByVal x As xreal) As xreal
            Dim df1x As New xreal
            df1x = 3*x*x
            'Console.WriteLine("In DF1: x: {0}, df1(x): {1}", x, df1x)
            Return df1x
        End Function

        Sub DemoNewtonRaphson() 
            Console.WriteLine("Newton-Raphson")
            Dim guess = 2.33
            Dim xmin = 1.0
            Dim xmax = 4.0
            Dim get_digits = 140
            Dim maxit = 14
            Dim res2  = xreal.NewtonRaphson(AddressOf F10, AddressOf DF10, guess, xmin, xmax, get_digits, maxit)
            Console.WriteLine("res2 (x0, iter): {0}", res2)
            Console.WriteLine()
        End Sub


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

        >>> from xlcalcnet import xreal
        >>> f = lambda x: x * x * x - 28
        >>> df1 = lambda x: 3 * x * x
        >>> df2 = lambda x: 6 * x
        >>> guess = 2.33; xmin = 1.0; xmax = 4.0; get_digits = 64;  maxit = 20
        >>> res = xreal.Halley(f, df1, df2, guess, xmin, xmax, get_digits, maxit)
        >>> print("res (x0, iter): ", res)



    The same routine in Visual Basic:

    .. code-block:: vbnet

        Function F10 (ByVal x As xreal) As xreal
            Dim fx As New xreal
            fx = x*x*x - 27
            'Console.WriteLine("In F1: x: {0}, f(x): {1}", x, fx)
            Return fx
        End Function

        Function DF10 (ByVal x As xreal) As xreal
            Dim df1x As New xreal
            df1x = 3*x*x
            'Console.WriteLine("In DF1: x: {0}, df1(x): {1}", x, df1x)
            Return df1x
        End Function

        Function D2F10 (ByVal x As xreal) As xreal
            Dim df2x As New xreal
            df2x = 6*x
            'Console.WriteLine("In DF2: x: {0}, df2(x): {1}", x, df2x)
            Return df2x
        End Function

        Sub DemoHalley() 
            Console.WriteLine("Halley")
            Dim guess = 2.33
            Dim xmin = 1.0
            Dim xmax = 4.0
            Dim get_digits = 140
            Dim maxit = 14
            Dim res3  = xreal.Halley(AddressOf F10, AddressOf DF10, AddressOf D2F10, _ 
                guess, xmin, xmax, get_digits, maxit)
            Console.WriteLine("res3 (x0, iter): {0}", res3)
            Console.WriteLine()
        End Sub




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

        >>> from xlcalcnet import xreal
        >>> f = lambda x: x * x * x - 28
        >>> df1 = lambda x: 3 * x * x
        >>> df2 = lambda x: 6 * x
        >>> guess = 2.33; xmin = 1.0; xmax = 4.0; get_digits = 64;  maxit = 20
        >>> res = xreal.Schroeder(f, df1, df2, guess, xmin, xmax, get_digits, maxit)
        >>> print("res (x0, iter): ", res)



    The same routine in Visual Basic:

    .. code-block:: vbnet

        Function F10 (ByVal x As xreal) As xreal
            Dim fx As New xreal
            fx = x*x*x - 27
            'Console.WriteLine("In F1: x: {0}, f(x): {1}", x, fx)
            Return fx
        End Function

        Function DF10 (ByVal x As xreal) As xreal
            Dim df1x As New xreal
            df1x = 3*x*x
            'Console.WriteLine("In DF1: x: {0}, df1(x): {1}", x, df1x)
            Return df1x
        End Function

        Function D2F10 (ByVal x As xreal) As xreal
            Dim df2x As New xreal
            df2x = 6*x
            'Console.WriteLine("In DF2: x: {0}, df2(x): {1}", x, df2x)
            Return df2x
        End Function

        Sub DemoSchroeder() 
            Console.WriteLine("Schroeder")
            Dim guess = 2.33
            Dim xmin = 1.0
            Dim xmax = 4.0
            Dim get_digits = 140
            Dim maxit = 14
            Dim res4  = xreal.Schroder(AddressOf F10, AddressOf DF10, AddressOf D2F10, _ 
                guess, xmin, xmax, get_digits, maxit)
            Console.WriteLine("res4 (x0, iter): {0}", res4)
            Console.WriteLine()
        End Sub



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

        >>> from xlcalcnet import xreal
        >>> f = lambda x: (x + 3) * (x - 1) * (x - 1)
        >>> bracket_min = 0.5; bracket_max = 1.5;  bits = 125;  maxit = 20
        >>> res = xreal.Brent_Minimum(f, bracket_min, bracket_max, bits, maxit)
        >>> print("res5 (x0, fx0, iter): ", result3)



    The same routine in Visual Basic:

    .. code-block:: vbnet

        Function F12 (ByVal x As xreal) As xreal
            Dim fx As New xreal
            fx = (x + 3) * (x - 1) * (x - 1)
            'Console.WriteLine("In F2: x: {0}, f(x): {1}", x, fx)
            Return fx
        End Function

        Sub DemoBrentMinimum() 
            Console.WriteLine("Brent_Minimum")
            Dim bracket_min = 0.5
            Dim bracket_max = 1.5
            Dim bits As Int32 = 125
            Dim maxit = 14
            Dim res5 = xreal.Brent_Minimum(AddressOf F12, bracket_min, bracket_max, bits, maxit)
            Console.WriteLine("res5 (x0, fx0, iter): {0}", res5)
            Console.WriteLine()
        End Sub



    .. code-block:: none

        boost.brent_minimum(f3, a, b, get_digits, maxit)
        x0:  2.9086877250246185e-09





