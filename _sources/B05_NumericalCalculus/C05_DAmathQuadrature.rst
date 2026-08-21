

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />





|newpage|


DAMath: Numerical Quadrature
===============================================================================

For a general overview, see:  Wikipedia :cite:p:`WikipediaAlg30`,  Wikipedia :cite:p:`WikipediaAlg31`, MathWorld :cite:p:`WolframAlg31`,  Wikipedia :cite:p:`WikipediaAlg33`.


.. _rst_amath_ier_1: 

General error codes for Amath integration functions, type 1
-----------------------------------------------------------------

Amath integration functions which are NOT using the double exponential transformation return an error code ``ier``, which has the following meaning:

``ier = 0``: Normal and reliable termination of the routine. It is assumed  that the requested accuracy has been achieved.

``ier > 0``: Abnormal termination of the routine the estimates for integral and error are less reliable. It is assumed that the requested accuracy has not been achieved.

``ier = 1``: Maximum number of subdivisions allowed has been achieved. One can allow more subdivisions by increasing the value of limit (and taking the according dimension adjustments into account). However, if this yields no improvement it is advised to analyze the integrand in order to determine the integration difficulties. If the position of a local difficulty can be determined (e.g. singularity, discontinuity within the interval) one will probably gain from splitting up the interval at this point and calling the integrator on the subranges. If possible, an appropriate special-purpose integrator should be used, which is designed for handling the type of difficulty involved.

``ier = 2``: The occurrence of roundoff error is detected, which prevents the requested tolerance from being achieved. The error may be under-estimated. 

``ier = 3``: Extremely bad integrand behaviour occurs at some points of the integration interval.

``ier = 4``: The algorithm does not converge. Roundoff error is detected in the extrapolation table. It is presumed that the requested tolerance cannot be achieved, and that the returned result is the best which can be obtained.

``ier = 5``: The integral is probably divergent, or slowly convergent. It must be noted that divergence can occur with any other value of ier.

``ier = 6``: The input is invalid, because epsabs <= 0 and epsrel < 50*eps_d. result, abserr, last are set to zero.

``ier = 7``: The input is invalid, limit < 0 or limit > QMAXLIM. result, abserr, last are set to zero.

``ier = 8``: Dynamic list vectors cannot be allocated. result, abserr, last are set to zero.

``ier = 9``: At least one limit a or b is NaN, or infinite a=b. result, abserr, last are set to NaN_d.



.. _rst_amath_ier_2: 

General error codes for Amath integration functions, type 2
-----------------------------------------------------------------

Amath integration functions which are using the double exponential transformation return an error code ``ier``, which has the following meaning:

``ier = 0``: Normal and reliable termination of the routine. It is assumed  that the requested accuracy has been achieved.

``ier > 0``: Abnormal termination of the routine the estimates for integral and error are less reliable. It is assumed that the requested accuracy has not been achieved.

``ier = 1``: eps < 8*eps_x.

``ier = 2``: roundoff problems.

``ier = 3``: max. iterations, result/abserr have values.









|newpage|


Global adaptive quadrature by Forsythe, Malcolm, Moler (quanc8)
-------------------------------------------------------------------------------

.. method:: ctx.quanc8(f, a, b, epsabs, epsrel, limit)

    where ``ctx`` is ``math53``. Performs a global adaptive quadrature of f over (a,b) based on a Fortran subroutine by Forsythe, Malcolm, Moler.

    :param f: the function for which the integral is determined.
    :param a: the left border of the integration interval.
    :param b: the right border of the integration interval.
    :param abserr: the absolute accuracy requested.
    :param relerr: the relative accuracy requested.

    :returns: a tuple (*integral, err, flag, neval*), where *integral* is an approximation to the integral; *abserr* is an estimate of of the modulus of the absolute error; *neval* is the number of integrand evaluations; and *ier* is the error code (success=0, error > 0: see :ref:`General error codes for Amath integration functions, type 1 <rst_amath_ier_1>`).




    Include reference to Forsythe, Malcolm, Moler.





    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> a = 0.0; b = 2.0; epsabs = 1E-8; epsrel = 0.0; limit = 0
        >>> f = lambda x: ereal.Exp(-x * x / 2)
        >>> result, abserr, neval, ier = ereal.Qags(f, a, b, epsabs, epsrel, limit)
        >>> print("result: ", result, "abserr: ", abserr)
        >>> print("neval: ", neval, "ier: ", ier)





|newpage|


21-point Gauss-Kronrod rule, finite interval (qags)
-------------------------------------------------------------------------------

