

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}





|newpage|

Scalar functions
===============================================================================



Real and complex sine
-------------------------------------------------------------------------------

.. method:: ctxlib.sin(x)

    where ``ctx`` is ``ctx_pm`` (see :ref:`Python contexts <rst_py_groups_of_contexts>` for details), ``ctx53``, ``ctxcpp``, ``ctxflint`` (see :ref:`.NET contexts <rst_net_groups_of_contexts>` for details). The corresponding ``ctx`` python lists are  ``ctxlistreal`` and ``ctxlistcplx``.


    Returns the sine of `x`, `\sin(x)`.  See also  Wikipedia :cite:p:`WikipediaFun31`,  MathWorld :cite:p:`WolframFun31`,  NIST :cite:p:`DLMFun30`,  :cite:t:`Ehrhardt2018` (4.2.55), Flint :cite:p:`FlintFun30`, Flint :cite:p:`FlintFun31`, Mpmath :cite:p:`MpmathFun31`.




|newpage|

.. _rst_mpm_quadratic_equation_roots: 

Quadratic equation
-------------------------------------------------------------------------------

.. method:: ctx.eval_quadratic(x, A, B, C)

    Returns the value of a quadratic polynomial, `A x^2 + B x + C`.



.. method:: ctx.quadratic_equation(A, B, C)

    Returns the roots `x_1, x_2`  of the quadratic equation `A x^2 + B x + C = 0`. See also Wikipedia :cite:p:`WikipediaAlg02`, :cite:t:`Press2007`.  

    See also: https://dlmf.nist.gov/1.11#iii


    .. math :: x_1 = \frac{Q}{A}, \quad x_2 = \frac{C}{Q}, \quad \text{where }  Q = -\frac{1}{2} \left(B + \sqrt{B^2 - 4AC}) \right)

    The sign of the square root is chosen so as to make `\displaystyle \Re(B^* \sqrt{B^2 - 4AC}) \ge 0`, where the asterisk denotes complex conjugation.




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '125'; n = '3'
        >>> \mathrm{d}x = dec.nthroot(x, n); mx = mpm.nthroot(x, n); ix = ipm.nthroot(x, n)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  5.000000000000000000000000000000000000000E+0
        mpm:  5.000000000000000000000000000000000000000e+0
        ipm:  5.000000000000000000000000000000000000000e+0 (2.755e-39%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '125'; n = '3'
        >>> fx = fpm.nthroot(x, n); gx = gmp.nthroot(x, n); ax = apm.nthroot(x, n)
        >>> mpm.show([fx, gx, ax])
        fpm:  5.00000000000000E+00
        gmp:  5.000000000000000000000000000000000000000E+00
        apm:  5.000000000000000000000000000000000000002e+0 (3.673e-39%)







|newpage|


.. _rst_mpm_cubic_equation_monic_roots: 

Monic cubic equation
-------------------------------------------------------------------------------

.. method:: ctx.eval_monic_cubic(x, a, b, c)

    Returns the value of a monic cubic polynomial, `x^3 + a x^2 + b x + c`.


.. method:: ctx.cubic_equation_monic(a, b, c)

    Returns the roots `x_1, x_2, x_3` of the monic cubic equation `x^3 + a x^2 + b x + c = 0`. See also Wikipedia :cite:p:`WikipediaAlg03`, :cite:t:`Press2007`. 

    See also: https://dlmf.nist.gov/1.11#iii


    .. math :: Q = \frac{a^2 - 3b}{9}, \quad R = \frac{2a^3 - 9ab + 27c}{54}.

    If `Q` and `R` are real *and* `R^2 < Q^3`, then the cubic equation has three real roots, with `\displaystyle \theta = \arccos \left( R  Q^{-3/2} \right)`:

    .. math :: x_1 = -2 \sqrt{Q} \cos \left( \frac{\theta}{3} \right) - \frac{a}{3}, \quad  x_2 = -2 \sqrt{Q} \cos \left( \frac{\theta + 2\pi}{3} \right) - \frac{a}{3}, \quad  x_3 = -2 \sqrt{Q} \cos \left( \frac{\theta - 2\pi}{3} \right) - \frac{a}{3}.

    Otherwise, `\displaystyle A = - \left(R + \sqrt{R^2 - Q^3}) \right)^{1/3}`, where the sign of the square root is chosen so as to make `\displaystyle \Re(R^* \sqrt{R^2 - Q^3}) \ge 0`, and the asterisk denotes complex conjugation. Define `B = 0` if `A = 0` and `B = Q / A` if `A \ne 0`. Then the three roots are given by

    .. math :: x_1 = (A + B) - \frac{a}{3}, \quad  x_2 = -\frac{1}{2} (A + B) - \frac{a}{3} + i \frac{\sqrt{3}}{2} (A - B), \quad   x_3 = -\frac{1}{2} (A + B) - \frac{a}{3} - i \frac{\sqrt{3}}{2} (A - B).

    Note that `x_1` is real if `a, b, c` are real.


    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '125'; n = '3'
        >>> \mathrm{d}x = dec.nthroot(x, n); mx = mpm.nthroot(x, n); ix = ipm.nthroot(x, n)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  5.000000000000000000000000000000000000000E+0
        mpm:  5.000000000000000000000000000000000000000e+0
        ipm:  5.000000000000000000000000000000000000000e+0 (2.755e-39%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '125'; n = '3'
        >>> fx = fpm.nthroot(x, n); gx = gmp.nthroot(x, n); ax = apm.nthroot(x, n)
        >>> mpm.show([fx, gx, ax])
        fpm:  5.00000000000000E+00
        gmp:  5.000000000000000000000000000000000000000E+00
        apm:  5.000000000000000000000000000000000000002e+0 (3.673e-39%)




|newpage|

.. _rst_mpm_cubic_equation_roots: 

Cubic equation
-------------------------------------------------------------------------------

.. method:: ctx.eval_cubic(x, A, B, C, D)

    Returns the value of a cubic polynomial, `A x^3 + B x^2 + C x + D`.


.. method:: ctx.cubic_equation(A, B, C, D)

    Returns the roots  `x_1, x_2, x_3` of the cubic equation `A x^3 + B x^2 + C x + D = 0`. See also Wikipedia :cite:p:`WikipediaAlg03`, :cite:t:`Press2007`.  

    See also: https://dlmf.nist.gov/1.11#iii


    This just calls :ref:`CubicEquationMonicRoots(z, a, b, c) <rst_mpm_cubic_equation_monic_roots>`   with `a = B / A, b = C / A, c = D / A`.





    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '125'; n = '3'
        >>> \mathrm{d}x = dec.nthroot(x, n); mx = mpm.nthroot(x, n); ix = ipm.nthroot(x, n)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  5.000000000000000000000000000000000000000E+0
        mpm:  5.000000000000000000000000000000000000000e+0
        ipm:  5.000000000000000000000000000000000000000e+0 (2.755e-39%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '125'; n = '3'
        >>> fx = fpm.nthroot(x, n); gx = gmp.nthroot(x, n); ax = apm.nthroot(x, n)
        >>> mpm.show([fx, gx, ax])
        fpm:  5.00000000000000E+00
        gmp:  5.000000000000000000000000000000000000000E+00
        apm:  5.000000000000000000000000000000000000002e+0 (3.673e-39%)






|newpage|

.. _rst_mpm_quartic_equation_roots: 

Quartic equation
-------------------------------------------------------------------------------

.. method:: ctx.eval_quartic(x, A, B, C, D, E)

    Returns the value of a quartic polynomial, `A x^4 + B x^3 + C x^2 + D x + E`.


.. method:: ctx.quartic_equation(A, B, C, D, E)

    Returns the roots `x_1, x_2, x_3, x_4` of the quartic equation `A x^4 + B x^3 + C x^2 + D x + E = 0`.  See also Wikipedia :cite:p:`WikipediaAlg04`.

    See also: https://dlmf.nist.gov/1.11#iii


    Define  `\displaystyle a = \frac{-3 B^2}{8 A^2} + \frac{C}{A}, \quad b =  \frac{ B^3}{8 A^3} - \frac{BC}{2 A^2} + \frac{D}{A}, \quad c =  \frac{-3 B^4}{256 A^4} + \frac{CB^2}{16 A^3}  - \frac{BD}{4 A^2} + \frac{E}{A}, \quad V = \frac{B}{4 A}`. 



    If `b = 0` then 

    `\displaystyle x_1 = V + Z_1, \quad  x_2 = V - Z_1, \quad  x_3 = V + Z_2, \quad  x_4 = V - Z_2`,

    where `\displaystyle W = \sqrt{a^2 - 4c}, \quad  Z_1 = \sqrt{\tfrac{1}{2}(-a + W)}, \quad  Z_2 = \sqrt{\tfrac{1}{2}(-a - W)}`. 



    If `b \ne 0` then 

    `\displaystyle x_1 = V + \tfrac{1}{2}(W + Z_1), \quad  x_2 = V + \tfrac{1}{2}(W - Z_1), \quad  x_3 = V - \tfrac{1}{2}(W + Z_2), \quad  x_4 = V -\tfrac{1}{2}(W - Z_2)`, 

    where `\displaystyle W = \sqrt{a + 2y}, \quad  Z_1 = \sqrt{-3a - 2y - \frac{2b}{W}}, \quad  Z_2 = \sqrt{-3a - 2y + \frac{2b}{W}}`, 

    and `y` is any root of the monic cubic equation `\displaystyle y^3 + ey^2+ fy + g =0`, with `\displaystyle e = \frac{5a}{2}, \quad  f = 2 a^2 -c, \quad  g = \frac{a^3}{2} - \frac{a c}{2} - \frac{b^2}{8}`;

    `y` is calculated as the first root returned by :ref:`CubicEquationMonicRoots(y, e, f, g) <rst_mpm_cubic_equation_monic_roots>`.



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '125'; n = '3'
        >>> \mathrm{d}x = dec.nthroot(x, n); mx = mpm.nthroot(x, n); ix = ipm.nthroot(x, n)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  5.000000000000000000000000000000000000000E+0
        mpm:  5.000000000000000000000000000000000000000e+0
        ipm:  5.000000000000000000000000000000000000000e+0 (2.755e-39%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '125'; n = '3'
        >>> fx = fpm.nthroot(x, n); gx = gmp.nthroot(x, n); ax = apm.nthroot(x, n)
        >>> mpm.show([fx, gx, ax])
        fpm:  5.00000000000000E+00
        gmp:  5.000000000000000000000000000000000000000E+00
        apm:  5.000000000000000000000000000000000000002e+0 (3.673e-39%)





|newpage|

Transscribed from Julia: complex elliptic functions in double precision
-------------------------------------------------------------------------------

Text describing functions





|newpage|

Transscribed from Julia: complex hurwitz function, and related, in double precision
--------------------------------------------------------------------------------------------

Text describing functions




|newpage|

Speeedups for iterative algorithms which require an initial guess
-------------------------------------------------------------------------------

Text describing functions

Inverses of cdfs: inverses of noncentral functions

inverses livk gamma_inva




|newpage|

Examples for matrix functions
-------------------------------------------------------------------------------

Text describing functions

Descriptive statistics via numpy in multiple precision

Multiple linear regression via numpy in multiple precision

Canonical correlation via numpy in multiple precision


Descriptive statistics via Eigen in multiple precision

Multiple linear regression via Eigen in multiple precision

Canonical correlation via Eigen in multiple precision


Levenberg-Marquardt algorithm via Eigen in multiple precision

L-BFGS algorithm via Eigen in multiple precision



