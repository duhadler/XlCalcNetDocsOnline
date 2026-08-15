

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

Generalized hypergeometric functions
===============================================================================


.. _rst_mpm_hyper: 

Generalized hypergeometric function  `{}_pF_q` 
-------------------------------------------------------------------------------

.. method:: ctx.hyperg_pfq(a_s, b_s, z)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns the generalized hypergeometric function  :sub:`p`\ F\ :sub:`q`\ (a; b, c; z).

    See also MathWorld :cite:p:`WolframFun1065`, MathWorld :cite:p:`WolframFun1065a`, Mpmath :cite:p:`MpmathFun1065`, Wikipedia :cite:p:`WikipediaFun1065`, NIST :cite:p:`DLMFun1065`. 



    Evaluates the generalized hypergeometric function

    .. math ::

        \,_pF_q(a_1,\ldots,a_p; b_1,\ldots,b_q; z) =
        \sum_{n=0}^\infty \frac{(a_1)_n (a_2)_n \ldots (a_p)_n}
           {(b_1)_n(b_2)_n\ldots(b_q)_n} \frac{z^n}{n!}

    where `(x)_n` denotes the rising factorial (see :ref:`rf() <rst_mpm_rf>`).


    The parameters lists ``a_s`` and ``b_s`` may contain integers,
    real numbers, complex numbers, as well as exact fractions given in
    the form of tuples `(p, q)`. The function is optimized to handle
    integers and fractions more efficiently than arbitrary
    floating-point parameters (since rational parameters are by
    far the most common).

    **Examples**

    The parameters can be any combination of integers, fractions,
    floats and complex numbers::

        >>> a, b, c, d, e = 1, (-1,2), pi, 3+4j, (2,3)
        >>> x = 0.2j
        >>> hyper([a,b],[c,d,e],x)
        (0.9923571616434024810831887 - 0.005753848733883879742993122j)
        >>> b, e = -0.5, mpf(2)/3
        >>> fn = lambda n: rf(a,n)*rf(b,n)/rf(c,n)/rf(d,n)/rf(e,n)*x**n/fac(n)
        >>> nsum(fn, [0, inf])
        (0.9923571616434024810831887 - 0.005753848733883879742993122j)

    The `\,_0F_0` and `\,_1F_0` series are just elementary functions::

        >>> a, z = sqrt(2), +pi
        >>> hyper([],[],z)
        23.14069263277926900572909
        >>> exp(z)
        23.14069263277926900572909
        >>> hyper([a],[],z)
        (-0.09069132879922920160334114 + 0.3283224323946162083579656j)
        >>> (1-z)**(-a)
        (-0.09069132879922920160334114 + 0.3283224323946162083579656j)

    If any `a_k` coefficient is a nonpositive integer, the series terminates
    into a finite polynomial::

        >>> hyper([1,1,1,-3],[2,5],1)
        0.7904761904761904761904762
        >>> identify(_)
        '(83/105)'

    If any `b_k` is a nonpositive integer, the function is undefined (unless the
    series terminates before the division by zero occurs)::

        >>> hyper([1,1,1,-3],[-2,5],1)
        Traceback (most recent call last):
          ...
        ZeroDivisionError: pole in hypergeometric series
        >>> hyper([1,1,1,-1],[-2,5],1)
        1.1

    Except for polynomial cases, the radius of convergence `R` of the hypergeometric
    series is either `R = \infty` (if `p \le q`), `R = 1` (if `p = q+1`), or
    `R = 0` (if `p > q+1`).

    The analytic continuations of the functions with `p = q+1`, i.e. `\,_2F_1`,
    `\,_3F_2`,  `\,_4F_3`, etc, are all implemented and therefore these functions
    can be evaluated for `|z| \ge 1`. The shortcuts :ref:`hyp2f1() <rst_mpm_hyp2f1>`, :ref:`hyp3f2() <rst_mpm_hyp3f2>`
    are available to handle the most common cases (see their documentation),
    but functions of higher degree are also supported::

        >>> hyper([1,2,3,4], [5,6,7], 1)   # 4F3 at finite-valued branch point
        1.141783505526870731311423
        >>> hyper([4,5,6,7], [1,2,3], 1)   # 4F3 at pole
        +inf
        >>> hyper([1,2,3,4,5], [6,7,8,9], 10)    # 5F4
        (1.543998916527972259717257 - 0.5876309929580408028816365j)
        >>> hyper([1,2,3,4,5,6], [7,8,9,10,11], 1j)   # 6F5
        (0.9996565821853579063502466 + 0.0129721075905630604445669j)

    Near `z = 1` with noninteger parameters::

        >>> hyper(['1/3',1,'3/2',2], ['1/5','11/6','41/8'], 1)
        2.219433352235586121250027
        >>> hyper(['1/3',1,'3/2',2], ['1/5','11/6','5/4'], 1)
        +inf
        >>> eps1 = extradps(6)(lambda: 1 - mpf('1e-6'))()
        >>> hyper(['1/3',1,'3/2',2], ['1/5','11/6','5/4'], eps1)
        2923978034.412973409330956

    Please note that, as currently implemented, evaluation of `\,_pF_{p-1}`
    with `p \ge 3` may be slow or inaccurate when `|z-1|` is small,
    for some parameter values.

    Evaluation may be aborted if convergence appears to be too slow.
    The optional ``maxterms`` (limiting the number of series terms) and ``maxprec``
    (limiting the internal precision) keyword arguments can be used
    to control evaluation::

        >>> hyper([1,2,3], [4,5,6], 10000)
        Traceback (most recent call last):
          ...
        NoConvergence: Hypergeometric series converges too slowly. Try increasing maxterms.
        >>> hyper([1,2,3], [4,5,6], 10000, maxterms=10**6)
        7.622806053177969474396918e+4310

    Additional options include ``force_series`` (which forces direct use of
    a hypergeometric series even if another evaluation function might work better)
    and ``asytol`` which controls the target tolerance for using
    asymptotic series.

    When `p > q+1`, ``hyper`` computes the (iterated) Borel sum of the divergent
    series. For `\,_2F_0` the Borel sum has an analytic solution and can be
    computed efficiently (see :ref:`hyp2f0() <rst_mpm_hyp2f0>`). For higher degrees, the functions
    is evaluated first by attempting to sum it directly as an asymptotic
    series (this only works for tiny `|z|`), and then by evaluating the Borel
    regularized sum using numerical integration. Except for
    special parameter combinations, this can be extremely slow.

        >>> hyper([1,1], [], 0.5)          # regularization of 2F0
        (1.340965419580146562086448 + 0.8503366631752726568782447j)
        >>> hyper([1,1,1,1], [1], 0.5)     # regularization of 4F1
        (1.108287213689475145830699 + 0.5327107430640678181200491j)

    With the following magnitude of argument, the asymptotic series for `\,_3F_1`
    gives only a few digits. Using Borel summation, ``hyper`` can produce
    a value with full accuracy::

        >>> mp.dps = 15
        >>> hyper([2,0.5,4], [5.25], '0.08', force_series=True)
        Traceback (most recent call last):
          ...
        NoConvergence: Hypergeometric series converges too slowly. Try increasing maxterms.
        >>> hyper([2,0.5,4], [5.25], '0.08', asytol=1e-4)
        1.0725535790737
        >>> hyper([2,0.5,4], [5.25], '0.08')
        (1.07269542893559 + 5.54668863216891e-5j)
        >>> hyper([2,0.5,4], [5.25], '-0.08', asytol=1e-4)
        0.946344925484879
        >>> hyper([2,0.5,4], [5.25], '-0.08')
        0.946312503737771
        >>> mp.dps = 25
        >>> hyper([2,0.5,4], [5.25], '-0.08')
        0.9463125037377662296700858

    Note that with the positive `z` value, there is a complex part in the
    correct result, which falls below the tolerance of the asymptotic series.

    By default, a parameter that appears in both ``a_s`` and ``b_s`` will be removed
    unless it is a nonpositive integer. This generally speeds up evaluation
    by producing a hypergeometric function of lower order.
    This optimization can be disabled by passing ``eliminate=False``.

        >>> hyper([1,2,3], [4,5,3], 10000)
        1.268943190440206905892212e+4321
        >>> hyper([1,2,3], [4,5,3], 10000, eliminate=False)
        Traceback (most recent call last):
          ...
        NoConvergence: Hypergeometric series converges too slowly. Try increasing maxterms.
        >>> hyper([1,2,3], [4,5,3], 10000, eliminate=False, maxterms=10**6)
        1.268943190440206905892212e+4321

    If a nonpositive integer `-n` appears in both ``a_s`` and ``b_s``, this parameter
    cannot be unambiguously removed since it creates a term 0 / 0.
    In this case the hypergeometric series is understood to terminate before
    the division by zero occurs. This convention is consistent with Mathematica.
    An alternative convention of eliminating the parameters can be toggled
    with ``eliminate_all=True``:

        >>> hyper([2,-1], [-1], 3)
        7.0
        >>> hyper([2,-1], [-1], 3, eliminate_all=True)
        0.25
        >>> hyper([2], [], 3)
        0.25






