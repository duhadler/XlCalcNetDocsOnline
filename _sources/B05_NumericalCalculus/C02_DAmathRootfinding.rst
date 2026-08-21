

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />




|newpage|

DAMath: Numerical Rootfinding and Minimization
===============================================================================







Quadratic Equation, Real Coefficients
-------------------------------------------------------------------------------

.. method:: ctx.squadx(a, b, c)

    where ``ctx`` is ``math53``. Solves the quadratic equation `a x^2 + b x + c = 0`. 

    :param a: real coeffient in the quadratic equation.
    :param b: real coeffient in the quadratic equation.
    :param c: real coeffient in the quadratic equation.

    :returns: a tuple (*z1, z2*), where *z1* is the first complex root.and  *z2* is the second complex root.

    See also:  Wikipedia :cite:p:`WikipediaAlg02`, MathWorld :cite:p:`WolframAlg02`.




    .. code-block:: pycon

        >>> from xlcalcnet import math53
        >>> a = -13;  b = 4;  c = 5
        >>> ic, x1, y1, x2, y2 = math53.squadx(a,b,c)
        >>> print("ic: ", ic,"x1: ", x1,"y1: ", y1,"x2: ", x2,"y2: ", y2)


    .. code-block:: none

        Quadratic
        Return Code:  2
        x1:  -0.4851249125321596 y1:  0.0 
        x2:  0.7928172202244673 y2:  0.0




|newpage|


Cubic Equation, Real Coefficients
-------------------------------------------------------------------------------


.. method:: ctx.cubsolve(a, b, c, d)

    where ``ctx`` is ``math53``. Solves the cubic equation `a x^3 + b x^2 + c x + d = 0`. 

    :param a: real coeffient in the cubic equation.
    :param b: real coeffient in the cubic equation.
    :param c: real coeffient in the cubic equation.
    :param d: real coeffient in the cubic equation.

    :returns: a tuple (*x, z1, z2*), where *x* is the real root, *z1* is the first complex root and  *z2* is the second complex root.


    See also:  Wikipedia :cite:p:`WikipediaAlg03`, MathWorld :cite:p:`WolframAlg03`.




    .. code-block:: pycon

        >>> from xlcalcnet import math53
        >>> a = -13; b = 4; c = 5; d = 1
        >>> x0, x1, y1, x2, y2 = math53.cubsolve(a,b,c,d)
        >>> print("x0: ", x0,"x1: ", x1,"y1: ", y1,"x2: ", x2,"y2: ", y2)


    .. code-block:: none

        Cubic
        x:  0.8593905490844492 
        x1:  -0.27584912069607076 y1:  -0.11582803026356575 
        x2:  -0.27584912069607076 y2:  0.11582803026356575





|newpage|

Brent's algorithm for finding a local minimum
-------------------------------------------------------------------------------

