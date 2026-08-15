

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

Appell Functions
===============================================================================


.. _rst_mpm_appellf1: 

Appell function `F_1`
-------------------------------------------------------------------------------

.. method:: ctx.appell_f1(a, b1, b2, c, x, y)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, or ``gmp``.


    Returns the Appell function F\ :sub:`1`\ (). See also Wikipedia :cite:p:`WikipediaFun1070`, MathWorld :cite:p:`WolframFun1070`, MathWorld :cite:p:`WolframFun1070a`, NIST :cite:p:`DLMFun1070`, Mpmath :cite:p:`MpmathFun1070`. 


    Gives the Appell F1 hypergeometric function of two variables,

    .. math ::

        F_1(a,b_1,b_2,c,x,y) = \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}
            \frac{(a)_{m+n} (b_1)_m (b_2)_n}{(c)_{m+n}}
            \frac{x^m y^n}{m! n!}.

    This series is only generally convergent when `|x| < 1` and `|y| < 1`,
    although the function can evaluate an analytic continuation
    with respecto to either variable, and sometimes both.

    **Examples**

    Evaluation is supported for real and complex parameters::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> appellf1(1,0,0.5,1,0.5,0.25)
        1.154700538379251529018298
        >>> appellf1(1,1+j,0.5,1,0.5,0.5j)
        (1.138403860350148085179415 + 1.510544741058517621110615j)






.. _rst_mpm_appellf2: 

Appell function  `F_2`
-------------------------------------------------------------------------------

.. method:: ctx.appell_f2(a, b1, b2, c1, c2, x, y)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, or ``gmp``.


    Returns the Appell function F\ :sub:`2`\ ().See also Wikipedia :cite:p:`WikipediaFun1070`, MathWorld :cite:p:`WolframFun1070`, MathWorld :cite:p:`WolframFun1070a`, NIST :cite:p:`DLMFun1070`, Mpmath :cite:p:`MpmathFun1071`. 


    Gives the Appell F2 hypergeometric function of two variables

    .. math ::

        F_2(a,b_1,b_2,c_1,c_2,x,y) = \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}
            \frac{(a)_{m+n} (b_1)_m (b_2)_n}{(c_1)_m (c_2)_n}
            \frac{x^m y^n}{m! n!}.

    The series is generally absolutely convergent for `|x| + |y| < 1`.

    **Examples**

    Evaluation for real and complex arguments::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> appellf2(1,2,3,4,5,0.25,0.125)
        1.257417193533135344785602
        >>> appellf2(1,-3,-4,2,3,2,3)
        -42.8
        >>> appellf2(0.5,0.25,-0.25,2,3,0.25j,0.25)
        (0.9880539519421899867041719 + 0.01497616165031102661476978j)
        >>> chop(appellf2(1,1+j,1-j,3j,-3j,0.25,0.25))
        1.201311219287411337955192
        >>> appellf2(1,1,1,4,6,0.125,16)
        (-0.09455532250274744282125152 - 0.7647282253046207836769297j)






.. _rst_mpm_appellf3: 

Appell function  `F_3`
-------------------------------------------------------------------------------

.. method:: ctx.appell_f3(a1, a2, b1, b2, c, x, y)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, or ``gmp``.


    Returns the Appell function F\ :sub:`3`\ ().See also Wikipedia :cite:p:`WikipediaFun1070`, MathWorld :cite:p:`WolframFun1070`, MathWorld :cite:p:`WolframFun1070a`, NIST :cite:p:`DLMFun1070`, Mpmath :cite:p:`MpmathFun1072`. 


    Gives the Appell F3 hypergeometric function of two variables

    .. math ::

        F_3(a_1,a_2,b_1,b_2,c,x,y) = \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}
            \frac{(a_1)_m (a_2)_n (b_1)_m (b_2)_n}{(c)_{m+n}}
            \frac{x^m y^n}{m! n!}.

    The series is generally absolutely convergent for `|x| < 1, |y| < 1`.

    **Examples**

    Evaluation for various parameters and variables::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> appellf3(1,2,3,4,5,0.5,0.25)
        2.221557778107438938158705
        >>> appellf3(1,2,3,4,5,6,0); hyp2f1(1,3,5,6)
        (-0.5189554589089861284537389 - 0.1454441043328607980769742j)
        (-0.5189554589089861284537389 - 0.1454441043328607980769742j)
        >>> appellf3(1,-2,-3,1,1,4,6)
        -17.4
        >>> appellf3(1,2,-3,1,1,4,6)
        (17.7876136773677356641825 + 19.54768762233649126154534j)
        >>> appellf3(1,2,-3,1,1,6,4)
        (85.02054175067929402953645 + 148.4402528821177305173599j)
        >>> chop(appellf3(1+j,2,1-j,2,3,0.25,0.25))
        1.719992169545200286696007






.. _rst_mpm_appellf4: 

Appell function  `F_4`
-------------------------------------------------------------------------------

.. method:: ctx.appell_f4(a, b, c1, c2, x, y)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, or ``gmp``.


    Returns the Appell function F\ :sub:`4`\ ().See also Wikipedia :cite:p:`WikipediaFun1070`, MathWorld :cite:p:`WolframFun1070`, MathWorld :cite:p:`WolframFun1070a`, NIST :cite:p:`DLMFun1070`, Mpmath :cite:p:`MpmathFun1073`. 


    Gives the Appell F4 hypergeometric function of two variables

    .. math ::

        F_4(a,b,c_1,c_2,x,y) = \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}
            \frac{(a)_{m+n} (b)_{m+n}}{(c_1)_m (c_2)_n}
            \frac{x^m y^n}{m! n!}.

    The series is generally absolutely convergent for
    `\sqrt{|x|} + \sqrt{|y|} < 1`.

    **Examples**

    Evaluation for various parameters and arguments::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> appellf4(1,1,2,2,0.25,0.125)
        1.286182069079718313546608
        >>> appellf4(-2,-3,4,5,4,5)
        34.8
        >>> appellf4(5,4,2,3,0.25j,-0.125j)
        (-0.2585967215437846642163352 + 2.436102233553582711818743j)





