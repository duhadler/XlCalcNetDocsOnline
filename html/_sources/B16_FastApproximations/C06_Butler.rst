







.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />





|newpage|


Approximations based on hypergeometric functions of scalar argument
===============================================================================

See also :cite:t:`Koev2006`, :cite:t:`Butler2002a`, :cite:t:`Butler2007`.





.. _rst_hypermat_1f1_butler: 

Hypergeometric function `{}_1F_1` for matrix argument (Butler's approximation)
-----------------------------------------------------------------------------------


.. method:: ctx.hypermat_1f1_butler(res, a, b, X)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns Butler's approximation to Kummer's confluent hypergeometric function for matrix argument, `{}_1F_1(a;b;\textbf{T})`, which is defined as (see {NIST})

    .. math:: {}_1F_1(a;b;\textbf{T}) = \sum_{k=0}^\infty \frac{1}{k!}  \sum_{|\kappa|=k}  \frac{\left[a\right]{\kappa}}{\left[b\right]{\kappa}} Z_{\kappa}(\textbf{T})

    with `-b+\tfrac{1}{2}(j+1) \notin  \mathbb{N}, 1 \leq j \leq m; ||\textbf{T}||<1`. Here `Z_{\kappa}(\textbf{T})` is a zonal polynomial.


    Butler's approximation takes the form

    .. math:: {}_1{F}_1(a;b;X)  \approx \frac{b^{pb-p(p+1)/4}}{\sqrt{R_{1,1}}}  \times \prod_{i=1}^p \left[\left(\frac{y_i}{a}\right)^a \left(\frac{1-y_i}{b-a} \right)^{b-a} e^{x_i y_i}  \right], \quad \text{where } 

    .. math:: X=\text{diag}(x_1,\ldots,x_p,	y_i=\frac{2a}{b-x_i+\sqrt{(x_i-b)^2 + 4ax_i}}, \text{ and }

    .. math:: R_{1,1} = \prod_{i=1}^p  \prod_{j=i}^p \left[\frac{y_i y_j}{a}+\frac{(1-y_i)(1-y_j)}{b-a}\right]. 



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.hypermat_1f1_butler(x, nu, nc); mx = mpm.hypermat_1f1_butler(x, nu, nc)
        >>> ix = ipm.hypermat_1f1_butler(x, nu, nc); fx = fpm.hypermat_1f1_butler(x, nu, nc)
        >>> gx = gmp.hypermat_1f1_butler(x, nu, nc); ax = apm.hypermat_1f1_butler(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





Comparisons with MATLAB: some results
-------------------------------------------------------------------------------

Text for examples

Matlab insert


EXAMPLE 1:
CF of log MeansRatio RV with and n = 5 and alpha = 7/2

.. code-block:: matlab
   :linenos:

   n     = 5;
   alpha = 7/2;
   t     = linspace(-100,100,201);
   cf    = cf_LogRV_MeansRatioW(t,n,alpha);
   figure; plot(t,real(cf),t,imag(cf)); grid on;
   title('CF of log MeansRatio RV with and n = 5 and alpha = 7/2')









.. _rst_hypermat_2f1_butler: 

Hypergeometric function `{}_2F_1` for matrix argument (Butler's approximation)
------------------------------------------------------------------------------------------


.. method:: ctx.hypermat_2f1_butler(res, a, b, c, X)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns Butler's approximation to the Gauss hypergeometric function for matrix argument, `{}_2F_1(a, b; c; \textbf{T})`, which is defined as (see {NIST})

    .. math:: {}_2F_1(a,b;c;\textbf{T}) = \sum_{k=0}^\infty \frac{1}{k!}  \sum_{|\kappa|=k}  \frac{\left[a\right]{\kappa}\left[b\right]{\kappa}}{\left[c\right]{\kappa}} Z_{\kappa}(\textbf{T})


    with `-c+\tfrac{1}{2}(j+1) \notin  \mathbb{N}, 1 \leq j \leq m; ||\textbf{T}||<1`. Here `Z_{\kappa}(\textbf{T})` is a zonal polynomial.


    Butler's approximation takes the form

    .. math:: {}_2{F}_1(a,b;c;X)  \approx \frac{c^{pc-p(p+1)/4}}{\sqrt{R_{2,1}}}   \times \prod_{i=1}^p \left[\left(\frac{y_i}{a}\right)^a \left(\frac{1-y_i}{c-a} \right)^{c-a} (1-x_i y_i)^{-b}  \right],

    where `X=\text{diag}(x_1,\ldots,x_p)`, `S_i = x_i y_i (1-y_i)/(1-x_i y_i)`, `\tau_i = x_i(b-a)-c`,

    .. math:: y_i=\frac{2a}{\sqrt{t_i^2 - 4ax_i(c-b)}-\tau_i}, \text{ and } 

    .. math:: R_{2,1} = \prod_{i=1}^p  \prod_{j=i}^p \left[\frac{y_i y_j}{a}+\frac{(1-y_i)(1-y_j)}{c-a}-\frac{b}{a(c-a)} S_i S_j   \right]. 




    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.hypermat_2f1_butler(x, nu, nc); mx = mpm.hypermat_2f1_butler(x, nu, nc)
        >>> ix = ipm.hypermat_2f1_butler(x, nu, nc); fx = fpm.hypermat_2f1_butler(x, nu, nc)
        >>> gx = gmp.hypermat_2f1_butler(x, nu, nc); ax = apm.hypermat_2f1_butler(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





Comparison with MATLAB: some results
-------------------------------------------------------------------------------

Text for examples

Matlab insert


EXAMPLE 1:
CF of log MeansRatio RV with and n = 5 and alpha = 7/2

.. code-block:: matlab
   :linenos:

   n     = 5;
   alpha = 7/2;
   t     = linspace(-100,100,201);
   cf    = cf_LogRV_MeansRatioW(t,n,alpha);
   figure; plot(t,real(cf),t,imag(cf)); grid on;
   title('CF of log MeansRatio RV with and n = 5 and alpha = 7/2')










