

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />






|newpage|


Boost/Math: Numerical integration
===============================================================================


For a general overview, see:  Wikipedia :cite:p:`WikipediaAlg30`,  Wikipedia :cite:p:`WikipediaAlg31`.



Trapezoidal Quadrature
-------------------------------------------------------------------------------

.. method:: ctxboost.Trapezoidal(f, a, b, tol, max_refinements)

    where ``ctx`` is ``ctxboost``.

    :param f: the function for which the integral is determined.
    :param a: the left border of the integration interval.
    :param b: the right border of the integration interval.
    :param tol: the requested tolerance.
    :param max_refinements: the maximal number of refinements. The default is 12.

    :returns: a tuple (*integral, error, L1*), where *integral* is an approximation to the integral, using a trapezoidal quadrature; *error* is an estimate of the error; and *L1* is an estimate of the L1 value.


    See also:  BoostMath :cite:p:`BoostAlg34`,  Wikipedia :cite:p:`WikipediaAlg34`.



    If we assume only that the integrand is twice continuously differentiable, we can prove that the error of the composite trapezoidal rule is O(h2). Hence halving the interval only cuts the error by about a fourth, which in turn implies that we must evaluate the function many times before an acceptable accuracy can be achieved. 

    However, the trapezoidal rule has an astonishing property: If the integrand is periodic, and we integrate it over a period, then the trapezoidal rule converges faster than any power of the step size h. This can be seen by examination of the Euler-Maclaurin summation formula, which relates a definite integral to its trapezoidal sum and error terms proportional to the derivatives of the function at the endpoints and the Bernoulli numbers. If the derivatives at the endpoints are the same or vanish, then the error very nearly vanishes. Hence the trapezoidal rule is essentially optimal for periodic integrands. 

    Other classes of integrands which are integrated efficiently by this method are the bump functions and bell-shaped integrals over the infinite interval. For details, see Trefethen's SIAM review. 


    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> f = lambda x: 1 / (5 - 4 * ereal.Cos(x))
        >>> result2 = ereal.Trapezoidal(f, a, b)
        >>> print("res: ", res)






    .. code-block:: none

        boost.trapezoidal(f6, a, b, tol)
        result:  1.3639170485190606





|newpage|


Gauss-Legendre quadrature
-------------------------------------------------------------------------------

.. method:: ctxboost.GaussLegendre(f, a, b)

    where ``ctx`` is ``ctxboost``.

    :param f: the function for which the integral is determined.
    :param a: the left border of the integration interval.
    :param b: the right border of the integration interval.

    :returns: a tuple (*integral, L1*), where *integral* is an approximation to the integral, using a non-adaptive Gauss-Legendre quadrature; and *L1* is an estimate of the L1 value.


    See also:  Wikipedia :cite:p:`WikipediaAlg35`,  BoostMath :cite:p:`BoostAlg35`.




    This is intentionally a very simple quadrature routine, it obtains no estimate of the error, and is not adaptive, but is very efficient in simple cases that involve integrating smooth "bell like" functions and functions with rapidly convergent power series. 

    The Gaussian quadrature routine support both real and complex-valued quadrature. 

    Internally class gauss has pre-computed tables of abscissa and weights for 7, 15, 20, 25 and 30 points at up to 100-decimal digit precision. That means that using for example, gauss<double, 30>::integrate incurs absolutely zero set-up overhead from computing the abscissa/weight pairs. When using multiprecision types with less than 100 digits of precision, then there is a small initial one time cost, while the abscissa/weight pairs are constructed from strings. 

    However, for types with higher precision, or numbers of points other than those given above, the abscissa/weight pairs are computed when first needed and then cached for future use, which does incur a noticeable overhead.



    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> a = 0.0; b = 1.0; tol = 1.0E-9
        >>> f = lambda x: x * x * ereal.Atan(x)
        >>> res = ereal.GaussLegendre(f, a, b)
        >>> print("res: ", res)




    .. code-block:: none

        boost.gauss_legendre(f6, a, b, tol)
        result:  14.0






|newpage|


Gauss-Kronrod Quadrature
-------------------------------------------------------------------------------

