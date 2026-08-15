

.. |newpage| raw:: latex

   \newpage


.. |vspace| raw:: html

   <br />





|newpage|



Cumulative distribution function (cdf)
========================================================




Calculating the cdf from the pdf
-------------------------------------------------------------------------------

.. method:: ctx.cdf_from_pdf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.



    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`:

    .. math:: \text{cdf}_X(x) = \int_{0}^{x} \text{pdf}_X(x) \mathrm{d}t .


    Using this method can be a viable option when the pdf, but not the cdf, is available in closed form.







Calculating the cdf from the pmf
-------------------------------------------------------------------------------

.. method:: ctx.cdf_from_pmf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    If `X` is a purely discrete random variable, then it attains values `x_{1},x_{2},\ldots` with probability `p_{i}=p(x_{i})`, and the CDF of `X` will be discontinuous at the points `x_{i}`: 

    .. math:: F_{X}(x)=\operatorname {P} (X\leq x)=\sum _{x_{i}\leq x}\operatorname {P} (X=x_{i})=\sum _{x_{i}\leq x}p(x_{i}).





.. _rst_gil_pelaez_cdf: 

Calculating the cdf from the  characteristic function
-------------------------------------------------------------------------------

.. method:: ctx.cdf_from_cf_continuous(x, cf)

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



.. _rst_cdf_from_cf_lattice: 

Calculating the cdf and sf from the  characteristic function (lattice distribution)
--------------------------------------------------------------------------------------------

.. method:: ctx.cdf_from_cf_lattice(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    The corresponding inversion formula for discrete distributions on the nonnegative integers is


    .. math::  \text{cdf}(x) =  \frac{1}{\pi} \int_{0}^{\pi} \Re \left( C_X(t)  \sum_{z=0}^x e^{-itz} \right) \mathrm{d}t.


    .. math::  \text{sf}(x) = 1-\text{cdf}(x) = \frac{1}{\pi} \int_{0}^{\pi} \Re \left( C_X(t)  \sum_{z=x+1}^{N(N+1)/2} e^{-itz} \right) \mathrm{d}t.






Calculating the cdf from the factorial moments (lattice distributions)
---------------------------------------------------------------------------------------------


The following relationships hold between the probabilities and the factorial moments in the case of a discrete distribution:


.. math::  \text{Pr}[X=x] = \sum_{j \ge x} (-1)^{x+j} \binom{j}{x} \frac{\mu'_{[j]}}{j!}  = \sum_{r \ge 0} (-1)^{r} \frac{\mu'_{[x+r]}}{x!r!}

and

.. math::  \sum_{i \ge x} \text{Pr}[X=i] = \sum_{j \ge x} (-1)^{x+j} \binom{j-1}{x-1} \frac{\mu'_{[j]}}{j!} 



See also Johnson(2005), page 59.






