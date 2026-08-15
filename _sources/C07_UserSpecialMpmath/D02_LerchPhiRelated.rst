

.. |newline| raw:: latex

   \newline



.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

Related to Lerch's phi
===============================================================================




.. _rst_mpm_bernfrac: 

Mpmath: Bernoulli number as fraction
-------------------------------------------------------------------------------


.. method:: mpm.bernfrac(n)


    Returns the Bernoulli number as fraction. See also  Mpmath :cite:p:`MpmathFun80a`. 

    See also: bernoulli_fmpq_ui in ARB

    Returns a tuple of integers `(p, q)` such that `p/q = B_n` exactly,
    where `B_n` denotes the `n`-th Bernoulli number. The fraction is
    always reduced to lowest terms. Note that for `n > 1` and `n` odd,
    `B_n = 0`, and `(0, 1)` is returned.

    **Examples**


    This function works for arbitrarily large `n`::

        >>> p, q = bernfrac(10**4)
        >>> print(q)
        2338224387510
        >>> print(len(str(p)))
        27692
        >>> mp.dps = 15
        >>> print(mpf(p) / q)
        -9.04942396360948e+27677
        >>> print(bernoulli(10**4))
        -9.04942396360948e+27677

    .. note ::

        :ref:`bernoulli() <rst_mpm_bernoulli>` computes a floating-point approximation
        directly, without computing the exact fraction first.
        This is much faster for large `n`.


        

.. _rst_mpm_dirichlet: 

Mpmath: Dirichlet L-Series
-------------------------------------------------------------------------------


.. method:: ctx.dirichlet_l(s, chi, derivative=0)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns the Dirichlet L-function.  See also  Wikipedia :cite:p:`WikipediaFun1009`, MathWorld :cite:p:`WolframFun1009`, NIST :cite:p:`DLMFun1009`,  Mpmath :cite:p:`MpmathFun1009`,  Mpmath :cite:p:`MpmathFun1009`. 

    Evaluates the Dirichlet L-function

    .. math ::  L(s,\chi) = \sum_{k=1}^\infty \frac{\chi(k)}{k^s}.

    where `\chi` is a periodic sequence of length `q` which should be supplied in the form of a list `[\chi(0), \chi(1), \ldots, \chi(q-1)]`. Strictly, `\chi` should be a Dirichlet character, but any periodic sequence will work.

    For example, ``dirichlet(s, [1])`` gives the ordinary
    Riemann zeta function and ``dirichlet(s, [-1,1])`` gives
    the alternating zeta function (Dirichlet eta function).

    Also the derivative with respect to `s` (currently only a first derivative) can be evaluated.


    The ordinary Riemann zeta method::

        >>> from xlcalcnet import *
        >>> mp.dps = 25; mp.pretty = True
        >>> dirichlet(3, [1]); zeta(3)
        1.202056903159594285399738
        1.202056903159594285399738
        >>> dirichlet(1, [1])
        +inf

    The alternating zeta method::

        >>> dirichlet(1, [-1,1]); ln(2)
        0.6931471805599453094172321
        0.6931471805599453094172321


        

.. _rst_mpm_nzeros: 

Mpmath: Number of zeros of the Riemann zeta function
-------------------------------------------------------------------------------

.. method:: ctxflint.zeta_nzeros(n)



    Returns the number of zeros of the Riemann zeta function.  See also  Wikipedia :cite:p:`WikipediaFun1011`, MathWorld :cite:p:`WolframFun1011`, NIST :cite:p:`DLMFun1011`, Flint :cite:p:`FlintFun1011`, Mpmath :cite:p:`MpmathFun1012`.

    This calls ``acb_dirichlet_zeta_nzeros``.

    Computes the number of zeros of the Riemann zeta function in `(0,1) \times (0,t]`, usually denoted by `N(t)`.




    An example :

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; t = 10000
        >>> \mathrm{d}z = dec.nzeros(t); mz = mpm.nzeros(t); gz = gmp.nzeros(t)
        >>> fz = fpm.nzeros(t); az = apm.nzeros(t)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.0142000000000000000E+4
        mpm: 1.0142000000000000000e+4
        gmp: 1.0142000000000000000E+04
        fpm: 1.01420000000000E+04
        apm: 1.0142000000000000000e+4 (0.0%)





.. _rst_mpm_secondzeta: 

Mpmath: Secondary zeta function
-------------------------------------------------------------------------------


.. method:: ctx.secondzeta(s, a=0.015)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.



    Returns the secondary zeta function. See also Mpmath :cite:p:`MpmathFun1022`, :cite:t:`Voros2003`, :cite:t:`Voros2009`, :cite:t:`Voros2009`.


    Evaluates the secondary zeta function `Z(s)`, defined for `\mathrm{Re}(s)>1` by

    .. math :: Z(s) = \sum_{n=1}^{\infty} \frac{1}{\tau_n^s}

    where `\frac12+i\tau_n` runs through the zeros of `\zeta(s)` with imaginary part positive.

    `Z(s)` extends to a meromorphic function on `\mathbb{C}`  with a double pole at `s=1` and  simple poles at the points `-2n` for `n=0`,  1, 2, ...

    **Examples**

        >>> from mpfunlab import *
        >>> mp.pretty = True; mp.dps = 15
        >>> secondzeta(2)
        0.023104993115419
        >>> xi = lambda s: 0.5*s*(s-1)*pi**(-0.5*s)*gamma(0.5*s)*zeta(s)
        >>> Xi = lambda t: xi(0.5+t*j)
        >>> chop(-0.5*diff(Xi,0,n=2)/Xi(0))
        0.023104993115419

    We may ask for an approximate error value::

        >>> secondzeta(0.5+100j, error=True)
        ((-0.216272011276718 - 0.844952708937228j), 2.22044604925031e-16)