.. _rst_mpm_hyp2f3: 

Generalized hypergeometric function  `{}_2F_3` 
-------------------------------------------------------------------------------

.. method:: ctx.hyperg_2f3(a1, a2, b1, b2, b3, z)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns the generalized hypergeometric function  :sub:`2`\ F\ :sub:`3`\ ().

    See also MathWorld :cite:p:`WolframFun1063`, MathWorld :cite:p:`WolframFun1063a`, Mpmath :cite:p:`MpmathFun1063`, Wikipedia :cite:p:`WikipediaFun1065`, NIST :cite:p:`DLMFun1065`. 



    Gives the hypergeometric function `\,_2F_3(a_1,a_2;b_1,b_2,b_3; z)`.
    The call ``hyp2f3(a1,a2,b1,b2,b3,z)`` is equivalent to
    ``hyper([a1,a2],[b1,b2,b3],z)``.

    Evaluation works for arbitrarily large arguments::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a1,a2,b1,b2,b3 = 1.5, (-1,3), 2.25, 4, (1,5)
        >>> hyp2f3(a1,a2,b1,b2,b3,10**20)
        -4.169178177065714963568963e+8685889590
        >>> hyp2f3(a1,a2,b1,b2,b3,-10**20)
        7064472.587757755088178629
        >>> hyp2f3(a1,a2,b1,b2,b3,10**20*j)
        (-5.163368465314934589818543e+6141851415 + 1.783578125755972803440364e+6141851416j)
        >>> hyp2f3(2+3j, -2j, 0.5j, 4j, -1-j, 10-20j)
        (-2280.938956687033150740228 + 13620.97336609573659199632j)
        >>> hyp2f3(2+3j, -2j, 0.5j, 4j, -1-j, 10000000-20000000j)
        (4.849835186175096516193e+3504 - 3.365981529122220091353633e+3504j)






