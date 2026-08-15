

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />





|newpage|

Characteristic functions of statistical distributions
==============================================================






Uniform distribution
---------------------------------------------


The uniform distribution is a continuous probability distribution  on the support interval `[a, b]` with finite `a < b`.
See also Wikipedia :cite:p:`WikipediaDis24`, MathWorld :cite:p:`WolframDis24`, BoostMath :cite:p:`BoostDis24`, :cite:t:`CharfunDis24`, R (Statistical System) :cite:p:`RDis24`.



Returns `C_X(t)`, the characteristic function of a random variable `X`, following a uniform distribution:

.. math:: C_X(t) =  \frac{e^{itb} - e^{ita}}{it(b-a)}, \quad \text{for } t\ne 0, 0  \text{ otherwise}.




An example in C\#

.. code-block:: csharp

    double a = 0.0;
    double b = 1.0;
    Complex i1 = Complex.ImaginaryOne;
    Complex fz = 1.0;
    if (t != 0.0)
    {
        fz = Complex.Exp(i1 * t * b) - Complex.Exp(i1 * t * a);
        fz /= (i1 * t * (b - a));
    }
    var y = fz.Real;
    var z = -fz.Imaginary;
    var x = t;




Below are 3D plots of this functions with different parameters, and `t \in (t_0, t_1)`:


|Path_Func_CfUniform_a| `\quad` |Path_Func_CfUniform_b| `\quad` |Path_Func_CfUniform_c|

