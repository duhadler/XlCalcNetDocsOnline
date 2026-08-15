

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}





|newpage|

Q Functions
===============================================================================


.. _rst_mpm_qp: 

q-Pochhammer symbol 
-------------------------------------------------------------------------------

.. method:: ctx.q_pochhammer(a, q=None, n=None)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, or ``gmp``.


    Returns the q-Pochhammer symbol. See also  Wikipedia :cite:p:`WikipediaFun1031`, MathWorld :cite:p:`WolframFun1031`, Mpmath :cite:p:`MpmathFun1031`. 

    Evaluates the q-Pochhammer symbol (or q-rising factorial)

    .. math ::

        (a; q)_n = \prod_{k=0}^{n-1} (1-a q^k)

    where `n = \infty` is permitted if `|q| < 1`. Called with two arguments, ``qp(a,q)`` computes `(a;q)_{\infty}`; with a single argument, ``qp(q)`` computes `(q;q)_{\infty}`. The special case

    .. math ::

        \phi(q) = (q; q)_{\infty} = \prod_{k=1}^{\infty} (1-q^k) =
            \sum_{k=-\infty}^{\infty} (-1)^k q^{(3k^2-k)/2}

    is also known as the Euler function, or (up to a factor `q^{-1/24}`) the Dedekind eta function.


    If `n` is a positive integer, the function amounts to a finite product::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> qp(2,3,5)
        -725305.0
        >>> fprod(1-2*3**k for k in range(5))
        -725305.0
        >>> qp(2,3,0)
        1.0

    Complex arguments are allowed::

        >>> qp(2-1j, 0.75j)
        (0.4628842231660149089976379 + 4.481821753552703090628793j)





.. _rst_mpm_qgamma: 

q-gamma function
-------------------------------------------------------------------------------

.. method:: ctx.q_gamma(z, q)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, or ``gmp``.


    Returns the q-gamma function. See also  Wikipedia :cite:p:`WikipediaFun1032`, MathWorld :cite:p:`WolframFun1032`, NIST :cite:p:`DLMFun1032`, Mpmath :cite:p:`MpmathFun1032`. 


    Evaluates the q-gamma function

    .. math ::  \Gamma_q(z) = \frac{(q; q)_{\infty}}{(q^z; q)_{\infty}} (1-q)^{1-z}.


    Evaluation for real and complex arguments::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> qgamma(4,0.75)
        4.046875
        >>> qgamma(6,6)
        121226245.0
        >>> qgamma(3+4j, 0.5j)
        (0.1663082382255199834630088 + 0.01952474576025952984418217j)

    The q-gamma function satisfies a functional equation similar
    to that of the ordinary gamma method::

        >>> q = mpf(0.25)
        >>> z = mpf(2.5)
        >>> qgamma(z+1,q)
        1.428277424823760954685912
        >>> (1-q**z)/(1-q)*qgamma(z,q)
        1.428277424823760954685912




.. _rst_mpm_qfac: 

q-factorial
-------------------------------------------------------------------------------

.. method:: ctx.q_factorial(z, q)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, or ``gmp``.


    Returns the q-factorial. See also  Wikipedia :cite:p:`WikipediaFun1033`, MathWorld :cite:p:`WolframFun1033`, NIST :cite:p:`DLMFun1033`, Mpmath :cite:p:`MpmathFun1033`. 


    Evaluates the q-factorial,

    .. math :: [n`q! = (1+q)(1+q+q^2)\cdots(1+q+\cdots+q^{n-1})

    or more generally

    .. math :: [z`q! = \frac{(q;q)_z}{(1-q)^z}.

    **Examples**

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> qfac(0,0)
        1.0
        >>> qfac(4,3)
        2080.0
        >>> qfac(5,6)
        121226245.0
        >>> qfac(1+1j, 2+1j)
        (0.4370556551322672478613695 + 0.2609739839216039203708921j)




.. _rst_mpm_qhyper: 

Hypergeometric q-series
-------------------------------------------------------------------------------

.. method:: ctx.q_hyperg(a_s, b_s, q, z)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, or ``gmp``.


    Returns the hypergeometric q-series. See also MathWorld :cite:p:`WolframFun1034`, NIST :cite:p:`DLMFun1034`, Mpmath :cite:p:`MpmathFun1034`. 

    Evaluates the basic hypergeometric series or hypergeometric q-series

    .. math ::

        \,_r\phi_s \left[\begin{matrix}
            a_1 & a_2 & \ldots & a_r \\
            b_1 & b_2 & \ldots & b_s
        \end{matrix} ; q,z \right] =
        \sum_{n=0}^\infty
        \frac{(a_1;q)_n, \ldots, (a_r;q)_n}
                {(b_1;q)_n, \ldots, (b_s;q)_n}
        \left((-1)^n q^{n\choose 2}\right)^{1+s-r}
        \frac{z^n}{(q;q)_n}

    where `(a;q)_n` denotes the q-Pochhammer symbol (see :ref:`qp() <rst_mpm_qp>`).

    **Examples**

    Evaluation works for real and complex arguments::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> qhyper([0.5], [2.25], 0.25, 4)
        -0.1975849091263356009534385
        >>> qhyper([0.5], [2.25], 0.25-0.25j, 4)
        (2.806330244925716649839237 + 3.568997623337943121769938j)
        >>> qhyper([1+j], [2,3+0.5j], 0.25, 3+4j)
        (9.112885171773400017270226 - 1.272756997166375050700388j)