.. method:: math53.localmin(f, a, b, eps, t)


    where ``ctx`` is ``math53``. Returns a local minimum of the function `f` in the interval (a, b), implementing Brent's algorithm.

    :param f: the function for which a local  minimum is to be found.
    :param a: the left border of the search interval.
    :param b: the right border of the search interval.
    :param eps: defines a tolerance eps*|x| + tol; eps should not be less than 2*eps_x, preferably not smaller than sqrt(eps_x).
    :param tol: defines a tolerance eps*|x| + tol.

    :returns: a tuple (*localmin, fx, ic*), where *localmin* is an approximation to  a local minimum; *fx* = f(localmin); and *ic* is the iteration count, -1 if a=b, 0 if max.=5000 exceeded.


    See also:  Wikipedia :cite:p:`WikipediaAlg28`, :cite:t:`Zhang2011`, :cite:t:`Brent1973`


    x is the approximate minimum abscissa, fx=f(x). eps and t define a tolerance tol =eps*|x|+t. f is never evaluated for 2 points closer together than tol. eps shall  not be less than 2*eps_x, preferably not smaller than sqrt(eps_x). ic is the  iteration count, -1 if a=b, 0 if max. count = 5000 exceeded. The algorithm combines golden section search and successive parabolic  interpolation using only function (not derivative) evaluations. 



    **Examples in Python**

    The routine in Python, using a local function definition. This form allows monitoring of the calls into the function (by un-commenting the ``print`` statement), but variables and functions local to the calling function cannot be accessed:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> a = -10.0; b = 20.0; eps = 1E-8; tol = 1E-8
        >>> f = lambda x: -ereal.Exp(-x * x)
        >>> res = ereal.LocalMin(f, a, b, eps, tol)
        >>> print('res: (x0, fx0, ic1):', res)



    The same routine in Python, using a local function definition. This form allows monitoring of the calls into the function (by un-commenting the ``print`` statement). Variables and functions local to the calling function can be accessed:

    .. code-block:: pycon

        a = -10.0; b = 20.0; eps = 1E-8; tol = 1E-8
        f = lambda x: -ereal.Exp(-x * x)
        print('ereal.LocalMin')
        res3 = ereal.LocalMin(f, a, b, eps, tol)
        print('res3: (x0, fx0, ic1):', res3)
        print()
        print()


    The same routine in Python, using a lambda expression. Variables and functions local to the calling function can be accessed:

    .. code-block:: pycon

        a = -10.0; b = 20.0; eps = 1E-8; tol = 1E-8
        f = lambda x: -ereal.Exp(-x * x)
        print('ereal.LocalMin')
        res3 = ereal.LocalMin(f, a, b, eps, tol)
        print('res3: (x0, fx0, ic1):', res3)
        print()
        print()


    The same routine in Python, inserting the lambda expression into ``ereal.LocalMin``. Variables and functions local to the calling function can be accessed from within the lambda expression:

    .. code-block:: pycon

        a = -10.0; b = 20.0; eps = 1E-8; tol = 1E-8
        f = lambda x: -ereal.Exp(-x * x)
        print('ereal.LocalMin')
        res3 = ereal.LocalMin(lambda x: -ereal.Exp(-x * x), a, b, eps, tol)
        print('res3: (x0, fx0, ic1):', res3)
        print()
        print()




    **Examples in CSharp**

    The same routine in CSharp, using a callback function definition outside of the scope of the calling function. This form allows the callback function to be called from other functions as well, and it supports monitoring of the calls into the function (by un-commenting the ``Console.WriteLine`` statement), but variables, functions and subroutines local to the calling function cannot be accessed:


    .. code-block:: csharp

        public static ereal XF1(ereal x)
        {
            var y = -ereal.Exp(-x * x);
            //Console.WriteLine("x: {0},   y: {1}", x, y)
            return y;
        }

        public static void DemoLocalMin()
        {
            var a = -10; var b = 20; var eps = 1E-10; var tol = 1E-10;
            var Res1 = ereal.LocalMin(XF1, a, b, eps, tol);
            Console.WriteLine("Res1:(x, fx, ic) {0}", Res1);
        }


    The same routine in CSharp, using a multi-line lambda expression to define the callback function. Note that in contrast to Python, in CSharp a lambda expression can contain not only expressions but also statements, including a ``return`` statement. This is functionally equivalent to defining a local function without the need to create a new class. Variables, functions and subroutines local to the calling function can be accessed from within the lambda expression. The function which is defined by the lambda expression can be called locally. In this form the lambda expression allows monitoring of the calls into the callback function (by un-commenting the ``Console.WriteLine`` statement):

    .. code-block:: csharp

        public static void DemoLocalMin2()
        {
            var a = -10; var b = 20; var eps = 1E-10; var tol = 1E-10;
            var F2 = ereal (ereal x) =>
            {
                var y = -ereal.Exp(-x * x);
                //Console.WriteLine("x: {0},   y: {1}", x, y)
                return y;
            };
            var Res1 = ereal.LocalMin(F2, a, b, eps, tol);
            Console.WriteLine("Res1:(x, fx, ic) {0}", Res1);
        }


    The same routine in CSharp, using a single-line lambda expression to define the callback function. Note that there is no ``return`` statement, and the return type of the function is not specified but inferred from the function expression. Variables, functions and subroutines local to the calling function can be accessed from within the lambda expression. The function which is defined by the lambda expression can be called locally. Monitoring of calls into the callback function is not supported:

    .. code-block:: csharp

        public static void DemoLocalMin3()
        {
            var a = -10; var b = 20; var eps = 1E-10; var tol = 1E-10;
            var F3 = (ereal x) => -ereal.Exp(-x * x);
            var Res1 = ereal.LocalMin(F3, a, b, eps, tol);
            Console.WriteLine("Res1:(x, fx, ic) {0}", Res1);
        }


    The same routine in CSharp, using an anonymous lambda expression, which is like a single line lambda expression inserted directly into ``ereal.LocalMin``. Variables and functions local to the calling function can be accessed from within the lambda expression. Since an anonymous lambda expression does not have a name, it cannot be called locally. Monitoring of calls into the callback function is not supported:

    .. code-block:: csharp

        public static void DemoLocalMin4()
        {
            var a = -10; var b = 20; var eps = 1E-10; var tol = 1E-10;
            var Res1 = ereal.LocalMin((ereal x) => -ereal.Exp(-x * x), a, b, eps, tol);
            Console.WriteLine("Res1:(x, fx, ic) {0}", Res1);
        }



    All of the above CSharp routines produce the following output:

    .. code-block:: none

        Res1:(x, fx, ic) (-1.0001755541428017160E-10, -1.0000000000000000000, 14)