.. _rst_mpm_hyp3f2: 

Generalized hypergeometric function  `{}_3F_2` 
-------------------------------------------------------------------------------

.. method:: ctx.hyperg_3f2(a1, a2, a3, b1, b2, z)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns the generalized hypergeometric function  :sub:`3`\ F\ :sub:`2`\ ().

    See also MathWorld :cite:p:`WolframFun1064`, MathWorld :cite:p:`WolframFun1064a`, Mpmath :cite:p:`MpmathFun1064`, Wikipedia :cite:p:`WikipediaFun1065`, NIST :cite:p:`DLMFun1065`. 


    The function is defined for `|z| < 1` as

    .. math :: 

        \,_3F_2(a_1,a_2,a_3,b_1,b_2,z) = \sum_{k=0}^{\infty}
            \frac{(a_1)_k (a_2)_k (a_3)_k}{(b_1)_k (b_2)_k} \frac{z^k}{k!}.

    and for `|z| \ge 1` by analytic continuation. The analytic structure of this
    function is similar to that of `\,_2F_1`, generally with a singularity at
    `z = 1` and a branch cut on `(1, \infty)`.

    Evaluation is supported inside, on, and outside
    the circle of convergence `|z| = 1`::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> hyp3f2(1,2,3,4,5,0.25)
        1.083533123380934241548707
        >>> hyp3f2(1,2+2j,3,4,5,-10+10j)
        (0.1574651066006004632914361 - 0.03194209021885226400892963j)
        >>> hyp3f2(1,2,3,4,5,-10)
        0.3071141169208772603266489
        >>> hyp3f2(1,2,3,4,5,10)
        (-0.4857045320523947050581423 - 0.5988311440454888436888028j)
        >>> hyp3f2(0.25,1,1,2,1.5,1)
        1.157370995096772047567631
        >>> (8-pi-2*ln2)/3
        1.157370995096772047567631
        >>> hyp3f2(1+j,0.5j,2,1,-2j,-1)
        (1.74518490615029486475959 + 0.1454701525056682297614029j)
        >>> hyp3f2(1+j,0.5j,2,1,-2j,sqrt(j))
        (0.9829816481834277511138055 - 0.4059040020276937085081127j)
        >>> hyp3f2(-3,2,1,-5,4,1)
        1.41
        >>> hyp3f2(-3,2,1,-5,4,2)
        2.12

    Evaluation very close to the unit circle::

        >>> hyp3f2(1,2,3,4,5,'1.0001')
        (1.564877796743282766872279 - 3.76821518787438186031973e-11j)
        >>> hyp3f2(1,2,3,4,5,'1+0.0001j')
        (1.564747153061671573212831 + 0.0001305757570366084557648482j)
        >>> hyp3f2(1,2,3,4,5,'0.9999')
        1.564616644881686134983664
        >>> hyp3f2(1,2,3,4,5,'-0.9999')
        0.7823896253461678060196207

    .. note ::

        Evaluation for `|z-1|` small can currently be inaccurate or slow
        for some parameter combinations.

    For various parameter combinations, `\,_3F_2` admits representation in terms
    of hypergeometric functions of lower degree, or in terms of
    simpler functions::

        >>> for a, b, z in [(1,2,-1), (2,0.5,1)]:
        ...     hyp2f1(a,b,a+b+0.5,z)**2
        ...     hyp3f2(2*a,a+b,2*b,a+b+0.5,2*a+2*b,z)
        ...
        0.4246104461966439006086308
        0.4246104461966439006086308
        7.111111111111111111111111
        7.111111111111111111111111

        >>> z = 2+3j
        >>> hyp3f2(0.5,1,1.5,2,2,z)
        (0.7621440939243342419729144 + 0.4249117735058037649915723j)
        >>> 4*(pi-2*ellipe(z))/(pi*z)
        (0.7621440939243342419729144 + 0.4249117735058037649915723j)