.. |Path_Func_CfUniform_a| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfUniform_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfUniform_b| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfUniform_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfUniform_c| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfUniform_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Characteristic function of the uniform distribution, with `a=0.0`, `b=1.0`, `t_0=-20.0` and  `t_1=20.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Middle figure**: Characteristic function of the uniform distribution, with `a=0`, `b=1`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Right figure**: Characteristic function of the uniform distribution, with `a=0`, `b=1`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.





|newpage|

Normal distribution
-------------------------------------------------


The normal distribution is a continuous probability distribution with mean `\mu \in \mathbb{R}`,  standard deviation `\sigma > 0`, and the support interval `(-\infty, +\infty)`.
See also Wikipedia :cite:p:`WikipediaDis20`, MathWorld :cite:p:`WolframDis20`, BoostMath :cite:p:`BoostDis20`, R (Statistical System) :cite:p:`RDis20`, Mpmath :cite:p:`MpmathFun07c`, Mpmath :cite:p:`MpmathFun07d`.


Returns `C_X(t)`, the characteristic function of a random variable `X`, following a normal distribution:

.. math:: C_X(t) = \exp \left( i \mu t - \tfrac{1}{2} \sigma^2 t^2 \right).



An example in C\#

.. code-block:: csharp

    double mu = 10.0;
    double sigma = 1.0;
    Complex i1 = Complex.ImaginaryOne;
    Complex fz = Complex.Zero;
    fz = Complex.Exp(i1 * t * mu - 0.5 * sigma * sigma * t * t);
    var y = fz.Real;
    var z = -fz.Imaginary;
    var x = t;




Below are 3D plots of this functions with different parameters, and `t \in (t_0, t_1)`:


|Path_Func_CfNormal_a| `\quad` |Path_Func_CfNormal_b| `\quad` |Path_Func_CfNormal_c|

.. |Path_Func_CfNormal_a| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfNormal_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfNormal_b| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfNormal_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfNormal_c| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfNormal_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Characteristic function of the normal distribution, with `\mu=10`, `\sigma=1`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Middle figure**: Characteristic function of the normal distribution, with `\mu=0`, `\sigma=1`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Right figure**: Characteristic function of the normal distribution, with `\mu=0`, `\sigma=1`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.






|newpage|

Chi-squared distribution
------------------------------------------------------

The chi-squared distribution is a continuous probability distribution with `n > 0` degrees of freedom and the support interval `(0,+\infty)`.
See also Wikipedia :cite:p:`WikipediaDis06`, MathWorld :cite:p:`WolframDis06`, BoostMath :cite:p:`BoostDis06`, :cite:t:`CharfunDis06`, R (Statistical System) :cite:p:`RDis06`.


Returns `C_X(t)`, the characteristic function of a random variable `X`, following a chi-squared distribution:

.. math:: C_X(t) = (1-2it)^{-n/2}.



An example in C\#

.. code-block:: csharp

    double nu = 100.0;
    Complex i1 = Complex.ImaginaryOne;
    Complex fz = Complex.Zero;
    fz = Complex.Pow(1 - 2 * i1 * t, -nu / 2);
    var x = fz.Real;
    var y = -fz.Imaginary;
    var z = t;



Below are 3D plots of this functions with different parameters, and `t \in (t_0, t_1)`:


|Path_Func_CfChiSquared_a| `\quad` |Path_Func_CfChiSquared_b| `\quad` |Path_Func_CfChiSquared_c|

.. |Path_Func_CfChiSquared_a| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfChiSquared_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfChiSquared_b| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfChiSquared_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfChiSquared_c| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfChiSquared_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Characteristic function of the chi-squared distribution, with `n=100`, `t_0=-0.2` and  `t_1=0.2`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Middle figure**: Characteristic function of the chi-squared distribution, with `n=10`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Right figure**: Characteristic function of the chi-squared distribution, with `n=10`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.









|newpage|

Beta distribution
-----------------------------------------------------


The beta distribution is a continuous probability distribution with parameters `a > 0`,  `b > 0`, and the support interval `(0, 1)`.
See also Wikipedia :cite:p:`WikipediaDis08`, MathWorld :cite:p:`WolframDis08`, BoostMath :cite:p:`BoostDis08`, :cite:t:`CharfunDis08`, R (Statistical System) :cite:p:`RDis08`.


Returns `C_X(t)`, the characteristic function of a random variable `X`, following a beta  distribution:

.. math:: C_X(t) = {}_1F_1 (a, a+b; it).

where `{}_1F_1()` is Kummer's confluent hypergeometric function (of the first kind).



An example in C\#

.. code-block:: csharp

    double a = 10.0;
    double b = 20.0;
    Complex i1 = Complex.ImaginaryOne;
    var fz = dcplx.zero();
    fz = cmath53.hyperg_1f1(a, a + b, i1 * t);
    var y = fz.Real;
    var z = -fz.Imaginary;
    var x = t;



Below are 3D plots of this functions with different parameters, and `t \in (t_0, t_1)`:


|Path_Func_CfBeta_a| `\quad` |Path_Func_CfBeta_b| `\quad` |Path_Func_CfBeta_c|

.. |Path_Func_CfBeta_a| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfBeta_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfBeta_b| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfBeta_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfBeta_c| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfBeta_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Characteristic function of the beta distribution, with `a=10`, `b=20`, `t_0=-40.0` and  `t_1=40.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Middle figure**: Characteristic function of the beta distribution, with `a=20`, `b=40`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Right figure**: Characteristic function of the beta distribution, with `a=20`, `b=40`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.








|newpage|

F distribution
--------------------------------------------------


The Fisher `F`-distribution is a continuous probability distribution with `m > 0` and  `n > 0` degrees of freedom, and the support interval `(0, +\infty)`.
See also Wikipedia :cite:p:`WikipediaDis09`, MathWorld :cite:p:`WolframDis09`, BoostMath :cite:p:`BoostDis09`, :cite:t:`CharfunDis09`, R (Statistical System) :cite:p:`RDis09`, :cite:t:`AbramowitzDis09`, :cite:t:`Butler2002`, :cite:t:`Chattamvelli1995`, :cite:t:`Witkovsky2001`.


Returns `C_X(t)`, the characteristic function of a random variable `X`, following a central Fisher F distribution:

.. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d}x = \frac{\Gamma(m/2+n/2)}{\Gamma(n/2)}  U \left( \frac{m}{2}, 1-\frac{n}{2}, -\frac{n}{m} it \right)

where `U(\cdot)` denotes the confluent hypergeometric function of the second kind.



An example in C\#

.. code-block:: csharp

    double nu = 21.0;
    double mu = 40.0;
    double G = math53.gamma(mu / 2 + nu / 2) / math53.gamma(nu / 2);
    Complex i1 = Complex.ImaginaryOne;
    var fz = dcplx.zero();
    fz = G * cmath53.hyperg_u(mu / 2, 1 - nu / 2, -(nu / mu) * i1 * t);
    var y = fz.Real;
    var z = -fz.Imaginary;
    var x = t;