.. method:: ctxboost.GaussKronrod(f, a, b, max_depth, tol)

    where ``ctx`` is ``ctxboost``.

    :param f: the function for which the integral is determined.
    :param a: the left border of the integration interval.
    :param b: the right border of the integration interval.
    :param max_depth: the maximal number of levels.
    :param tol: the requested tolerance.

    :returns: a tuple (*integral, error, L1*), where *integral* is an approximation to the integral, using a Gauss-Kronrod quadrature; *error* is an estimate of the error; and *L1* is an estimate of the L1 value.


    See also:  Wikipedia :cite:p:`WikipediaAlg36`,  BoostMath :cite:p:`BoostAlg36`.



    The idea behind Gaussian quadrature is to choose n nodes and weights in such a way that polynomials of order 2n-1 are integrated exactly. However, integration of polynomials is trivial, so it is rarely done via numerical methods. Instead, transcendental and numerically defined functions are integrated via Gaussian quadrature, and the defining problem becomes how to estimate the remainder. Gaussian quadrature alone (without some form of interval splitting) cannot answer this question. 

    It is possible to compute a Gaussian quadrature of order n and another of order (say) 2n+1, and use the difference as an error estimate. However, this is not optimal, as the zeros of the Legendre polynomials (nodes of the Gaussian quadrature) are never the same for different orders, so 3n+1 function evaluations must be performed. Kronrod considered the problem of how to interleave nodes into a Gaussian quadrature in such a way that all previous function evaluations can be reused, while increasing the order of polynomials that can be integrated exactly. This allows an a posteriori error estimate to be provided while still preserving exponential convergence. Kronrod discovered that by adding n+1 nodes (computed from the zeros of the Legendre-Stieltjes polynomials) to a Gaussian quadrature of order n, he could integrate polynomials of order 3n+1. 

    The integration routines provided here will perform either adaptive or non-adaptive quadrature, they should be chosen for the integration of smooth functions with no end point singularities.

    The number of points specified in the Points template parameter must be an odd number: giving a (N-1)/2 Gauss quadrature as the comparison for error estimation. 

    Internally class gauss_kronrod has pre-computed tables of abscissa and weights for 15, 31, 41, 51 and 61 Gauss-Kronrod points at up to 100-decimal digit precision. That means that using for example, gauss_kronrod<double, 31>::integrate incurs absolutely zero set-up overhead from computing the abscissa/weight pairs. When using multiprecision types with less than 100 digits of precision, then there is a small initial one time cost, while the abscissa/weight pairs are constructed from strings. 

    The Gauss-Kronrod quadrature support integrands defined on the real line and returning complex values. In this case, the template argument is the real type, and the complex type is deduced via the return type of the function. 




    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> a = 0.0; b = float('+inf')
        >>> f = lambda x: ereal.Exp(-x * x / 2)
        >>> result3 = ereal.GaussKronrod(f, a, b)
        >>> print("result3: ", result3)





    .. code-block:: none

        boost.gauss_kronrod(f6, a, b, max_depth, tol)
        result:  14.000000000000002





|newpage|


Double-exponential quadrature: tanh_sinh
-------------------------------------------------------------------------------

.. method:: ctxboost.TanhSinh(f, a, b, tol, max_refinements)

    where ``ctx`` is ``ctxboost``.

    :param f: the function for which the integral is determined.
    :param a: the left border of the integration interval.
    :param b: the right border of the integration interval.
    :param tol: the requested tolerance.
    :param max_refinements: the maximal number of refinements. The default is 12.

    :returns: a tuple (*integral, error, L1, levels*), where *integral* is an approximation to the integral, using a tanh-sinh quadrature; *error* is an estimate of the error; *L1* is an estimate of the L1 value; and *levels* is the number of levels used.


    See also:  Wikipedia :cite:p:`WikipediaAlg40`,  BoostMath :cite:p:`BoostAlg40`, :cite:t:`Okayama2013`, :cite:t:`Okayama2016`.


    The tanh-sinh quadrature routine provided by boost is a rapidly convergent numerical integration scheme for holomorphic integrands. By this we mean that the integrand is the restriction to the real line of a complex-differentiable function which is bounded on the interior of the unit disk `|z| < 1`, so that it lies within the so-called Hardy space. If your integrand obeys these conditions, it can be shown that tanh-sinh integration is optimal, in the sense that it requires the fewest function evaluations for a given accuracy of any quadrature algorithm for a random element from the Hardy space. 

    Complex integrands are supported.






    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> a = -1.0; b = 1.0
        >>> f = lambda x: 5 * x + 7
        >>> res = ereal.TanhSinh(f, a, b)
        >>> print("res: ", res)





    .. code-block:: none

        boost.tanh_sinh(f6, a, b)
        result:  14.0




|newpage|


Double-exponential quadrature: sinh_sinh
-------------------------------------------------------------------------------

