

.. |newpage| raw:: latex

   \newpage



.. |vspace| raw:: html

   <br />







|newpage|


A quick look at Scipy
=====================================================





Example: Numerical integration
-------------------------------------------------------

See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html#scipy.integrate.quad

**scipy.integrate.quad**

Compute a definite integral.

Integrate func from a to b (possibly infinite interval) using a technique from the Fortran library QUADPACK.

Examples

Calculate `\int_0^4 x^2 \mathrm{d} x` and compare with an analytic result

.. code-block:: pycon

    >>> from scipy import integrate
    >>> import numpy as np
    >>> x2 = lambda x: x**2
    >>> integrate.quad(x2, 0, 4)
    (21.333333333333332, 2.3684757858670003e-13)
    >>> print(4**3 / 3.)  # analytical result
    21.3333333333


Calculate `\int_0^{\infty} e^{-x} \mathrm{d} x`

.. code-block:: pycon

    >>> invexp = lambda x: np.exp(-x)
    >>> integrate.quad(invexp, 0, np.inf)
    (1.0, 5.842605999138044e-11)


Calculate `\int_0^1 x^2 \mathrm{d} x` for `a = 1, 3`

.. code-block:: pycon

    >>> f = lambda x, a: a*x
    >>> y, err = integrate.quad(f, 0, 1, args=(1,))
    >>> y
    0.5
    >>> y, err = integrate.quad(f, 0, 1, args=(3,))
    >>> y
    1.5





Example: One-dimensional root-finding
-------------------------------------------------------

See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root_scalar.html#scipy.optimize.root_scalar

**scipy.optimize.root_scalar**


Examples

Find the root of a simple cubic

.. code-block:: pycon

    >>> from scipy import optimize
    >>> def f(x): return (x**3 - 1)  # only one real root at x = 1

    >>> def fprime(x): return 3*x**2


The ``brentq`` method takes as input a bracket

.. code-block:: pycon

    >>> sol = optimize.root_scalar(f, bracket=[0, 3], method='brentq')
    >>> sol.root, sol.iterations, sol.function_calls
    (1.0, 10, 11)


The ``newton`` method takes as input a single point and uses the derivative(s).

.. code-block:: pycon

    >>> sol = optimize.root_scalar(f, x0=0.2, fprime=fprime, method='newton')
    >>> sol.root, sol.iterations, sol.function_calls
    (1.0, 11, 22)


The function can provide the value and derivative(s) in a single call.

.. code-block:: pycon

    >>> def f_p_pp(x):
        return (x**3 - 1), 3*x**2, 6*x

    >>> sol = optimize.root_scalar(f_p_pp, x0=0.2, fprime=True, method='newton')
    >>> sol.root, sol.iterations, sol.function_calls
    (1.0, 11, 11)

    >>> sol = optimize.root_scalar(f_p_pp, x0=0.2, fprime=True, fprime2=True, method='halley')
    >>> sol.root, sol.iterations, sol.function_calls
    (1.0, 7, 8)











Example: Special functions
-------------------------------------------------------

See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ynp_zeros.html#scipy.special.ynp_zeros

Compute the first four roots of the first derivative of the Bessel function of second kind for order 0 `Y_0'`.

.. code-block:: pycon

    >>> from scipy.special import ynp_zeros
    >>> ynp_zeros(0, 4)
    array([ 2.19714133,  5.42968104,  8.59600587, 11.74915483])

    Plot `Y_0, Y_0'`, and confirm visually that the roots of `Y_0'` are located at local extrema of `Y_0`.

