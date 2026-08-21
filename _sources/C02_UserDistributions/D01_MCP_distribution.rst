

.. |newpage| raw:: latex

   \newpage

.. |br| raw:: html

   <br />


Distributions related to multiple comparisons of means
==========================================================








.. _rst_nmax_rho_pdf: 

.. _rst_nmax_rho_cdf: 


Normal maximum distribution, `\rho_{ij, i \ne j} = \rho`: pdf, cdf, qtf, boost class
-------------------------------------------------------------------------------------------

.. method:: math53lib.NmaxRhoPdf(x, rho, k)

.. method:: math53lib.NmaxRhoCdf(x, rho, k)

.. method:: math53lib.NmaxRhoQtf(q, rho, k)

.. method:: math53lib.NmaxRhoDist(rho, k)



Returns the pdf, cdf, qtf or boost class of a random variable `X`, following the distribution of the maximum of `k \ge 2` correlated standard normal variates,  with common correlation `-1/(k-1) \le \rho \le 1` and the support interval `(-\infty, +\infty)`, and `0 \le q \le 1`.

See also :cite:t:`Dunnett1955`, :cite:t:`Bechhofer1988`, :cite:t:`Grubbs1969`, :cite:t:`Bechhofer1988`, :cite:t:`Stoline1979`, and :cite:t:`Hahn1971`.

.. math:: \text{pdf}(x) = f_{\text{nmaxrho}}(x, \rho, k)  = \frac{k}{b} \int_{-\infty}^\infty \left( \Phi(z_1) \right)^{k-1} \phi(z_1) \: \phi(y) \: dy,


.. math:: \text{cdf}(x)= F_{\text{nmaxrho}}(x, \rho, k)  = \int_{-\infty}^\infty \left( \Phi(z_1) \right)^{k} \phi(y) dy, 

.. math:: \text{sf}(x) = 1 -  \int_{-\infty}^\infty \left( \Phi(z_1) \right)^{k} \phi(y) dy, 



where `\displaystyle z_1 = \frac{x+a}{b}`,  `a = y \sqrt{\rho}`, and `b = \sqrt{1-\rho}`. Note that while `z_1` is a complex number for `\rho < 0`, the integral always evaluates to a real number. In the context of the Dunnett t-test with reference sample size `n_0` and common comparator sample size `n_i`, `\displaystyle \rho=\frac{1}{1+n_0/n_i}`. In the context of maximum deviation from the common mean (equal sample sizes), `\displaystyle \rho=-\frac{1}{k-1}`.


There is no known explicit expression for `\text{qtf}(q)` or `\text{isf}(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).



An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.NmaxRhoPdf(x, rho, k)
    ereal('5.2359877559829887307E-1')


An example in Python 

.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.NmaxRhoPdf(x, rho, k)
    ereal('5.2359877559829887307E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.NmaxRhoCdf(x, rho, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NmaxRhoCdf(x, rho, k)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.NmaxRhoQtf(q, rho, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NmaxRhoQtf(q, rho, k)
    ereal('5.3518479027559984754E-1')








|newpage|

.. _rst_nmm_rho_pdf: 

.. _rst_nmm_rho_cdf: 

Normal maximum modulus distribution, `\rho_{ij, i \ne j} = \rho`:  pdf, cdf, qtf, boost class
--------------------------------------------------------------------------------------------------

.. method:: math53lib.NmmRhoPdf(x, rho, k)

.. method:: math53lib.NmmRhoCdf(x, rho, k)

.. method:: math53lib.NmmRhoQtf(q, rho, k)

.. method:: math53lib.NmmRhoDist(rho, k)


Returns the pdf, cdf, qtf or boost class of a random variable `X`, following the distribution of the maximum of the absolute value  of `k \ge 2` correlated standard normal variates,  with common correlation `-1/(k-1) \le \rho \le 1` and the support interval `(0, +\infty)`, and `0 \le q \le 1`.

See also :cite:t:`Dunnett1955`, :cite:t:`Bechhofer1988`, :cite:t:`Grubbs1969`, :cite:t:`Bechhofer1988`, :cite:t:`Stoline1979`, and :cite:t:`Hahn1971`.


.. math:: \text{pdf}(x) = \frac{k}{b} \int_{-\infty}^\infty \left( \Phi(z_1)- \Phi(z_2)  \right)^{k-1} (\phi(z_1)+\phi(z_1)) \: \phi(y) \: dy,

.. math:: \text{cdf}(x)= F_{\text{nmaxrho}}(x, \rho, k)  = \int_{-\infty}^\infty \left( \Phi(z_1) - \Phi(z_2) \right)^{k} \phi(y) dy, 

.. math:: \text{sf}(x) = 1 -  \int_{-\infty}^\infty \left( \Phi(z_1) - \Phi(z_2) \right)^{k} \phi(y) dy, 



where `\displaystyle z_1 = \frac{x+a}{b}`,  `\displaystyle z_2 = \frac{-x+a}{b}`,  `a = y \sqrt{\rho}`, and `b = \sqrt{1-\rho}`. Note that while `z_1` and  `z_2` are complex numbers for `\rho < 0`, the integral always evaluates to a real number. In the context of the Dunnett t-test with reference sample size `n_0` and common comparator sample size `n_i`, `\displaystyle \rho=\frac{1}{1+n_0/n_i}`. In the context of maximum deviation from the common mean (equal sample sizes), `\displaystyle \rho=-\frac{1}{k-1}`.


There is no known explicit expression for `\text{qtf}(q)` or `\text{isf}(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).