Below are 3D plots of this functions with different parameters, and `t \in (t_0, t_1)`:


|Path_Func_CfFisherF_a| `\quad` |Path_Func_CfFisherF_b| `\quad` |Path_Func_CfFisherF_c|

.. |Path_Func_CfFisherF_a| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfFisherF_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfFisherF_b| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfFisherF_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfFisherF_c| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfFisherF_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Characteristic function of the Fisher `F`-distribution, with `m=40`, `n=20`, `t_0=-20.0` and  `t_1=20.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Middle figure**: Characteristic function of the Fisher `F`-distribution, with `m=20`, `n=40`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Right figure**: Characteristic function of the Fisher `F`-distribution, with `m=20`, `n=40`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.









|newpage|

Non-central Chi-squared distribution
----------------------------------------------------------

The noncentral chi-square distribution is a continuous probability distribution with degrees of freedom `n>0`, 
noncentrality parameter `\lambda_1`, and support interval `(0, \infty)`.
See also Wikipedia :cite:p:`WikipediaDis01`, MathWorld :cite:p:`WolframDis01`, :cite:t:`Patnaik1949`, :cite:t:`Penev2000`, :cite:t:`Wang1993`, :cite:t:`Winterbottom1979`, BoostMath :cite:p:`BoostDis01`, :cite:t:`CharfunDis01`, :cite:t:`Kerns2018`, R (Statistical System) :cite:p:`RDis01`, :cite:t:`Yu2011`.



Returns `C_X(t)`, the characteristic function of a random variable `X`, following a non-central chi-squared distribution:

.. math:: C_X(t) = \exp \left(\frac{i \lambda t}{1-2it}\right)  (1-2it)^{-n/2}.



An example in C\#

.. code-block:: csharp

    double nu = 10.0;
    double lambda1 = 50.0;
    Complex i1 = Complex.ImaginaryOne;
    Complex fz = Complex.Zero;
    fz = Complex.Pow(1 - 2 * i1 * t, -nu / 2);
    fz *= Complex.Exp((i1 * t * lambda1) / (1 - 2 * i1 * t));
    var y = fz.Real;
    var z = -fz.Imaginary;
    var x = t;


Below are 3D plots of this functions with different parameters, and `t \in (t_0, t_1)`:


|Path_Func_CfChiSquaredNc_a| `\quad` |Path_Func_CfChiSquaredNc_b| `\quad` |Path_Func_CfChiSquaredNc_c|

.. |Path_Func_CfChiSquaredNc_a| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfChiSquaredNc_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfChiSquaredNc_b| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfChiSquaredNc_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfChiSquaredNc_c| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfChiSquaredNc_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Characteristic function of the noncentral chi-square distribution, with `\lambda=50`, `n=10`, `t_0=-0.2` and  `t_1=0.2`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Middle figure**: Characteristic function of the noncentral chi-square distribution, with `\lambda=20`, `n=40`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Right figure**: Characteristic function of the noncentral chi-square distribution, with `\lambda=20`, `n=40`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.







|newpage|

Binomial distribution
-------------------------------------------------


The binomial distribution is a discrete (lattice) probability distribution  with number of trials `n \ge 0` and success probability `0 \le p \le 1`.
See also  Wikipedia :cite:p:`WikipediaDis33`, MathWorld :cite:p:`WolframDis33`, BoostMath :cite:p:`BoostDis33`, :cite:t:`CharfunDis33`, R (Statistical System) :cite:p:`RDis33`.


Returns `C_X(t)`, the characteristic function of a random variable `X`, following an binomial distribution:

.. math::  C_X(t) = \left(P e^{it} + Q\right)^n.



An example in C\#

.. code-block:: csharp

    double n1 = 20.0;
    double p = 0.5;
    Complex i1 = Complex.ImaginaryOne;
    Complex fz = Complex.Zero;
    fz = Complex.Pow(1 - p + p * Complex.Exp(i1 * t), n1);
    var x = fz.Real;
    var y = -fz.Imaginary;
    var z = t;



Below are 3D plots of this functions with different parameters, and `t \in (t_0, t_1)`:


|Path_Func_CfBinomial_a| `\quad` |Path_Func_CfBinomial_b| `\quad` |Path_Func_CfBinomial_c|

.. |Path_Func_CfBinomial_a| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfBinomial_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfBinomial_b| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfBinomial_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfBinomial_c| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfBinomial_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Characteristic function of the binomial distribution, with `p=0.5`, `n=20`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Middle figure**: Characteristic function of the binomial distribution, with `p=0.5`, `n=40`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Right figure**: Characteristic function of the binomial distribution, with `p=0.5`, `n=40`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.











|newpage|

Hypergeometric distribution
------------------------------------------------------


The hypergeometric distribution is a discrete (lattice) probability distribution  with `k` successes (random draws for which the object drawn has a specified feature) in `n \in \{0, 1 ,2, \ldots, N \}` draws, without replacement, from a finite population of size `N \in \{0, 1 ,2, \ldots \}`` that contains exactly `K \in \{0, 1 ,2, \ldots, N \}` objects with that feature, wherein each draw is either a success or a failure, and the support interval `(\max(0,n+K-N), \min(K,n))`.
See also  Wikipedia :cite:p:`WikipediaDis35`, MathWorld :cite:p:`WolframDis35`, BoostMath :cite:p:`BoostDis35`, R (Statistical System) :cite:p:`RDis35`, :cite:t:`Berkopec2007`, :cite:t:`Johnson2005` page 251.