.. code-block:: pycon

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> from scipy.special import yn, ynp_zeros, yvp
    >>> zeros = ynp_zeros(0, 4)
    >>> xmax = 13
    >>> x = np.linspace(0, xmax, 500)
    >>> fig, ax = plt.subplots()
    >>> ax.plot(x, yn(0, x), label=r'$Y_0$')
    >>> ax.plot(x, yvp(0, x, 1), label=r"$Y_0'$")
    >>> ax.scatter(zeros, np.zeros((4, )), s=30, c='r',
               label=r"Roots of $Y_0'$", zorder=5)
    >>> for root in zeros:
            y0_extremum =  yn(0, root)
            lower = min(0, y0_extremum)
            upper = max(0, y0_extremum)
            ax.vlines(root, lower, upper, color='r')
    >>> ax.hlines(0, 0, xmax, color='k')
    >>> ax.set_ylim(-0.6, 0.6)
    >>> ax.set_xlim(0, xmax)
    >>> plt.legend()
    >>> plt.show()



See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ncfdtr.html#scipy.special.ncfdtr

Cumulative distribution function of the non-central F distribution.

The computation time required for this routine is proportional to the noncentrality parameter nc. Very large values of this parameter can consume immense computer resources. This is why the search range is bounded by 10,000.

Examples

.. code-block:: pycon

    >>> import numpy as np
    >>> from scipy import special
    >>> from scipy import stats
    >>> import matplotlib.pyplot as plt

Plot the CDF of the non-central F distribution, for nc=0. Compare with the F-distribution from scipy.stats:

.. code-block:: pycon

    >>> x = np.linspace(-1, 8, num=500)
    >>> dfn = 3
    >>> dfd = 2
    >>> ncf_stats = stats.f.cdf(x, dfn, dfd)
    >>> ncf_special = special.ncfdtr(dfn, dfd, 0, x)

    >>> fig = plt.figure()
    >>> ax = fig.add_subplot(111)
    >>> ax.plot(x, ncf_stats, 'b-', lw=3)
    >>> ax.plot(x, ncf_special, 'r-')
    >>> plt.show()





Example: Linear regression
-------------------------------------------------------

See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html#scipy.stats.linregress

Calculate a linear least-squares regression for two sets of measurements.




Examples

.. code-block:: pycon

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> from scipy import stats
    >>> rng = np.random.default_rng()

Generate some data:

.. code-block:: pycon

    >>> x = rng.random(10)
    >>> y = 1.6*x + rng.random(10)

Perform the linear regression:

.. code-block:: pycon

    >>> res = stats.linregress(x, y)

Coefficient of determination (R-squared):

.. code-block:: pycon

    >>> print(f"R-squared: {res.rvalue**2:.6f}")
    R-squared: 0.717533

Plot the data along with the fitted line:

.. code-block:: pycon

    >>> plt.plot(x, y, 'o', label='original data')
    >>> plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')
    >>> plt.legend()
    >>> plt.show()



Calculate 95% confidence interval on slope and intercept:

    >>> # Two-sided inverse Students t-distribution
    >>> # p - probability, df - degrees of freedom
    >>> from scipy.stats import t
    >>> tinv = lambda p, df: abs(t.ppf(p/2, df))

    >>> ts = tinv(0.05, len(x)-2)
    >>> print(f"slope (95%): {res.slope:.6f} +/- {ts*res.stderr:.6f}")
    slope (95%): 1.453392 +/- 0.743465
    >>> print(f"intercept (95%): {res.intercept:.6f}" f" +/- {ts*res.intercept_stderr:.6f}")
    intercept (95%): 0.616950 +/- 0.544475




    


|newpage|


Statsmodels
-------------------------------------------------------

See also: https://pypi.org/project/statsmodels/

See also: https://github.com/statsmodels/statsmodels

See also: https://www.statsmodels.org/stable/



Statsmodels is a Python package that provides a complement to scipy for statistical computations including descriptive statistics and estimation and inference for statistical models.







|newpage|


Scikit-learn
-------------------------------------------------------

See also: https://pypi.org/project/scikit-learn/

See also: https://github.com/scikit-learn/scikit-learn

See also: https://scikit-learn.org/stable/



Scikit-learn is a Python module for machine learning built on top of SciPy and is distributed under the 3-Clause BSD license.