.. method:: ctxboost.SinhSinh(f, tol, max_refinements)

    where ``ctx`` is ``ctxboost``.

    :param f: the function for which the integral is determined.
    :param tol: the requested tolerance.
    :param max_refinements: the maximal number of refinements. The default is 9.

    :returns: a tuple (*integral, error, L1, levels*), where *integral* is an approximation to the integral, using a sinh-sinh quadrature over the limits of integration `(-\infty, \infty)`; *error* is an estimate of the error; *L1* is an estimate of the L1 value; and *levels* is the number of levels used.



    See also:  BoostMath :cite:p:`BoostAlg42`, :cite:t:`Okayama2013`, :cite:t:`Okayama2016`.



    Returns the value of the integral of f over the limits of integration `(-\infty, \infty)`. Complex integrands are supported.




    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> f = lambda x: math.exp(-x * x)
        >>> res = ereal.SinhSinh(f)
        >>> print("res: ", res)






    .. code-block:: none

        boost.sinh_sinh(f7)
        result:  1.7724538509055168




|newpage|


Double-exponential quadrature: exp_sinh
-------------------------------------------------------------------------------

.. method:: ctxboost.ExpSinh((f, tol, max_refinements, a, b)

    where ``ctx`` is ``ctxboost``.

    :param f: the function for which the integral is determined.
    :param tol: the requested tolerance.
    :param max_refinements: the maximal number of refinements. The default is 12.
    :param a: the left border of the integration interval. The default is 0.
    :param b: the right border of the integration interval.  The default is `+\infty`. Note that *a* and *b* cannot both be finite.

    :returns: a tuple (*integral, error, L1, levels*), where *integral* is an approximation to the integral, using a tanh-sinh quadrature; *error* is an estimate of the error; *L1* is an estimate of the L1 value; and *levels* is the number of levels used.




    Returns the value of the integral of f over the limits of integration `(0, \infty)`. Complex integrands are supported.

    See also:  BoostMath :cite:p:`BoostAlg43`, :cite:t:`Okayama2013`, :cite:t:`Okayama2016`.





    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> f = lambda x: math.exp(-3 * x)
        >>> result3 = ereal.ExpSinh(f)
        >>> print("result3: ", result3)







    .. code-block:: none

        boost.exp_sinh(f8)
        result:  0.33333333333333337






|newpage|


Fourier Integral, Cosine
-------------------------------------------------------------------------------

.. method:: ctxboost.OouraCos(f)

    where ``ctx`` is ``ctxboost``.

    :param f: the function for which the integral is determined.

    :returns: a tuple (*integral, error*), where *integral* is an approximation to the integral, using a Ooura Cos quadrature of the function f in the interval (0, +inf); *error* is an estimate of the error.


    See also:  BoostMath :cite:p:`BoostAlg44`, :cite:t:`Ooura1999`, :cite:t:`Ooura2005`.





    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> f = lambda x: 1 / (x * x + 1)
        >>> result3 = ereal.Ooura_Cos(f)
        >>> print("result3: ", result3)





    .. code-block:: none

        boost.OouraCos(f3, a, b, get_digits, maxit)
        x0:  2.9086877250246185e-09





|newpage|


Fourier Integral, Sine
-------------------------------------------------------------------------------

.. method:: ctxboost.OouraSin(f)

    where ``ctx`` is ``ctxboost``.

    :param f: the function for which the integral is determined.

    :returns: a tuple (*integral, error*), where *integral* is an approximation to the integral, using a Ooura Sin quadrature of the function f in the interval (0, +inf); *error* is an estimate of the error.


    See also:  BoostMath :cite:p:`BoostAlg44`, :cite:t:`Ooura1999`, :cite:t:`Ooura2005`.




    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> f = lambda x: 1 / x
        >>> result3 = ereal.Ooura_Sin(f)
        >>> print("result3: ", result3)






    .. code-block:: none

        boost.OouraCos(f3, a, b, get_digits, maxit)
        x0:  2.9086877250246185e-09






.. _rst_gil_pelaez_pdf_boost: 

Calculating the pdf from the characteristic function
-------------------------------------------------------------------------------

.. method:: ctx.pdf_from_cf_boost(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Calculates the pdf as the inverse Fourier transform of its characteristic function.

    The PDF of Y is the inverse Fourier transform of its characteristic function,

    .. math:: \text{pdf}_X(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{ity} C_X(t) \mathrm{d} y  = \frac{1}{\pi} \int_{0}^{\infty} \Re \left ( e^{-itx} C_X(t) \right ) \mathrm{d} t.

    where `\Re (z)` denotes the real part of `z`. We also have


    .. math:: \int_{0}^{\infty} \Re \left ( e^{-itx} C_X(t) \right ) \mathrm{d} t = \int_{0}^{\infty} \Re \left ( C_X(t) \right ) \cos(t x) \mathrm{d} t +   \int_{0}^{\infty} \Im \left (  C_X(t) \right ) \sin(t x) \mathrm{d} t.

    Using the right-hand side of this equation allows for efficient use of the quadrature formula of Fillon, with the half-period  `\omega = \pi/x`.







.. _rst_gil_pelaez_cdf_boost: 

Calculating the cdf from the  characteristic function
-------------------------------------------------------------------------------

.. method:: ctx.cdf_from_cf_continuous_boost(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Calculates the cdf from the characteristic function using the procedure of Gil-Pelaez.

    Assuming that the characteristic function is absolutely integrable over `(-\infty, \infty)`, Gil-Pelaez  derived the following inversion formula which requires integration of a real-valued function only. In particular,

    .. math:: \text{cdf}_X(x) = \frac{1}{2} - \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{e^{-itx} C_X(t) - e^{itx} C_X(t)}{it} \mathrm{d} t  = \frac{1}{2} - \frac{1}{\pi} \int_{0}^{\infty} \Im \left ( \frac{  e^{-itx} C_X(t)}{t}  \right ) \mathrm{d}t.

    where `\Im (z)` denotes the imaginary part of `z`. We also have


    .. math:: \int_{0}^{\infty} \Im \left ( \frac{  e^{-itx} C_X(t)}{t}  \right ) \mathrm{d}t =  \int_{0}^{\infty} \Im \left ( \frac{C_X(t)}{t}  \right ) \cos(t x) \mathrm{d}t  -  \int_{0}^{\infty} \Re \left ( \frac{C_X(t)}{t}  \right ) \sin(t x) \mathrm{d}t.

    Using the right-hand side of this equation allows for efficient use of the quadrature formula of Fillon, with the half-period  `\omega = \pi/x`.


    The python code is currently in Charfun.py

    The following code provides a test-suite for the numerical inversion of the characteristic function:

    .. code-block:: python

        class tests_charfunc(rv_cont):

            def __init__(self, rv2, x = 5, a = 0, b = 2):
        
                cdf_value = rv2.cdf(x)
                print ("rv2.cdf(x): ", cdf_value)

                rv2.set_x(x)
                plot(rv2.gil_pelaez_imag, [a, b], points=200)
                print
        
                rv2.set_x(x)
                plot(rv2.gil_pelaez_cos, [a, b], points=200)
                print
        
                rv2.set_x(x)
                plot(rv2.gil_pelaez_sin, [a, b], points=200)
                print
        
                rv2.set_x(x)
                I0 = quad(rv2.gil_pelaez_imag, [0, +inf])
                print("Integral: ", I0)
                result0 = 0.5 - I0/pi
                print("result0:", result0 )
                print("diff0:", result0 - cdf_value)
        
        
                rv2.set_x(x)
                I1 =quadosc(rv2.gil_pelaez_cos, [0, inf], period=1*pi/x) # half period
                print("I1:", I1 )
        
                rv2.set_x(x)
                I2 =quadosc(rv2.gil_pelaez_sin, [0, inf], period=1*pi/x) # half period
                print("I2:", I2 )
        
                I3 = I1 + I2
                print("I3:", I3 )
                print("Int diff:", I3 - I0)
                result3 = 0.5 - I3/pi
                print("result3:", result3 )
                print("diff3:", result3 - cdf_value)







    **Example: non-central chi-squared distribution**

    The following code shows the difference between using the generic integration (error: diff0: -6.1218939724378892896e-6) and quadrature for oscillatory functions (error: diff3: 8.4703294725430033907e-22).


    .. code-block:: python

        mp.dps = 20
        print()
        print ("Hello mpDistributions local ! ")
        print()


        a = 0.0
        b = 2

        n = mpf("5")
        x = mpf("10")
        rv2 = mpr().chisquare(n)

        tests_charfunc(rv2, x, a, b)



    This produces the following output (plots are to be added):

    .. parsed-literal::

        Hello mpDistributions local ! 

        rv2.cdf(x):  0.92476475385348782128

        Integral:  -1.334418597712864291
        result0: 0.92475863195951538339
        diff0: -6.1218939724378892896e-6
        I1: 0.11817924829245123086
        I2: -1.4526170785024453884
        I3: -1.3344378302099941575
        Int diff: -0.000019232497129866511475
        result3: 0.92476475385348782128
        diff3: 8.4703294725430033907e-22