Returns `C_X(t)`, the characteristic function of a random variable `X`, following an hypergeometric distribution:

.. math::  C_X(t) = {}_2F_1(-n, -K; N-K-n+1; e^{it}) \binom{N-K}{n}  \bigg/  \binom{N}{n} .

where `{}_2F_1(\cdot)` is the Gauss hypergeometric function.



An example in C\#

.. code-block:: csharp

    int N = 50;
    int K = 16;
    int n1 = 12;
    Complex i1 = Complex.ImaginaryOne;
    var fz = dcplx.zero();
    fz = cmath53.hyperg_2f1(-n1, -K, N - K - n1 + 1, cmath53.exp(i1 * t));
    fz = fz * math53.binomial(N - K, n1) / math53.binomial(N, n1);
    var x = fz.Real;
    var y = -fz.Imaginary;
    var z = t;


Below are 3D plots of this functions with different parameters, and `t \in (t_0, t_1)`:


|Path_Func_CfHypergeo_a| `\quad` |Path_Func_CfHypergeo_b| `\quad` |Path_Func_CfHypergeo_c|

.. |Path_Func_CfHypergeo_a| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfHypergeo_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfHypergeo_b| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfHypergeo_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_CfHypergeo_c| image:: ../_static/PathSurfaces/CharFunc/Path_Func_CfHypergeo_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Characteristic function of the hypergeometric distribution, with `N=50`, `K=16`, `n=12`, `t_0=-10.0` and  `t_1=10.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Middle figure**: Characteristic function of the hypergeometric distribution, with `N=50`, `K=10`, `n=4`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.

**Right figure**: Characteristic function of the hypergeometric distribution, with `N=50`, `K=10`, `n=4`, `t_0=-2.0` and  `t_1=2.0`. Perspective camera. Camera angles are `\theta=120^\circ` and `\phi = 120^\circ`.










|newpage|

Distribution of Wilks' `\Lambda` 
-----------------------------------------------------


The Wilks' `\Lambda` distribution is a continuous probability distribution with `p \ge 1` predictor variables, error degress of freedom `m \ge 1` and `n \ge 1`, and the support interval `(0,1)`.
See also: :cite:t:`Anderson2003`, :cite:t:`Muirhead1982`, :cite:t:`Butler2007`, :cite:t:`Pham-Gia2008`, :cite:t:`CharfunDis1001`, :cite:t:`CharfunDis1002`.



Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of Wilks' Lambda:

.. math:: C_X(t) = \frac{\Gamma_p(n/2  -it)\Gamma_p((n + m)/2)}{\Gamma_p(n/2)\Gamma_p((n + m)/2  -it)}.


