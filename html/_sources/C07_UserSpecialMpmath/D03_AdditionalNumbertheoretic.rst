

.. |newline| raw:: latex

   \newline



.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

Additional numbertheoretic functions
===============================================================================





.. _rst_mpm_primepi: 

Mpmath: Prime counting function
-------------------------------------------------------------------------------


.. method:: ctx.primepi(x)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns the prime counting function.

    See also Wikipedia :cite:p:`WikipediaFun122`, MathWorld :cite:p:`WolframFun122`, Mpmath :cite:p:`MpmathFun1028`.



    Evaluates the prime counting function, `\pi(x)`, which gives
    the number of primes less than or equal to `x`. The argument
    `x` may be fractional.

    The prime counting function is very expensive to evaluate
    precisely for large `x`, and the present implementation is
    not optimized in any way. For numerical approximation of the
    prime counting function, it is better to use :ref:`primepi2() <rst_mpm_primepi2>`
    or :ref:`riemannr() <rst_mpm_riemannr>`.

    Some values of the prime counting method::

        >>> from mpfunlab import *
        >>> [primepi(k) for k in range(20)]
        [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8]
        >>> primepi(3.5)
        2
        >>> primepi(100000)
        9592












.. _rst_mpm_mangoldt: 

Mpmath: Mangoldt function
-------------------------------------------------------------------------------


.. method:: ctx.mangoldt(n)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns the Mangoldt function. See also  Wikipedia :cite:p:`WikipediaFun1030`, MathWorld :cite:p:`WolframFun1030`, Mpmath :cite:p:`MpmathFun1030`. 

    Evaluates the von Mangoldt function `\Lambda(n) = \log p` if `n = p^k` a power of a prime, and `\Lambda(n) = 0` otherwise::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> [mangoldt(n) for n in range(-2,3)]
        [0.0, 0.0, 0.0, 0.0, 0.6931471805599453094172321]
        >>> mangoldt(6)
        0.0
        >>> mangoldt(7)
        1.945910149055313305105353
        >>> mangoldt(8)
        0.6931471805599453094172321
        >>> fsum(mangoldt(n) for n in range(101))
        94.04531122935739224600493
        >>> fsum(mangoldt(n) for n in range(10001))
        10013.39669326311478372032








.. _rst_mpm_primepi2: 

Mpmath: Upper bound for the value of the prime counting function
-------------------------------------------------------------------------------


.. method:: ctx.primepi2_upper(x)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns bounds for the value of the prime counting function. See also Wikipedia :cite:p:`WikipediaFun123`, Wikipedia :cite:p:`WikipediaFun122`, MathWorld :cite:p:`WolframFun122`, MathWorld :cite:p:`WolframFun123`.

    Returns an interval (as an ``mpi`` instance) providing bounds
    for the value of the prime counting function `\pi(x)`. For small
    `x`, :ref:`primepi2() <rst_mpm_primepi2>` returns an exact interval based on
    the output of :ref:`primepi() <rst_mpm_primepi>`. For `x > 2656`, a loose interval
    based on Schoenfeld's inequality

    .. math ::

        |\pi(x) - \mathrm{li}(x)| < \frac{\sqrt x \log x}{8 \pi}

    is returned. This estimate is rigorous assuming the truth of
    the Riemann hypothesis, and can be computed very quickly.


    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = '1E+10'
        >>> dx = dec.primepi2_upper(x); mx = mpm.primepi2_upper(x); gx = gmp.primepi2_upper(x)
        >>> fx = fpm.primepi2_upper(x); ax = apm.primepi2_upper(x)
        >>> mpm.show([dx, mx, gx, fx, ax])
        dec:  4.551472320000000000000000000000000000000E+8
        mpm:  4.551472320000000000000000000000000000000e+8
        gmp:  4.551472320000000000000000000000000000000E+08
        fpm:  4.55147232000000E+08
        apm:  4.551472320000000000000000000000000000000e+8 (0.0%)