An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.NmmRhoPdf(x, rho, k)
    ereal('5.2359877559829887307E-1')


.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.NmmRhoPdf(x, rho, k)
    ereal('5.2359877559829887307E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.NmmRhoCdf(x, rho, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NmmRhoCdf(x, rho, k)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.NmmRhoQtf(q, rho, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NmmRhoQtf(q, rho, k)
    ereal('5.3518479027559984754E-1')















|newpage|

.. _rst_nmax_rhoij_pdf: 

.. _rst_nmax_rhoij_cdf: 


Normal maximum distribution, `\rho_{ij, i \ne j} = \lambda_i \lambda_j`:  pdf, cdf, qtf, boost class
------------------------------------------------------------------------------------------------------

.. method:: math53lib.NmaxRhoijPdf(x, lambda_i, k)

.. method:: math53lib.NmaxRhoijCdf(x, lambda_i, k)

.. method:: math53lib.NmaxRhoijQtf(q, lambda_i, k)

.. method:: math53lib.NmaxRhoijDist(lambda_i, k)


Returns the pdf, cdf, qtf or boost class of a random variable `X`, following the distribution of the maximum deviate of `k \ge 2` correlated standard normal variates,  with common correlation `0 \le \rho \le 1` and the support interval `(-\infty, +\infty)`, and `0 \le q \le 1`.
See also :cite:t:`Dunnett1955`, :cite:t:`Bechhofer1988`, :cite:t:`Grubbs1969`, :cite:t:`Bechhofer1988`, :cite:t:`Stoline1979`, and :cite:t:`Hahn1971`.


.. math:: \text{pdf}(x) = f_{\text{nmaxrhoij}}(x, \rho, k)  = \frac{k}{b} \int_{-\infty}^\infty \left( \Phi(z_1) \right)^{k-1} \phi(z_1) \: \phi(y) \: dy, \quad \text{where}

.. math:: z_1 = \frac{x+a}{b}, \quad  a = y \sqrt{|\rho|}, \quad  b = \sqrt{1-\rho}, \rho = -\frac{1}{k-1}.


.. math:: \text{cdf}(x)= F_{\text{nmaxrhoij}}(x, \rho, k)  = \int_{-\infty}^\infty \left[\Phi \left(\frac{x + \sqrt{\vert \rho \vert} y} {\sqrt{1-\rho}} \right) \right]^n \phi(y) dy , \rho = -\frac{1}{k-1}.

.. math:: \text{sf}(x) = 1 -  \int_{-\infty}^\infty \left[\Phi \left(\frac{x + \sqrt{\vert \rho \vert} y} {\sqrt{1-\rho}} \right) \right]^n \phi(y) dy , \rho = -\frac{1}{k-1}.


For `\lambda_i` = `\sqrt{\rho} \geq 0` for all `i`, this reduces to the equicorrelated case. 

With `\rho_{ij}=\lambda_i  \lambda_j`, we have for a one-sided test:

.. math::  F_n(h;\rho_{ij}) = \int_{-\infty}^\infty \prod_{i=1}^n  \left[\Phi \left(\frac{(a_i-\mu_i)/\sigma_i + \lambda_i z} {\sqrt{1-\lambda_i^2}} \right) \right] \phi(y) dz



There is no known explicit expression for `\text{qtf}(q)` or `\text{isf}(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).



An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.NmaxRhoijPdf(q, rho, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NmaxRhoijPdf(q, rho, k)
    ereal('5.3518479027559984754E-1')


.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.NmaxRhoijPdf(q, rho, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NmaxRhoijPdf(q, rho, k)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.NmaxRhoijCdf(q, rho, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NmaxRhoijCdf(q, rho, k)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.NmaxRhoijQtf(q, rho, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NmaxRhoijQtf(q, rho, k)
    ereal('5.3518479027559984754E-1')









|newpage|

.. _rst_nmm_rhoij_pdf: 

.. _rst_nmm_rhoij_cdf: 


Normal maximum modulus distribution, `\rho_{ij, i \ne j} = \lambda_i \lambda_j`: pdf, cdf, qtf, boost class
---------------------------------------------------------------------------------------------------------------

.. method:: math53lib.NmmRhoijPdf(x, rho, k)

.. method:: math53lib.NmmRhoijCdf(x, rho, k, cdf=True)

.. method:: math53lib.NmmRhoijQtf(q, rho, k, qtf=True)

.. method:: math53lib.NmmRhoijDist(q, rho, k, qtf=True)


Returns the pdf, cdf, qtf or boost class of a random variable `X`, following the distribution of the maximum of `k \ge 2` correlated standard normal variates,  with correlation  `\rho_{ij, i \ne j} = \lambda_i \lambda_j` and the support interval `(-\infty, +\infty)`, and `0 \le q \le 1`.

See also :cite:t:`Dunnett1955`, :cite:t:`Bechhofer1988`, :cite:t:`Grubbs1969`, :cite:t:`Bechhofer1988`, :cite:t:`Stoline1979`, and :cite:t:`Hahn1971`.


.. math:: \text{pdf}(x) = \frac{k}{b} \int_{-\infty}^\infty \left( \Phi(z_1)- \Phi(z_2)  \right)^{k-1} (\phi(z_1)+\phi(z_1)) \: \phi(y) \: dy, \quad \text{where }


.. math:: z_1 = \frac{x+a}{b},  z_2 = \frac{-x+a}{b}, \quad  a = y \sqrt{|\rho|}, \quad  b = \sqrt{1-\rho}, \rho = -\frac{1}{k-1}.


.. math:: \text{cdf}(x) =  \int_{-\infty}^\infty \left[\Phi \left(\frac{x + \sqrt{\vert \rho \vert} y} {\sqrt{1-\rho}} \right) - \Phi \left(\frac{-x + \sqrt{\vert \rho \vert} y} {\sqrt{1-\rho}} \right) \right]^k \phi(y) dy , \rho = -\frac{1}{k-1}.


.. math:: \text{sf}(x) = 1 -  \int_{-\infty}^\infty \left[\Phi \left(\frac{x + \sqrt{\vert \rho \vert} y} {\sqrt{1-\rho}} \right) - \Phi \left(\frac{-x + \sqrt{\vert \rho \vert} y} {\sqrt{1-\rho}} \right) \right]^k \phi(y) dy , \rho = -\frac{1}{k-1}.


For `\lambda_i` = `\sqrt{\rho} \geq 0` for all `i`, this reduces to the equicorrelated case. 

With `\rho_{ij}=\lambda_i  \lambda_j`, we have for a two-sided test:

 .. math::  F_n(h;\rho_{ij}) = \int_{-\infty}^\infty \prod_{i=1}^n  \left[\Phi \left(\frac{(a_i-\mu_i)/\sigma_i + \lambda_i z} {\sqrt{1-\lambda_i^2}} \right) - \Phi \left(\frac{(b_i-\mu_i)/\sigma_i + \lambda_i z} {\sqrt{1-\lambda_i^2}} \right) \right] \phi(y) dz

 
There is no known explicit expression for `\text{qtf}(q)` or `\text{isf}(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).



An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.NmmRhoijPdf(x, rho, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NmmRhoijPdf(x, rho, k)
    ereal('5.3518479027559984754E-1')



.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.NmmRhoijPdf(x, rho, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NmmRhoijPdf(x, rho, k)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.NmmRhoijCdf(x, rho, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NmmRhoijCdf(x, rho, k)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.NmmRhoijQtf(q, rho, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NmmRhoijQtf(q, rho, k)
    ereal('5.3518479027559984754E-1')










|newpage|


.. _rst_mpm_nrange_pdf: 

.. _rst_mpm_nrange_cdf: 


Normal range distribution:  pdf, cdf, qtf, boost class
-------------------------------------------------------------------------------

.. method:: math53lib.NrangePdf(x, k)

.. method:: math53lib.NrangeCdf(n, x)

.. method:: math53lib.NrangeQtf(q, k)

.. method:: math53lib.NrangeDist(k)


Returns the pdf, cdf, qtf or boost class of a random variable `X`, following a normal range distribution, with  `k \ge 2` groups, and the support interval `(0, +\infty)`, and `0 \le q \le 1`.
See also  Wikipedia :cite:p:`WikipediaDis60`, :cite:t:`Harter1960`, :cite:t:`RDis60`.


The density in the central case is given by

.. math:: \text{pdf}(x) = k(k-1)  \int_{-\infty}^\infty \left( \Phi(y) - \Phi(y-x) \right)^{k-2} \phi(y) \phi(y-x) dy


We have

.. math:: \text{cdf}(x) =  k  \int_{-\infty}^\infty \phi(y) \left( \Phi(y) - \Phi(y-x) \right)^{k-1} dy

.. math:: \text{sf}(x) = 1 -   k  \int_{-\infty}^\infty \phi(y) \left( \Phi(y) - \Phi(y-x) \right)^{k-1} dy



In the noncentral case, this becomes

.. math:: \text{cdf}(x) = F_sr \left(m,n,x\right) =  \sum_{i=1}^k  \int_{-\infty}^\infty \phi(y_i - \mu_i) \left( \prod_{i=1, j \neq i}^k (\Phi(y_i - \mu_i) - \Phi(y_i - \mu_i -x) \right) dy_i.


There is no known explicit expression for `\text{qtf}(q)` or `\text{isf}(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).




An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.NrangePdf(x, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NrangePdfxq, k)
    ereal('5.3518479027559984754E-1')



.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.NrangePdf(x, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NrangePdfxq, k)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.NrangeCdf(x, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NrangePdf(x, k)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.NrangeQtf(q, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NrangeQtf(q, k)
    ereal('5.3518479027559984754E-1')








|newpage|


Studentized maximum distribution:  pdf, cdf, qtf, boost class
-------------------------------------------------------------------------------

.. method:: math53lib.SmaxPdf(x, k, nu)

.. method:: math53lib.SmaxCdf(x, k, nu)

.. method:: math53lib.SmaxQtf(q, k, nu)

.. method:: math53lib.SmaxDist(k, nu)


Returns the pdf, cdf, qtf or boost class of a random variable `X`, following a studentized maximum distribution with `k \ge 1` groups, `\nu` error degrees of freedom, and the support interval `(-\infty, +\infty)`, and `0 \le q \le 1`.
See also :cite:t:`Stoline1979`, :cite:t:`Hochberg1987`, :cite:t:`Narula1978`.


.. math:: \text{pdf}(x) = \int_{0}^\infty f_{\text{nnax}}(sx, k) \cdot s \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `f_{\text{nmax}}(\cdot, k)` is the pdf of the normal maximum with `k` groups, and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.


.. math:: \text{cdf}(x) = \int_{0}^\infty F_{\text{nmax}}(sx, k) \cdot \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `F_{\text{nnax}}(\cdot, k)` is the cdf of the normal maximum with `k` groups, and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.

.. math:: \text{sf}(x) = 1 -  \text{cdf}(x)


There is no known explicit expression for `\text{qtf}(q)` or `\text{isf}(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).



An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.SmaxPdf(x, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.SmaxPdf(x, k)
    ereal('5.3518479027559984754E-1')



.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.SmaxPdf(x, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.SmaxPdf(x, k)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.SmaxCdf(x, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.SmaxCdf(x, k)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.SmaxQtf(q, k)
    ereal('5.2359877559829887307E-1')
    >>> ereal.SmaxQtf(q, k)
    ereal('5.3518479027559984754E-1')








|newpage|


Studentized maximum modulus distribution:  pdf, cdf, qtf, boost class
-------------------------------------------------------------------------------

.. method:: math53lib.SmmPdf(x, k, nu)

.. method:: math53lib.SmmCdf(x, k, nu)

.. method:: math53lib.SmmQtf(q, k, nu)

.. method:: math53lib.SmmDist(k, nu)


Returns the pdf, cdf, qtf or boost class of a random variable `X`,  of a random variable `X`, following a studentized maximum modulus distribution  with `k \ge 1` groups, `\nu` error degrees of freedom, and the support interval `(0, +\infty)`, and `0 \le q \le 1`.
See also :cite:t:`Stoline1979`, :cite:t:`Hochberg1987`, :cite:t:`Narula1978`.


.. math:: \text{pdf}(x) = \int_{0}^\infty f_{\text{nmm}}(sx, k) \cdot s \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `f_{\text{nmm}}(\cdot, k)` is the pdf of the normal maximum modulus with `k` groups, and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.



.. math:: \text{cdf}(x) = \int_{0}^\infty F_{\text{nmm}}(sx, k) \cdot \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `F_{\text{nmm}}(\cdot, k)` is the cdf of the normal maximum modulus with `k` groups, and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.

.. math:: \text{sf}(x) = 1 -  \text{cdf}(x)


There is no known explicit expression for `\text{qtf}(q)` or `\text{isf}(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).



An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.SmmPdf(x, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.SmmPdf(x, k, nu)
    ereal('5.3518479027559984754E-1')



.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.SmmPdf(x, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.SmmPdf(x, k, nu)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.SmmCdf(x, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.SmmCdf(x, k, nu)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.SmmQtf(q, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.SmmQtf(q, k, nu)
    ereal('5.3518479027559984754E-1')









|newpage|


Dunnett `t`-distribution, 1-sided:  pdf, cdf, qtf, boost class
-------------------------------------------------------------------------------

.. method:: math53lib.Dunnett1Pdf(x, rho, k, nu)

.. method:: math53lib.Dunnett1Cdf(x, rho, k, nu)

.. method:: math53lib.Dunnett1Qtf(q, rho, k, nu)

.. method:: math53lib.Dunnett1Dist(rho, k, nu)


Returns the pdf, cdf, qtf or boost class of a random variable `X`,  of a random variable `X`, following a 1-sided  Dunnett `t`-distribution with common correlation `\rho`,  `k \ge 2` groups (including control group), error degrees of freedom `\nu`, and the support interval `(-\infty, +\infty)`, and `0 \le q \le 1`.
See also :cite:t:`Dunnett1955`, :cite:t:`Bechhofer1988`.


.. math:: \text{pdf}(x) = \int_{0}^\infty f_{\text{nmaxrho}}(sx, \rho, k) \cdot s \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `f_{\text{nmaxrho}}(\cdot, \rho, k)` is the pdf of the normal maximum (equicorrelated case) with common correlation `\rho` and `k` groups (see :ref:`nmax_rho_pdf() <rst_nmax_rho_pdf>`), and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.



.. math:: \text{cdf}(x) = \int_{0}^\infty F_{\text{nmaxrho}}(sx, \rho, k) \cdot \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `F_{\text{nmaxrho}}(\cdot, \rho, k)` is the cdf of the normal maximum (equicorrelated case) with common correlation `\rho` and `k` groups (see :ref:`nmax_rho_cdf() <rst_nmax_rho_cdf>`), and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.


.. math:: \text{sf}(x) = 1 -  \text{cdf}(x)


There is no known explicit expression for `\text{qtf}(q)` or `\text{isf}(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).




An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.Dunnett1Pdf(x, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.Dunnett1Pdf(x, rho, k, nu)
    ereal('5.3518479027559984754E-1')



.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.Dunnett1Pdf(x, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.Dunnett1Pdf(x, rho, k, nu)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.Dunnett1Cdf(x, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.Dunnett1Cdf(x, rho, k, nu)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.Dunnett1Cdf(q, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.Dunnett1Cdf(q, rho, k, nu)
    ereal('5.3518479027559984754E-1')










|newpage|


Dunnett `t`-distribution, 2-sided:  pdf, cdf, qtf, boost class
-------------------------------------------------------------------------------

.. method:: math53lib.Dunnett2Pdf(x, rho, k, nu)

.. method:: math53lib.Dunnett2Cdf(x, rho, k, nu)

.. method:: math53lib.Dunnett2Qtf(q, rho, k, nu)

.. method:: math53lib.Dunnett2Dist(rho, k, nu)


Returns the pdf, cdf, qtf or boost class of a random variable `X`, following a 2-sided  Dunnett `t`-distribution with common correlation `\rho`,  `k \ge 2` groups (including control group), error degrees of freedom `\nu`, and the support interval `(0, +\infty)`, and `0 \le q \le 1`.
See also :cite:t:`Dunnett1955`, :cite:t:`Bechhofer1988`.


.. math:: \text{pdf}(x) = \int_{0}^\infty f_{\text{nmmrho}}(sx, \rho, k) \cdot s \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `f_{\text{nmmrho}}(\cdot, \rho, k)` is the pdf of the normal maximum modulus (equicorrelated case) with common correlation `\rho` and `k` groups (see :ref:`nmm_rho_pdf() <rst_nmm_rho_pdf>`), and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.


.. math:: \text{cdf}(x) = \int_{0}^\infty F_{\text{nmmrho}}(sx, \rho, k) \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `F_{\text{nmmrho}}(\cdot, \rho, k)` is the cdf of the normal maximum modulus (equicorrelated case) with common correlation `\rho` and `k` groups (see :ref:`nmm_rho_cdf() <rst_nmm_rho_cdf>`), and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.

.. math:: \text{sf}(x) = 1 -  \text{cdf}(x)


There is no known explicit expression for `\text{qtf}(q)` or `\text{isf}(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).




An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.Dunnett2Pdf(x, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.Dunnett2Pdf(x, rho, k, nu)
    ereal('5.3518479027559984754E-1')



.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.Dunnett2Pdf(x, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.Dunnett2Pdf(x, rho, k, nu)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.Dunnett2Cdf(x, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.Dunnett2Cdf(x, rho, k, nu)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.Dunnett2Qtf(q, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.Dunnett2Qtf(q, rho, k, nu)
    ereal('5.3518479027559984754E-1')












|newpage|


Nair `t`-distribution:  pdf, cdf, qtf, boost class
-------------------------------------------------------------------------------

.. method:: math53lib.NairPdf(x, rho, k, nu)

.. method:: math53lib.NairCdf(x, rho, k, nu)

.. method:: math53lib.NairQtf(q, rho, k, nu)

.. method:: math53lib.NairDist(rho, k, nu)


Returns the pdf, cdf, qtf or boost class of a random variable `X`,  of a random variable `X`, following the Nair `t`-distribution with common correlation `\rho`,  `k \ge 2` groups (including control group), error degrees of freedom `\nu`, and the support interval `(-\infty, +\infty)`, and `0 \le q \le 1`.
See also :cite:t:`Dunnett1955`, :cite:t:`Bechhofer1988`.



.. math:: \text{pdf}(x) = \int_{0}^\infty f_{\text{nmaxrho}}(sx, \rho, k) \cdot s \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `f_{\text{nmaxrho}}(\cdot, \rho, k)` is the pdf of the normal maximum (equicorrelated case) with common correlation `\rho` and `k` groups (see :ref:`nmax_rho_pdf() <rst_nmax_rho_pdf>`), and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.


.. math:: \text{cdf}(x) = \int_{0}^\infty F_{\text{nmaxrho}}(sx, \rho, k) \cdot \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `F_{\text{nmaxrho}}(\cdot, \rho, k)` is the cdf of the normal maximum (equicorrelated case) with common correlation `\rho` and `k` groups (see :ref:`nmax_rho_cdf() <rst_nmax_rho_cdf>`), and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.

.. math:: \text{sf}(x) = 1 -  \text{cdf}(x)



An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.NairPdf(x, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NairPdf(x, rho, k, nu)
    ereal('5.3518479027559984754E-1')



.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.NairPdf(x, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NairPdf(x, rho, k, nu)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.NairCdf(x, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NairCdf(x, rho, k, nu)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.NairQtf(q, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.NairQtf(q, rho, k, nu)
    ereal('5.3518479027559984754E-1')


















|newpage|


Halperin `t`-distribution: pdf, cdf, qtf, boost class
-------------------------------------------------------------------------------

.. method:: math53lib.HalperinPdf(x, rho, k, nu)

.. method:: math53lib.HalperinCdf(x, rho, k, nu)

.. method:: math53lib.HalperinQtf(q, rho, k, nu)

.. method:: math53lib.HalperinDist(rho, k, nu)



Returns the pdf, cdf, qtf or boost class of a random variable `X`, following a Halperin `t`-distribution with common correlation `\rho`,  `k \ge 2` groups (including control group), error degrees of freedom `\nu`, and the support interval `(0, +\infty)`, and `0 \le q \le 1`.
See also :cite:t:`Dunnett1955`, :cite:t:`Bechhofer1988`.


.. math:: \text{pdf}(x) = \int_{0}^\infty f_{\text{nmmrho}}(sx, \rho, k) \cdot s \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `f_{\text{nmmrho}}(\cdot, \rho, k)` is the pdf of the normal maximum modulus (equicorrelated case) with common correlation `\rho` and `k` groups (see :ref:`nmm_rho_pdf() <rst_nmm_rho_pdf>`), and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.


.. math:: \text{cdf}(x) = \int_{0}^\infty F_{\text{nmmrho}}(sx, \rho, k) \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `F_{\text{nmmrho}}(\cdot, \rho, k)` is the cdf of the normal maximum modulus (equicorrelated case) with common correlation `\rho` and `k` groups (see :ref:`nmm_rho_cdf() <rst_nmm_rho_cdf>`), and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.


.. math:: \text{sf}(x) = 1 -  \text{cdf}(x)


There is no known explicit expression for `\text{qtf}(q)` or `\text{isf}(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).




An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.HalperinPdf(x, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.HalperinPdf(x, rho, k, nu)
    ereal('5.3518479027559984754E-1')



.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.HalperinPdf(x, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.HalperinPdf(x, rho, k, nu)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.HalperinCdf(x, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.HalperinCdf(x, rho, k, nu)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.HalperinQtf(q, rho, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.HalperinQtf(q, rho, k, nu)
    ereal('5.3518479027559984754E-1')

















|newpage|


Studentized range distribution: pdf, cdf, qtf, boost class
-------------------------------------------------------------------------------

.. method:: math53lib.StdrangePdf(x, k, nu)

.. method:: math53lib.StdrangeCdf(x, k, nu)

.. method:: math53lib.StdrangeQtf(q, k, nu)

.. method:: math53lib.StdrangeDist(k, nu)


Returns the pdf, cdf, qtf or boost class of a random variable `X`, following a studentized range distribution, with  `k \ge 2` groups, `\nu` error degrees of freedom,  and the support interval `(0, +\infty)`, and `0 \le q \le 1`.
See also  Wikipedia :cite:p:`WikipediaDis60`, :cite:t:`Harter1960`, :cite:t:`RDis60`.


.. math:: \text{pdf}(x) = \int_{0}^\infty f_{\text{nrange}}(sx, k) \cdot s \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `f_{\text{nrange}}(\cdot, k)` is the pdf of the normal range with `k` groups (see :ref:`nrange_pdf() <rst_mpm_nrange_pdf>`), and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.


.. math:: \text{cdf}(x) = \int_{0}^\infty F_{\text{nrange}}(sx, k) \cdot \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: ds  

where `F_{\text{nrange}}(\cdot, k)` is the cdf of the normal range with `k` groups (see :ref:`nrange_cdf() <rst_mpm_nrange_cdf>`), and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.


.. math:: \text{sf}(x) = 1 -  \text{cdf}(x)


There is no known explicit expression for `\text{qtf}(q)` or `\text{isf}(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).



An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.StdrangePdf(x, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.StdrangePdf(x, k, nu)
    ereal('5.3518479027559984754E-1')



.. code-block:: pycon

    >>> from xlcalcnet import ereal
    >>> ereal.StdrangePdf(x, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.StdrangePdf(x, k, nu)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.StdrangeCdf(x, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.StdrangeCdf(x, k, nu)
    ereal('5.3518479027559984754E-1')

    >>> from xlcalcnet import ereal
    >>> ereal.StdrangeQtf(q, k, nu)
    ereal('5.2359877559829887307E-1')
    >>> ereal.StdrangeQtf(q, k, nu)
    ereal('5.3518479027559984754E-1')










