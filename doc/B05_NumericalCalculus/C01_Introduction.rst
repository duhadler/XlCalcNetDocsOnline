

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />




|newpage|

Introduction
===============================================================================







Delegates, lambda expressions, callback functions: an example
----------------------------------------------------------------


Returns a local minimum of the function `f` in the interval (a, b), implementing Brent's algorithm. 


See also:  Wikipedia :cite:p:`WikipediaAlg28`,  :cite:t:`Zhang2011`,  :cite:t:`Brent1973`


x is the approximate minimum abscissa, fx=f(x). eps and t define a tolerance tol =eps*|x|+t. f is never evaluated for 2 points closer together than tol. eps shall  not be less than 2*eps_x, preferably not smaller than sqrt(eps_x). ic is the  iteration count, -1 if a=b, 0 if max. count = 5000 exceeded. The algorithm combines golden section search and successive parabolic  interpolation using only function (not derivative) evaluations. 



**Parameters:**

:f:   the function for which a local  minimum is to be found.

:a:   left border of the interval `(a, b)`.

:b:   right border of the interval (a, b).

:eps:   defines a tolerance tol = `\epsilon|x|+` t.

:tol:   defines a tolerance tol = `\epsilon|x|+` t.



**Results:**

:x:     the approximate minimum abscissae.

:fx:     fx = f(x).

:ic:     the iteration count, -1 if a=b, 0 if max. count = 5000 exceeded.



Usage in Python
----------------------------------------------------------------


The routine in Python, using a local function definition. This form allows monitoring of the calls into the function (by un-commenting the ``print`` statement), but variables and functions local to the calling function cannot be accessed:

.. code-block:: pycon

    >>> from xlcalcnet import xreal
    >>> a = -10.0; b = 20.0; eps = 1E-8; tol = 1E-8
    >>> f = lambda x: -xreal.Exp(-x * x)
    >>> res = xreal.LocalMin(f, a, b, eps, tol)
    >>> print('res: (x0, fx0, ic1):', res)



The same routine in Python, using a local function definition. This form allows monitoring of the calls into the function (by un-commenting the ``print`` statement). Variables and functions local to the calling function can be accessed:

.. code-block:: pycon

    a = -10.0; b = 20.0; eps = 1E-8; tol = 1E-8
    f = lambda x: -xreal.Exp(-x * x)
    print('xreal.LocalMin')
    res3 = xreal.LocalMin(f, a, b, eps, tol)
    print('res3: (x0, fx0, ic1):', res3)
    print()
    print()


The same routine in Python, using a lambda expression. Variables and functions local to the calling function can be accessed:

.. code-block:: pycon

    a = -10.0; b = 20.0; eps = 1E-8; tol = 1E-8
    f = lambda x: -xreal.Exp(-x * x)
    print('xreal.LocalMin')
    res3 = xreal.LocalMin(f, a, b, eps, tol)
    print('res3: (x0, fx0, ic1):', res3)
    print()
    print()


The same routine in Python, inserting the lambda expression into ``xreal.LocalMin``. Variables and functions local to the calling function can be accessed from within the lambda expression:

.. code-block:: pycon

    a = -10.0; b = 20.0; eps = 1E-8; tol = 1E-8
    f = lambda x: -xreal.Exp(-x * x)
    print('xreal.LocalMin')
    res3 = xreal.LocalMin(lambda x: -xreal.Exp(-x * x), a, b, eps, tol)
    print('res3: (x0, fx0, ic1):', res3)
    print()
    print()





Usage in CSharp
----------------------------------------------------------------


The same routine in CSharp, using a callback function definition outside of the scope of the calling function. This form allows the callback function to be called from other functions as well, and it supports monitoring of the calls into the function (by un-commenting the ``Console.WriteLine`` statement), but variables, functions and subroutines local to the calling function cannot be accessed:


.. code-block:: csharp

    public static xreal XF1(xreal x)
    {
        var y = -xreal.Exp(-x * x);
        //Console.WriteLine("x: {0},   y: {1}", x, y)
        return y;
    }

    public static void DemoLocalMin()
    {
        var a = -10; var b = 20; var eps = 1E-10; var tol = 1E-10;
        var Res1 = xreal.LocalMin(XF1, a, b, eps, tol);
        Console.WriteLine("Res1:(x, fx, ic) {0}", Res1);
    }


The same routine in CSharp, using a multi-line lambda expression to define the callback function. Note that in contrast to Python, in CSharp a lambda expression can contain not only expressions but also statements, including a ``return`` statement. This is functionally equivalent to defining a local function without the need to create a new class. Variables, functions and subroutines local to the calling function can be accessed from within the lambda expression. The function which is defined by the lambda expression can be called locally. In this form the lambda expression allows monitoring of the calls into the callback function (by un-commenting the ``Console.WriteLine`` statement):

.. code-block:: csharp

    public static void DemoLocalMin2()
    {
        var a = -10; var b = 20; var eps = 1E-10; var tol = 1E-10;
        var F2 = xreal (xreal x) =>
        {
            var y = -xreal.Exp(-x * x);
            //Console.WriteLine("x: {0},   y: {1}", x, y)
            return y;
        };
        var Res1 = xreal.LocalMin(F2, a, b, eps, tol);
        Console.WriteLine("Res1:(x, fx, ic) {0}", Res1);
    }


The same routine in CSharp, using a single-line lambda expression to define the callback function. Note that there is no ``return`` statement, and the return type of the function is not specified but inferred from the function expression. Variables, functions and subroutines local to the calling function can be accessed from within the lambda expression. The function which is defined by the lambda expression can be called locally. Monitoring of calls into the callback function is not supported:

.. code-block:: csharp

    public static void DemoLocalMin3()
    {
        var a = -10; var b = 20; var eps = 1E-10; var tol = 1E-10;
        var F3 = (xreal x) => -xreal.Exp(-x * x);
        var Res1 = xreal.LocalMin(F3, a, b, eps, tol);
        Console.WriteLine("Res1:(x, fx, ic) {0}", Res1);
    }


The same routine in CSharp, using an anonymous lambda expression, which is like a single line lambda expression inserted directly into ``xreal.LocalMin``. Variables and functions local to the calling function can be accessed from within the lambda expression. Since an anonymous lambda expression does not have a name, it cannot be called locally. Monitoring of calls into the callback function is not supported:

.. code-block:: csharp

    public static void DemoLocalMin4()
    {
        var a = -10; var b = 20; var eps = 1E-10; var tol = 1E-10;
        var Res1 = xreal.LocalMin((xreal x) => -xreal.Exp(-x * x), a, b, eps, tol);
        Console.WriteLine("Res1:(x, fx, ic) {0}", Res1);
    }



All of the above CSharp routines produce the following output:

.. code-block:: none

    Res1:(x, fx, ic) (-1.0001755541428017160E-10, -1.0000000000000000000, 14)