.. _rst_mpm_primepi2_lower: 

Mpmath: Lower dound for the value of the prime counting function
-------------------------------------------------------------------------------


.. method:: ctx.primepi2_lower(x)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns bounds for the value of the prime counting function. See also Wikipedia :cite:p:`WikipediaFun123`, Wikipedia :cite:p:`WikipediaFun122`, MathWorld :cite:p:`WolframFun122`, MathWorld :cite:p:`WolframFun123`.

    Returns an interval (as an ``mpi`` instance) providing bounds
    for the value of the prime counting function `\pi(x)`. For small
    `x`, :ref:`primepi2() <rst_mpm_primepi2>` returns an exact interval based on
    the output of :ref:`primepi() <rst_mpm_primepi>`. For `x > 2656`, a loose interval
    based on Schoenfeld's inequality

    .. math ::

        |\pi(x) - \mathrm{li}(x)| < \frac{\sqrt x \log x}{8 \pi}

    is returned. This estimate is rigorous assuming the truth of
    the Riemann hypothesis, and can be computed very quickly.


    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = '1E+10'
        >>> dx = dec.primepi2_lower(x); mx = mpm.primepi2_lower(x); gx = gmp.primepi2_lower(x)
        >>> fx = fpm.primepi2_lower(x); ax = apm.primepi2_lower(x)
        >>> mpm.show([dx, mx, gx, fx, ax])
        dec:  4.549639970000000000000000000000000000000E+8
        mpm:  4.549639970000000000000000000000000000000e+8
        gmp:  4.549639970000000000000000000000000000000E+08
        fpm:  4.54963997000000E+08
        apm:  4.549639970000000000000000000000000000000e+8 (0.0%)









.. _rst_mpm_riemannr: 

Mpmath, DAMath: Riemann R function
-------------------------------------------------------------------------------