.. method:: ctx.qags(f, a, b, epsabs, epsrel, limit)

    where ``ctx`` is ``math53``. Performs a global adaptive quadrature of f over (a,b) based on 21-point Gauss-Kronrod rule for the subintervals, with acceleration by Wynn's epsilon algorithm.

    :param f: the function for which the integral is determined.
    :param a: the left border of the integration interval.
    :param b: the right border of the integration interval.
    :param epsabs: the absolute accuracy requested.
    :param epsrel: the relative accuracy requested.
    :param limit: upperbound on the no. of subintervals, 0: use DefLimit.

    :returns: a tuple (*integral, abserr, neval, ier*), where *integral* is an approximation to the integral; *abserr* is an estimate of of the modulus of the absolute error; *neval* is the number of integrand evaluations; and *ier* is the error code (success=0, error > 0: see :ref:`General error codes for Amath integration functions, type 1 <rst_amath_ier_1>`).


    See also: :cite:t:`Piessens1983`,  Wikipedia :cite:p:`WikipediaAlg32`,  Wikipedia :cite:p:`WikipediaAlg36`.




    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> a = 0.0; b = 2.0; epsabs = 1E-8; epsrel = 0.0; limit = 0
        >>> f = lambda x: ereal.Exp(-x * x / 2)
        >>> result, abserr, neval, ier = ereal.Qags(f, a, b, epsabs, epsrel, limit)
        >>> print("result: ", result, "abserr: ", abserr)
        >>> print("neval: ", neval, "ier: ", ier)










|newpage|


15-point Gauss-Kronrod rule, infinite interval (qagi)
-------------------------------------------------------------------------------

.. method:: math53.qagi(f, bound, inf, epsabs, epsrel, limit)

    where ``ctx`` is ``math53``. Performs a global adaptive quadrature of f over an infinite interval based on a transformed 15-point Gauss-Kronrod for the subintervals, with acceleration by Wynn's epsilon algorithm.

    :param f: the function for which the integral is determined.
    :param bound: finite bound of integration range (if any).
    :param inf: indicating the kind of integration range involved:  1 corresponds to  (bound, +infinity), -1 to  (-infinity, bound), 2  to  (-infinity, +infinity).
    :param epsabs: the absolute accuracy requested.
    :param epsrel: the relative accuracy requested.
    :param limit: upperbound on the no. of subintervals, 0: use DefLimit.

    :returns: a tuple (*integral, abserr, neval, ier*), where *integral* is an approximation to the integral; *abserr* is an estimate of of the modulus of the absolute error; *neval* is the number of integrand evaluations; and *ier* is the error code (success=0, error > 0: see :ref:`General error codes for Amath integration functions, type 1 <rst_amath_ier_1>`).


    See also: :cite:t:`Piessens1983`,  Wikipedia :cite:p:`WikipediaAlg32`.






    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> bound = 0.0; infcode = 2; epsabs = 1E-8; epsrel = 0.0; limit = 0
        >>> f = lambda x: ereal.Exp(-x * x / 2)
        >>> result, abserr, neval, ier = ereal.Qagi(f, bound, infcode, epsabs, epsrel, limit)
        >>> print("result: ", result, "abserr: ", abserr)
        >>> print("neval: ", neval, "ier: ", ier)







|newpage|



Cauchy principal value, finite interval (qawc)
-------------------------------------------------------------------------------

.. method:: math53.qawc(f, a, b, c, epsabs, epsrel, limit)

    where ``ctx`` is ``math53``. Performs an adaptive quadrature of `f(x)/(x-c)` over the finite interval `(a,b)` with the singularity at `c` and `c` not equal `a` or `b`. The routine calculates an approximation result to the Cauchy principal value.

    :param f: the function for which the integral is determined.
    :param a: the left border of the integration interval.
    :param b: the right border of the integration interval.
    :param c: singularity, ier=6 if `c=a` or `c=b`.
    :param epsabs: the absolute accuracy requested.
    :param epsrel: the relative accuracy requested.
    :param limit: upperbound on the no. of subintervals, 0: use DefLimit.

    :returns: a tuple (*integral, abserr, neval, ier*), where *integral* is an approximation to the integral; *abserr* is an estimate of of the modulus of the absolute error; *neval* is the number of integrand evaluations; and *ier* is the error code (success=0, error > 0: see :ref:`General error codes for Amath integration functions, type 1 <rst_amath_ier_1>`).


    See also: https://maxima.sourceforge.io/docs/manual/maxima_100.html

    See also: :cite:t:`Piessens1983`,  Wikipedia :cite:p:`WikipediaAlg32`,  Wikipedia :cite:p:`WikipediaAlg41`.



    The routine in Python:

    .. code-block:: pycon
        
            # Qawc Example is missing
            bound = 0.0; infcode = 2; epsabs = 1E-8; epsrel = 0.0; limit = 0
            f = lambda x: ereal.Exp(-x * x / 2)
            result, abserr, neval, ier = ereal.Qagi(f, bound, infcode, epsabs, epsrel, limit)
            print("ereal.Qagi")
            print("result: ", result, "abserr: ", abserr)
            print("neval: ", neval, "ier: ", ier)
            print()