.. _rst_mpm_hyp2f2: 

Generalized hypergeometric function  `{}_2F_2`
-------------------------------------------------------------------------------

.. method:: ctx.hyperg_2f2(a1, a2, b1, b2, z)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns the generalized hypergeometric function  :sub:`2`\ F\ :sub:`2`\ (a; b, c; z).

    See also MathWorld :cite:p:`WolframFun1062`, MathWorld :cite:p:`WolframFun1062a`, Mpmath :cite:p:`MpmathFun1062`, Wikipedia :cite:p:`WikipediaFun1065`, NIST :cite:p:`DLMFun1065`. 


    Gives the hypergeometric function `\,_2F_2(a_1,a_2;b_1,b_2; z)`.
    The call ``hyp2f2(a1,a2,b1,b2,z)`` is equivalent to
    ``hyper([a1,a2],[b1,b2],z)``.

    Evaluation works for complex and arbitrarily large arguments::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a, b, c, d = 1.5, (-1,3), 2.25, 4
        >>> hyp2f2(a, b, c, d, 10**20)
        -5.275758229007902299823821e+43429448190325182663
        >>> hyp2f2(a, b, c, d, -10**20)
        2561445.079983207701073448
        >>> hyp2f2(a, b, c, d, 10**20*j)
        (2218276.509664121194836667 - 1280722.539991603850462856j)
        >>> hyp2f2(2+3j, -2j, 0.5j, 4j, 10-20j)
        (80500.68321405666957342788 - 20346.82752982813540993502j)











.. _rst_mpm_hyp2f0: 

Generalized hypergeometric function `\,_2F_0`
-------------------------------------------------------------------------------


.. method:: ctx.hyperg_2f0(a, b, z)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns the generalized hypergeometric function  :sub:`2`\ F\ :sub:`0`\ (a, b; z). See also  Wikipedia :cite:p:`WikipediaFun169`, MathWorld :cite:p:`WolframFun169`, NIST :cite:p:`DLMFun169`, BoostMath :cite:p:`BoostFun169`, Mpmath :cite:p:`MpmathFun169`. 