.. method:: ctx.riemann_r(x)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns the Riemann R function. See also MathWorld :cite:p:`WolframFun123`, Mpmath :cite:p:`MpmathFun123`., Mpmath :cite:p:`MpmathFun124`. 


    Evaluates the Riemann R function, a smooth approximation of the
    prime counting function. The Riemann
    R function gives a fast numerical approximation useful e.g. to
    roughly estimate the number of primes in a given interval.

    The Riemann R function is computed using the rapidly convergent Gram
    series,

    .. math ::

        R(x) = 1 + \sum_{k=1}^{\infty}
            \frac{\log^k x}{k k! \zeta(k+1)}.

    From the Gram series, one sees that the Riemann R function is a
    well-defined analytic function (except for a branch cut along
    the negative real half-axis); it can be evaluated for arbitrary
    real or complex arguments.




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = '7.5'
        >>> \mathrm{d}x = dec.riemannr(x); mx = mpm.riemannr(x); gx = gmp.riemannr(x)
        >>> fx = fpm.riemannr(x); ax = apm.riemannr(x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  3.729347432649662619188571351358357974070E+0
        mpm:  3.729347432649662619188571351358357974070e+0
        gmp:  3.729347432649662619188571351358357974070E+00
        fpm:  3.72934743264966E+00
        mpm:  3.729347432649662619188571351358357974070e+0


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '-4+2j'
        >>> \mathrm{d}z = dec.riemannr(z); mz = mpm.riemannr(z); gz = gmp.riemannr(z)
        >>> fz = fpm.riemannr(z); az = apm.riemannr(z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: -5.5100220815548642759E-1  + 2.1696639813811945004E+0j
        mpm: -5.5100220815548642759e-1  + 2.1696639813811945004e+0j
        gmp: -5.5100220815548642759E-01 + 2.1696639813811945004E+00j
        fpm: -5.51002208155486E-01      + 2.16966398138119E+00j
        mpm: -5.5100220815548642759e-1  + 2.1696639813811945004e+0j








.. _rst_mpm_primezeta: 

Mpmath, DAMath: Prime zeta function
-------------------------------------------------------------------------------


.. method:: ctx.primezeta(s)

    where ``ctx`` is ``math53``, ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns for `x > 0.2` the prime zeta function `\displaystyle P(x) = \sum_{p \text{ prime}} p^{-x}`,  or its real part for `x<1`.

    See also :cite:t:`Ehrhardt2018` (3.6.2).


    Returns the prime zeta function. See also  Wikipedia :cite:p:`WikipediaFun1021`, MathWorld :cite:p:`WolframFun1021`, Mpmath :cite:p:`MpmathFun1021`, :cite:t:`Froberg1968`. 


    This function calculates the prime zeta function

    .. math :: P(x) = \sum_{p prime} p^{-x}, \quad x>1.

    Computes the prime zeta function, which is defined
    in analogy with the Riemann zeta function (:ref:`zeta() <rst_mpm_zeta>`)
    as

    .. math ::

        P(s) = \sum_p \frac{1}{p^s}

    where the sum is taken over all prime numbers `p`. Although
    this sum only converges for `\mathrm{Re}(s) > 1`, the
    function is defined by analytic continuation in the
    half-plane `\mathrm{Re}(s) > 0`.

    **Examples**

    Arbitrary-precision evaluation for real and complex arguments is
    supported::

        >>> from xlcalcnet import *
        >>> mp.dps = 30; mp.pretty = True
        >>> primezeta(2)
        0.452247420041065498506543364832
        >>> primezeta(pi)
        0.15483752698840284272036497397
        >>> mp.dps = 50
        >>> primezeta(3)
        0.17476263929944353642311331466570670097541212192615
        >>> mp.dps = 20
        >>> primezeta(3+4j)
        (-0.12085382601645763295 - 0.013370403397787023602j)






.. _rst_mpm_const_mertens: 

Mpmath: Mertens constant
-------------------------------------------------------------------------------


.. method:: ctx.const_mertens()

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns the Mertens constant. See also  Wikipedia :cite:p:`WikipediaFun1024`, MathWorld :cite:p:`WolframFun1024`, Mpmath :cite:p:`MpmathFun1024`. 


    Represents the Mertens or Meissel-Mertens constant, which is the
    prime number analog of Euler's constant:

    .. math :: B_1 = \lim_{N\to\infty} \left(\sum_{p_k \le N} \frac{1}{p_k} - \log \log N \right)

    Here `p_k` denotes the `k`-th prime number. Other names for this
    constant include the Hadamard-de la Vallee-Poussin constant or
    the prime reciprocal constant.

    Beispielsweise:


    .. math ::  M=\gamma +\sum _{k=2}^{\infty }{\frac {\mu (k)}{k}}\log {\bigg (}\zeta (k){\bigg )}

    where `\mu (n)` denotes the  Möbius function and `\zeta (n)` the Riemann zeta function. 

    The following gives the Mertens constant to 50 digits::

        >>> from mpfunlab import *
        >>> mp.dps = 50; mp.pretty = True
        >>> +mertens
        0.2614972128476427837554268386086958590515666482612




.. _rst_mpm_const_twinprime: 

Mpmath: Twin prime constant
-------------------------------------------------------------------------------


.. method:: ctx.const_twinprime()

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.



    Returns the Twin prime constant. See also  Wikipedia :cite:p:`WikipediaFun1025`, MathWorld :cite:p:`WolframFun1025`, Mpmath :cite:p:`MpmathFun1025`. 



    Represents the twin prime constant, which is the factor `C_2` featuring in the Hardy-Littlewood conjecture for the growth of the twin prime counting function,

    .. math ::

        \pi_2(n) \sim 2 C_2 \frac{n}{\log^2 n}.

    It is given by the product over primes

    .. math :: C_2 = \prod_{p\ge3} \frac{p(p-2)}{(p-1)^2} \approx 0.66016

    See also code in mpmath: mpmath/libmp/gammazeta.py,  def twinprime_fixed(prec)

    See also code in mpmath: mpmath/libmp/libintmath.py,  def moebius(n)


    Flajolet and Vardi (1996) give series with accelerated convergence (see mathworld)

    .. math ::  C_2 = \prod_{n=2} ^ {\infty} \left[ \zeta(n)(1-2^{-n})  \right]^{-I_n}, \quad \text{with } I_n = \frac{1}{n} \sum_{d|n} \mu(d) 2^{n/d}.



    Computing `C_2` to 50 digits::

        >>> from mpfunlab import *
        >>> mp.dps = 50; mp.pretty = True
        >>> +twinprime
        0.66016181584686957392781211001455577843262336028473





.. _rst_mpm_cyclotomic: 

Mpmath: Cyclotomic polynomial
-------------------------------------------------------------------------------


.. method:: ctx.cyclotomic(n, x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns the cyclotomic polynomial. See also  Wikipedia :cite:p:`WikipediaFun1029`, MathWorld :cite:p:`WolframFun1029`, Mpmath :cite:p:`MpmathFun1029`. 

    Evaluates the cyclotomic polynomial `\Phi_n(x)`, defined by

    .. math :: \Phi_n(x) = \prod_{\zeta} (x - \zeta)

    where `\zeta` ranges over all primitive `n`-th roots of unity (see :ref:`unitroots() <rst_mpm_unitroots>`). An equivalent representation, used for computation, is

    .. math :: \Phi_n(x) = \prod_{d\mid n}(x^d-1)^{\mu(n/d)} = \Phi_n(x)

    where `\mu(m)` denotes the Moebius function. 


    The definition as a product over primitive roots may be checked by computing the product explicitly (for a real argument, this method will generally introduce numerical noise in the imaginary part)::

        >>> mp.dps = 25
        >>> z = 3+4j
        >>> cyclotomic(10, z)
        (-419.0 - 360.0j)
        >>> fprod(z-r for r in unitroots(10, primitive=True))
        (-419.0 - 360.0j)
        >>> z = 3
        >>> cyclotomic(10, z)
        61.0
        >>> fprod(z-r for r in unitroots(10, primitive=True))
        (61.0 - 3.146045605088568607055454e-25j)





.. _rst_mpm_stirling1: 

Mpmath: Stirling number of the first kind
-------------------------------------------------------------------------------


.. method:: ctx.stirling1(n, k, exact=False)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns the Stirling number of the first kind. See also  Wikipedia :cite:p:`WikipediaFun1026`, MathWorld :cite:p:`WolframFun1026`, NIST :cite:p:`DLMFun1026`, Mpmath :cite:p:`MpmathFun1026`. 


    Gives the Stirling number of the first kind `s(n,k)`, defined by

    .. math ::

        x(x-1)(x-2)\cdots(x-n+1) = \sum_{k=0}^n s(n,k) x^k.

    The value is computed using an integer recurrence. The implementation
    is not optimized for approximating large values quickly.

    **Examples**

    Comparing with the generating method::

        >>> from xlcalcnet import *
        >>> mp.dps = 25; mp.pretty = True
        >>> taylor(lambda x: ff(x, 5), 0, 5)
        [0.0, 24.0, -50.0, 35.0, -10.0, 1.0]
        >>> [stirling1(5, k) for k in range(6)]
        [0.0, 24.0, -50.0, 35.0, -10.0, 1.0]

    Recurrence relation::

        >>> n, k = 5, 3
        >>> stirling1(n+1,k) + n*stirling1(n,k) - stirling1(n,k-1)
        0.0

    Pass ``exact=True`` to obtain exact values of Stirling numbers as integers::

        >>> stirling1(42, 5)
        -2.864498971768501633736628e+50
        >>> print(stirling1(42, 5, exact=True))
        -286449897176850163373662803014001546235808317440000




.. _rst_mpm_stirling2: 

Mpmath: Stirling number of the second kind
-------------------------------------------------------------------------------


.. method:: ctx.stirling2(n, k, exact=False)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.



    Returns the Stirling number of the second kind. See also  Wikipedia :cite:p:`WikipediaFun1027`, MathWorld :cite:p:`WolframFun1027`, NIST :cite:p:`DLMFun1026`, Mpmath :cite:p:`MpmathFun1027`. 


    Gives the Stirling number of the second kind `S(n,k)`, defined by

    .. math ::

        x^n = \sum_{k=0}^n S(n,k) x(x-1)(x-2)\cdots(x-k+1)

    The value is computed using integer arithmetic to evaluate a power sum.
    The implementation is not optimized for approximating large values quickly.

    **Examples**

    Comparing with the generating method::

        >>> from xlcalcnet import *
        >>> mp.dps = 25; mp.pretty = True
        >>> taylor(lambda x: sum(stirling2(5,k) * ff(x,k) for k in range(6)), 0, 5)
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

    Recurrence relation::

        >>> n, k = 5, 3
        >>> stirling2(n+1,k) - k*stirling2(n,k) - stirling2(n,k-1)
        0.0

    Pass ``exact=True`` to obtain exact values of Stirling numbers as integers::

        >>> stirling2(52, 10)
        2.641822121003543906807485e+45
        >>> print(stirling2(52, 10, exact=True))
        2641822121003543906807485307053638921722527655


        

.. _rst_mpm_polyexp: 

Mpmath: CODE!! Polyexponential function
-------------------------------------------------------------------------------


.. method:: ctx.polyexp(s, z)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.



    Returns the polyexponential function. See  Mpmath :cite:p:`MpmathFun1020`. 


    Evaluates the polyexponential function, defined for arbitrary complex `s`, `z` by the series

    .. math ::

        E_s(z) = \sum_{k=1}^{\infty} \frac{k^s}{k!} z^k.

    `E_s(z)` is constructed from the exponential function analogously
    to how the polylogarithm is constructed from the ordinary
    logarithm; as a function of `s` (with `z` fixed), `E_s` is an L-series
    It is an entire function of both `s` and `z`.

    The polyexponential function provides a generalization of the
    Touchard polynomials to noninteger orders `n`.
    In terms of the Bell polynomials,

    .. math ::

        E_s(z) = e^z B_s(z) - \mathrm{sinc}(\pi s).

    Note that `B_n(x)` and `e^{-x} E_n(x)` are identical if `n`
    is a nonzero integer, but not otherwise. In particular, they differ
    at `n = 0`.

    **Examples**

    Evaluating a series::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> nsum(lambda k: sqrt(k)/fac(k), [1,inf])
        2.101755547733791780315904
        >>> polyexp(0.5,1)
        2.101755547733791780315904

    Evaluation for arbitrary arguments::

        >>> polyexp(-3-4j, 2.5+2j)
        (2.351660261190434618268706 + 1.202966666673054671364215j)

    Evaluation is accurate for tiny function values::

        >>> polyexp(4, -100)
        3.499471750566824369520223e-36

    If `n` is a nonpositive integer, `E_n` reduces to a special
    instance of the hypergeometric function `\,_pF_q`::

        >>> n = 3
        >>> x = pi
        >>> polyexp(-n,x)
        4.042192318847986561771779
        >>> x*hyper([1]*(n+1), [2]*(n+1), x)
        4.042192318847986561771779







Mpmath, DAMath: Moebius function, `\mu(n)`
-------------------------------------------------------------------------------

.. method:: math53.moebius(n) 

    Returns `\mu(n)`, the Möbius function.

    For integer `n`, the Moebius `\mu` function `\mu(n)` equals 0 if `n` has repeated integer factors. Otherwise, if `n` is the product of `k` distinct primes, the Moebius `\mu` function `\mu(n)` equals `(-1)^k`.


    https://en.wikipedia.org/wiki/M%C3%B6bius_function


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Moebius(3)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Moebius)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Moebius(3)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Moebius)
        Gpr('5.3518479027559984754E-1')