|newpage|


Double Exponential (DE) transformation, finite interval (intde)
-------------------------------------------------------------------------------

.. method:: math53.intde(f, a, b, eps)

    where ``ctx`` is ``math53``. Performs an automatic quadrature of f(x) over the finite interval (a,b)} using Double Exponential (DE) transformation.

    :param f: the function for which the integral is determined.
    :param a: the left border of the integration interval.
    :param b: the right border of the integration interval.
    :param eps: the relative accuracy requested.

    :returns: a tuple (*integral, abserr, neval, ier*), where *integral* is an approximation to the integral,  if ier=0 or 3; *abserr* is an estimate of of the modulus of the absolute error, if ier=0 or 3; *neval* is the number of integrand evaluations; and *ier* is the error code (success=0, error > 0: see :ref:`General error codes for Amath integration functions, type 2 <rst_amath_ier_2>`).


    See also:  Wikipedia :cite:p:`WikipediaAlg40`, :cite:t:`Takahasi1974`, :cite:t:`Ooura1991`, :cite:t:`Mori1991`.




    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> a = 0.0; b = 2.0; eps = 1E-8
        >>> f = lambda x: ereal.Exp(-x * x / 2)
        >>> result, abserr, neval, ier = ereal.Intde(f, a, b, eps)
        >>> print("result: ", result, "abserr: ", abserr)
        >>> print("neval: ", neval, "ier: ", ier)







|newpage|


DE transformation, infinite interval, no oscillatory factor (intdei)
-------------------------------------------------------------------------------

.. method:: math53.intdei(f, a, eps)

    where ``ctx`` is ``math53``. Performs an automatic quadrature of f(x) over (a,INF) using Double Exponential transformation when f(x) has no oscillatory factor.

    :param f: the function for which the integral is determined.
    :param a: the left border of the integration interval.
    :param eps: the relative accuracy requested.

    :returns: a tuple (*integral, abserr, neval, ier*), where *integral* is an approximation to the integral,  if ier=0 or 3; *abserr* is an estimate of of the modulus of the absolute error, if ier=0 or 3; *neval* is the number of integrand evaluations; and *ier* is the error code (success=0, error > 0: see :ref:`General error codes for Amath integration functions, type 2 <rst_amath_ier_2>`).


    See also:  Wikipedia :cite:p:`WikipediaAlg40`, :cite:t:`Takahasi1974`, :cite:t:`Ooura1991`, :cite:t:`Mori1991`.






    The routine in Python:

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> a = 0.0; eps = 1E-8
        >>> f = lambda x: ereal.Exp(-x * x / 2)
        >>> result, abserr, neval, ier = ereal.Intdei(f, a, eps)
        >>> print("result: ", result, "abserr: ", abserr)
        >>> print("neval: ", neval, "ier: ", ier)







|newpage|


DE transformation, infinite interval, oscillatory factor (intdeo)
-------------------------------------------------------------------------------

.. method:: math53.intdeo(f, a, omega, eps)

    where ``ctx`` is ``math53``.     Performs an automatic quadrature of f(x) over (a,INF) using Double Exponential transformation when f(x) has an oscillatory factor.

    :param f: the function for which the integral is determined.
    :param a: the left border of the integration interval.
    :param omega: oscillatory factor.
    :param eps: the relative accuracy requested.

    :returns: a tuple (*integral, abserr, neval, ier*), where *integral* is an approximation to the integral,  if ier=0 or 3; *abserr* is an estimate of of the modulus of the absolute error, if ier=0 or 3; *neval* is the number of integrand evaluations; and *ier* is the error code (success=0, error > 0: see :ref:`General error codes for Amath integration functions, type 2 <rst_amath_ier_2>`).


    See also:  Wikipedia :cite:p:`WikipediaAlg40`, :cite:t:`Takahasi1974`, :cite:t:`Ooura1991`, :cite:t:`Mori1991`.






    The routine in Python:

    .. code-block:: pycon

        # Intdeo example is missing
        a = 0.0; eps = 1E-8
        f = lambda x: ereal.Exp(-x * x / 2)
        result, abserr, neval, ier = ereal.Intdei(f, a, eps)
        print("ereal.Intdei")
        print("result: ", result, "abserr: ", abserr)
        print("neval: ", neval, "ier: ", ier)
        return "0"