|newpage|

Modified Brent’s algorithm for finding a local minimum
-------------------------------------------------------------------------------

.. method:: math53.mbrent(f, a, b, t)


    where ``ctx`` is ``math53``. Returns a local minimum of the function `f` in the interval (a, b), implementing a modified (simplified) version of Brent's algorithm as in  procedure localmin with fixed eps=0.5*sqrt(eps_x).

    :param f: the function for which a local  minimum is to be found.
    :param a: the left border of the search interval.
    :param b: the right border of the search interval.
    :param tol: defines a tolerance eps*|x| + tol.

    :returns: a tuple (*localmin, fx, ic*), where *localmin* is an approximation to  a local minimum; *fx* = f(localmin); and *ic* is the iteration count, -1 if a=b, 0 if max.=5000 exceeded.



    See also:  Wikipedia :cite:p:`WikipediaAlg28`, :cite:t:`Zhang2011`, :cite:t:`Brent1973`,  BoostMath :cite:p:`BoostAlg28`.



    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> a = -10.0; b = 20.0; tol = 1E-8
        >>> f = lambda x: -ereal.Exp(-x * x)
        >>> res = ereal.MBrent(f, a, b, tol)
        >>> print('res4: (x0, fx0, ic1):', res4)







|newpage|


Rootfinding: Brent/Dekker algorithm
-------------------------------------------------------------------------------

.. method:: math53.zbrent(f, a, b, t)


    where ``ctx`` is ``math53``. Performs the Brent/Dekker algorithm with guaranteed convergence for finding a zero of a function,; assumes that f(a) and f(b) have different signs.

    :param f: the function for which a zero is sought.
    :param a: the left border of the search interval.
    :param b: the right border of the search interval.
    :param tol: defines a tolerance  6 * eps_x * `|x|` +2*tol.

    :returns: a tuple (*root, ic, err*), where *root* is an approximation to a zero (root) of the function; *ic* is the iteration count, -1 if a=b, 0 if max.=5000 exceeded; and *err* is the error code (0: no error, -1: if f(a) and f(b) have the same sign, -2: max. iteration count exceeded).


    Brent/Dekker algorithm with guaranteed convergence for finding a zero   of a function: Return a zero x of the function f in the interval [a,b] to within a tolerance 6*eps_x*|x|+2*t, where t is a positive tolerance; assumes that f(a) and f(b) have different signs. ic is the iteration   count; err is an error code (0: no error, -1: if f(a) and f(b) have the same sign, -2: max. iteration count exceeded). The algorithm is based   on a combination of successive interpolations and bisection. 


    See also:  Wikipedia :cite:p:`WikipediaAlg28`, :cite:t:`Zhang2011`, :cite:t:`Brent1971`,  BoostMath :cite:p:`BoostAlg28`.






    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> a = -20.0; b = 20.0; tol = 1E-8
        >>> f = lambda x: ereal.Exp(x) - 10
        >>> res = ereal.ZBrent(f, a, b, tol)
        >>> print('res5: (x0, ic1, err):', res5)








|newpage|



Rootfinding: Simplified Brent/Dekker algorithm
-------------------------------------------------------------------------------

.. method:: math53.zeroin(f, a, b, t)


    where ``ctx`` is ``math53``. Performs a simplified version of the Brent/Dekker algorithm for finding a zero of a function; assumes that f(a) and f(b) have different signs.

    :param f: the function for which a zero is sought.
    :param a: the left border of the search interval.
    :param b: the right border of the search interval.
    :param tol: defines a tolerance  6 * eps_x * `|x|` +2*tol.

    :returns: an approximation to a zero (root) of the function.


    See also:  Wikipedia :cite:p:`WikipediaAlg28`, :cite:t:`Zhang2011`, :cite:t:`Brent1971`,  BoostMath :cite:p:`BoostAlg28`.




    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> a = -20.0; b = 20.0; tol = 1E-8
        >>> f = lambda x: ereal.Exp(x) - 10
        >>> x0 = ereal.ZeroIn(f, a, b, tol)
        >>> print('x0: ', x0)






