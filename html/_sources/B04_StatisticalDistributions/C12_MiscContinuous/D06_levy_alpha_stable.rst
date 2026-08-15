

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




.. _rst_dist_levy_alphastable: 

Lévy alpha-stable distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_levy_alpha_stable(n1, n2, lambda, **kwargs)


    A random variable `X` is called Lévy alpha-stable if its characteristic function, `C_X(t)`, can be written as

    .. math:: C_X(t) = \varphi (t;\alpha ,\beta ,c,\mu )=\exp \left(it\mu -|ct|^{\alpha }\left(1-i\beta \operatorname {sgn} (t)\Phi \right)\right)


    where `sgn(t)` is just the sign of `t` and 

    .. math::  \Phi ={\begin{cases}
             \tan \left({\frac {\pi \alpha }{2}}\right)&\alpha \neq 1\\-{\frac {2}{\pi }}\log |t|&\alpha =1 
         \end{cases}}

    where `\mu \in \mathbb{R}` is a shift parameter.


    See also: Wikipedia :cite:p:`WikipediaDis94`, :cite:t:`CharfunDis94`.




|cr|

.. method:: dist_levy_alpha_stable.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a 
    Lévy alpha stable distribution:

    .. math:: \text{pdf}_X(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{ity} C_X(t) \mathrm{d} y  = \frac{1}{\pi} \int_{0}^{\infty} \Re \left ( e^{-itx} C_X(t) \right ) \mathrm{d} t.

    where `\Re (z)` denotes the real part of `z`.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_levy_alpha_stable(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_levy_alpha_stable.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Lévy alpha stable distribution:

    .. math:: \text{cdf}_X(x) = \frac{1}{2} - \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{e^{-itx} C_X(t) - e^{itx} C_X(t)}{it}  \mathrm{d} t  = \frac{1}{2} - \frac{1}{\pi} \int_{0}^{\infty} \Im \left (    \frac{  e^{-itx} C_X(t)}{t}  \right ) \mathrm{d} t.

    where `\Im (z)` denotes the imaginary part of `z`.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_levy_alpha_stable(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_levy_alpha_stable.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following a Lévy alpha stable distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_levy_alpha_stable(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_levy_alpha_stable.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following a Lévy alpha stable distribution:

    There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: 
    It is computed using Newton iterations with starting values from a normal approximation.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_levy_alpha_stable(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_levy_alpha_stable.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following a Lévy alpha stable distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_levy_alpha_stable(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_levy_alpha_stable.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Lévy alpha stable distribution. The characteristic function can be written as

    .. math:: C_X(t) =  \varphi (t;\alpha ,\beta ,c,\mu )=\exp \left(it\mu -|ct|^{\alpha }\left(1-i\beta \operatorname {sgn} (t)\Phi \right)\right)


    where sgn`(t)` is just the sign of `t` and 

    .. math::  \Phi ={\begin{cases}
             \tan \left({\frac {\pi \alpha }{2}}\right)&\alpha \neq 1\\-{\frac {2}{\pi }}\log |t|&\alpha =1 
         \end{cases}}
   
    where `\mu \in \mathbb{R}` is a shift parameter.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_levy_alpha_stable(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_levy_alpha_stable.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_levy_alpha_stable.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.





|cr|

.. method:: dist_levy_alpha_stable.moments(k)

    Returns ``NaN``, since moments do not exist.



|cr|

.. method:: dist_levy_alpha_stable.cumulants(k)

    Returns ``NaN``, since cumulants do not exist.






**Examples**


A number of cases of analytically expressible stable distributions are known. Let the stable distribution be expressed by 
`f(x;\alpha ,\beta ,c,\mu )`, then we know: 

The Cauchy Distribution is given by `f(x;\alpha=1,\beta=0,c=1,\mu=0)`. 

The Levy distribution is given by `f(x;\alpha={\tfrac {1}{2}},\beta=1,c=1,\mu=0)`.

The Normal distribution is given by `f(x;\alpha=2,\beta=0,c=1,0)`. 


A special case is the Landau distribution, which is given by `f(x;\alpha=1,\beta=1,c=\pi/2,\mu=0)`.


Let `S_{\mu ,\nu }(z)` be a Lommel function, then

.. math:: f\left( x;\alpha={\tfrac {1}{3}},\beta=0,c=1,\mu=0 \right) = \Re \left({\frac {2e^{-{\frac {i\pi }{4}}}}{3{\sqrt {3}}\pi }}{\frac {1}{\sqrt {x^{3}}}}S_{0,{\frac {1}{3}}}\left({\frac {2e^{\frac {i\pi }{4}}}{3{\sqrt {3}}}}{\frac {1}{\sqrt {x}}}\right)\right)


Let  `S(x)` and 
`C(x)` denote the Fresnel Integrals then:

.. math:: f\left(x;\alpha={\tfrac {1}{2}},\beta=0,c=1,\mu=0\right) = {\frac {1}{\sqrt {2\pi |x|^{3}}}}\left(\sin \left({\tfrac {1}{4|x|}}\right)\left[{\frac {1}{2}}-S\left({\tfrac {1}{\sqrt {2\pi |x|}}}\right)\right]+\cos \left({\tfrac {1}{4|x|}}\right)\left[{\frac {1}{2}}-C\left({\tfrac {1}{\sqrt {2\pi |x|}}}\right)\right]\right).


Let `K_{v}(x)` be the modified Bessel function of the second kind then:

.. math:: f\left(x;\alpha={\tfrac {1}{3}},\beta=1,c=1,\mu=0\right) = {\frac {1}{\pi }}{\frac {2{\sqrt {2}}}{3^{\frac {7}{4}}}}{\frac {1}{\sqrt {x^{3}}}}K_{\frac {1}{3}}\left({\frac {4{\sqrt {2}}}{3^{\frac {9}{4}}}}{\frac {1}{\sqrt {x}}}\right)


