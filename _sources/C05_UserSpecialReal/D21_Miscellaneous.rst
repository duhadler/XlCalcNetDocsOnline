

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Miscellaneous functions
===============================================================================



.. _Ctx_LogseriesPdf:

Log-series distribution, pmf
-------------------------------------------------------------------------------


.. method:: Math53.logseries_pmf(k, mu)


    Returns `\text{pmf}(x)`, the value of the probability mass function (:ref:`Pmf <Dist_Pmf>`) of the log-series distribution with mean `mu` and the support interval `(0,+\infty)`, and `0 \le q \le 1`.

    See also  Wikipedia :cite:p:`WikipediaDis97`, MathWorld :cite:p:`WolframDis97`, :cite:t:`Johnson2005`, :cite:t:`Ehrhardt2018` (3.9.17).





    .. math:: \text{pmf}(x) = \frac{-1}{\ln(1-p)} \frac{p^k}{k}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("LogseriesPdf(x, a, b): ", LogseriesPdf(x, a, b))
        >>> print ("dist_logseries(a, b).pdf(x): ", dist_logseries(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00





.. _Ctx_LogseriesCdf:

Log-series distribution, cdf
-------------------------------------------------------------------------------


.. method:: Math53.logseries_cdf(k, mu)

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the log-series distribution with mean `mu` and the support interval `(0,+\infty)`, and `0 \le q \le 1`.

    See also  Wikipedia :cite:p:`WikipediaDis97`, MathWorld :cite:p:`WolframDis97`, :cite:t:`Johnson2005`, :cite:t:`Ehrhardt2018` (3.9.17).

    .. math::  \text{cdf}(x) = 1 + \frac{B(p; k+1, 0)}{\ln(1-p)}.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("LogseriesCdf(x, a, b): ", LogseriesCdf(x, a, b))
        >>> print ("dist_logseries(a, b).cdf(x): ", dist_logseries(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00





.. _Ctx_ZetaPmf:

Zeta distribution, pmf
-------------------------------------------------------------------------------


.. method:: Math53.zeta_pmf(k, r)


    Returns `\text{pmf}(x)`, the value of the probability mass function (:ref:`Pmf <Dist_Pmf>`) of the zeta distribution with parameter `r`, and `0 \le q \le 1`.


    See also  Wikipedia :cite:p:`WikipediaDis103`, :cite:t:`Rinne2008`, :cite:t:`Johnson2005` page 527, :cite:t:`Ehrhardt2018` (3.9.34).


    .. math:: \text{pmf}_X(k) = \frac{k^{-(r+1)}}{\zeta(r+1)}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("ZetaPdf(x, a, b): ", ZetaPdf(x, a, b))
        >>> print ("dist_zeta(a, b).pdf(x): ", dist_zeta(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00




.. _Ctx_ZetaCdf:

Zeta distribution, cdf
-------------------------------------------------------------------------------


.. method:: Math53.zeta_cdf(k, r)


    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the zeta distribution:

    .. math:: \text{cdf}(x) = \frac{H_k^{r+1}}{\zeta(r+1)} = 1 - \frac{\zeta(r+1, k+1)}{\zeta(r+1)}.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("ZetaCdf(x, a, b): ", ZetaCdf(x, a, b))
        >>> print ("dist_zeta(a, b).cdf(x): ", dist_zeta(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00




        


Voigt function U
-------------------------------------------------------------------------------

.. method:: math53.voigt_u(z)

    Returns the Voigt function U. See also  Wikipedia :cite:p:`WikipediaFun185`, NIST :cite:p:`DLMFun185`.

    The Voigt functions[1] U, V, and H (sometimes called the line broadening function) are defined by

    .. math :: U(x,t)+iV(x,t)={\sqrt {\frac {\pi }{4t}}}e^{z^{2}}\operatorname {erfc} (z)={\sqrt {\frac {\pi }{4t}}}w(iz),

    .. math :: H(a,u)={\frac {U(u/a,1/4a^{2})}{a{\sqrt {\pi }}}},

    where

    .. math :: z=(1-ix)/2{\sqrt {t}},

    erfc is the complementary error function, and w(z) is the Faddeeva function.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.VoigtU(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.VoigtU('0.1')
        ecplx('5.3518479027559984754E-1')







Voigt function V
-------------------------------------------------------------------------------

.. method:: math53.voigt_v(x, t)

    Returns the Voigt function V. See also Wikipedia :cite:p:`WikipediaFun185`, NIST :cite:p:`DLMFun185`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.VoigtV(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.VoigtV('0.1')
        ecplx('5.3518479027559984754E-1')






Voigt function H
-------------------------------------------------------------------------------

.. method:: math53.voigt_h(x, t)

    Returns the Voigt function H. See also Wikipedia :cite:p:`WikipediaFun185`, NIST :cite:p:`DLMFun185`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.VoigtH(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.VoigtH('0.1')
        ecplx('5.3518479027559984754E-1')






Voigt Profile distribution, pdf
-------------------------------------------------------------------------------

.. method:: math53.voigt_profile_pdf(q, a, b)


    Returns `\text{pdf}(x)`, the probability density function of a random variable `X`, following a Voigt Profile distribution with shape `a > 0`, scale `b > 0`, and the support interval `(0, +\infty)`.
    See also  Wikipedia :cite:p:`WikipediaDis56`.


    .. math:: \text{pdf}(x) = V(x; \sigma, \gamma) = \frac{\Re[w(z)]}{\sigma \sqrt{2 \pi}}, \quad \text{where } z = \frac{x + i\gamma}{\sigma \sqrt{\pi}}.



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.VoigtProfilePdf(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.VoigtProfilePdf('0.1')
        ecplx('5.3518479027559984754E-1')



