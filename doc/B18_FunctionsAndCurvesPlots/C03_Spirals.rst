

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />








|newpage|


Spirals
==============================================================




Archimedes' spiral
---------------------------------------------------------------------------

.. method:: User.ArchimedesSpiral(a, Resolution, AsPolar = false)


    The  parametric equations of Archimedes' Spiral are

    .. math:: r(t) = a t,

    .. math:: x(t) = r \cos(t),

    .. math:: y(t) = r \sin(t).

    Changing the parameter `a` controls the distance between loops.


    See also  Wikipedia :cite:p:`Wikipedia2D209`,  MathWorld :cite:p:`Wolfram2D209`, MathCurve :cite:p:`MathCurve2D209`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')



    |Archimedes_Spiral_a| `\quad` |Archimedes_Spiral_b| `\quad` |Archimedes_Spiral_c|

    .. |Archimedes_Spiral_a| image:: ../_static/ParametricCurves/Spirals/Archimedes_Spiral.*
       :width: 30 %

    .. |Archimedes_Spiral_b| image:: ../_static/ParametricCurves/Spirals/Archimedes_Spiral.*
       :width: 30 %

    .. |Archimedes_Spiral_c| image:: ../_static/ParametricCurves/Spirals/Archimedes_Spiral.*
       :width: 30 %





    **Left figure**: Archimedes Spiral


    **Middle figure**: Archimedes Spiral


    **Right figure**: Archimedes Spiral






|newpage|


Fermat's spiral
---------------------------------------------------------------------------

.. method:: User.FermatSpiral(a, Resolution, AsPolar = false)



    The parametric equations of Fermat' spiral are

    .. math:: r(t) = \pm a \sqrt{t},

    .. math:: x(t) = r \cos(t),

    .. math:: y(t) = r \sin(t).

    Changing the parameter `a` controls the distance between loops.


    See also  Wikipedia :cite:p:`Wikipedia2D210`,  MathWorld :cite:p:`Wolfram2D210`,  MathCurve :cite:p:`Wikipedia2D210`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')


    |Fermats_Spiral_a| `\quad` |Fermats_Spiral_b| `\quad` |Fermats_Spiral_c|

    .. |Fermats_Spiral_a| image:: ../_static/ParametricCurves/Spirals/Fermat_Spiral.*
       :width: 30 %

    .. |Fermats_Spiral_b| image:: ../_static/ParametricCurves/Spirals/Fermat_Spiral.*
       :width: 30 %

    .. |Fermats_Spiral_c| image:: ../_static/ParametricCurves/Spirals/Fermat_Spiral.*
       :width: 30 %





    **Left figure**: Fermat's Spiral.


    **Middle figure**: Fermat's Spiral.


    **Right figure**: Fermat's Spiral.











|newpage|


Hyperbolic Spiral
---------------------------------------------------------------------------

.. method:: User.HyperbolicSpiral(a, Resolution, AsPolar = false)



    The parametric equations of the hyperbolic spiral are

    .. math:: r(t) = \frac{a}{t},

    .. math:: x(t) = r \cos(t),

    .. math:: y(t) = r \sin(t).

    Changing the parameter `a` controls the distance between loops.



    See also  Wikipedia :cite:p:`Wikipedia2D211`,  MathWorld :cite:p:`Wolfram2D211`,  MathCurve :cite:p:`MathCurve2D211`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    |Hyperbolic_Spiral_a| `\quad` |Hyperbolic_Spiral_b| `\quad` |Hyperbolic_Spiral_c|

    .. |Hyperbolic_Spiral_a| image:: ../_static/ParametricCurves/Spirals/Hyperbolic_Spiral.*
       :width: 30 %

    .. |Hyperbolic_Spiral_b| image:: ../_static/ParametricCurves/Spirals/Hyperbolic_Spiral.*
       :width: 30 %

    .. |Hyperbolic_Spiral_c| image:: ../_static/ParametricCurves/Spirals/Hyperbolic_Spiral.*
       :width: 30 %





    **Left figure**: Hyperbolic Spiral.


    **Middle figure**: Hyperbolic Spiral.


    **Right figure**: Hyperbolic Spiral.







|newpage|


Lituus
---------------------------------------------------------------------------

.. method:: User.Lituus(a, Resolution, AsPolar = false)



    The parametric equations of the Lituus are

    .. math:: r(t) = \frac{a}{\sqrt{t}},

    .. math:: x(t) = r \cos(t),

    .. math:: y(t) = r \sin(t).

    Changing the parameter `a` controls the distance between loops.



    See also  Wikipedia :cite:p:`Wikipedia2D212`,  MathWorld :cite:p:`Wolfram2D212`,  MathCurve :cite:p:`MathCurve2D212`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    |Lituus_a| `\quad` |Lituus_b| `\quad` |Lituus_c|

    .. |Lituus_a| image:: ../_static/ParametricCurves/Spirals/Lituus.*
       :width: 30 %

    .. |Lituus_b| image:: ../_static/ParametricCurves/Spirals/Lituus.*
       :width: 30 %

    .. |Lituus_c| image:: ../_static/ParametricCurves/Spirals/Lituus.*
       :width: 30 %





    **Left figure**: Lituus.


    **Middle figure**: Lituus.


    **Right figure**: Lituus.










|newpage|


Logarithmic Spiral
------------------------------------------------------------------------

.. method:: User.LogarithmicSpiral(a, Resolution, AsPolar = false)



    The parametric equations of the logarithmic spiral are

    .. math:: r(t) = a \exp(k t),

    .. math:: x(t) = r \cos(t),

    .. math:: y(t) = r \sin(t).

    where `a>0` and `k \ne 0` are real constants.



    See also  Wikipedia :cite:p:`Wikipedia2D213`,  MathWorld :cite:p:`Wolfram2D213`,  MathCurve :cite:p:`MathCurve2D213`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')



    |Logarithmic_Spiral_a| `\quad` |Logarithmic_Spiral_b| `\quad` |Logarithmic_Spiral_c|

    .. |Logarithmic_Spiral_a| image:: ../_static/ParametricCurves/Spirals/Logarithmic_Spiral.*
       :width: 30 %

    .. |Logarithmic_Spiral_b| image:: ../_static/ParametricCurves/Spirals/Logarithmic_Spiral.*
       :width: 30 %

    .. |Logarithmic_Spiral_c| image:: ../_static/ParametricCurves/Spirals/Logarithmic_Spiral.*
       :width: 30 %





    **Left figure**: Logarithmic Spiral.


    **Middle figure**: Logarithmic Spiral.


    **Right figure**: Logarithmic Spiral.





|newpage|


Poinsot's Spiral
------------------------------------------------------------------------

.. method:: User.PoinsotSpiral(a, Resolution, AsPolar = false)



    The parametric equations of the Poinsot spiral are

    .. math:: r(t) = \frac{a}{\alpha \cosh(k t) + \beta \sinh(k t)}, \quad \text{with } \alpha^2 + \beta^2 \ne 0.

    .. math:: x(t) = r \cos(t),

    .. math:: y(t) = r \sin(t).

    where `a>0` and `k \ne 0` are real constants.



    See also  Wikipedia :cite:p:`Wikipedia2D219`,  MathWorld :cite:p:`Wolfram2D219`,  MathCurve :cite:p:`MathCurve2D219`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')


    |Poinsot_Spiral_1_a| `\quad` |Poinsot_Spiral_2_a|

    .. |Poinsot_Spiral_1_a| image:: ../_static/ParametricCurves/Spirals/PoinsotSpiral1.*
       :width: 30 %

    .. |Poinsot_Spiral_2_a| image:: ../_static/ParametricCurves/Spirals/PoinsotSpiral1.*
       :width: 30 %






    **Left figure**: Poinsot's Spiral, type 1.


    **Middle figure**: Poinsot's Spiral, type 2.








|newpage|


Cotes's spiral
------------------------------------------------------------------------

.. method:: User.CotesSpiral(a, Resolution, AsPolar = false)


    The shape of spirals in the family depends on the parameters. The curves in polar coordinates, `(r, \theta), r>0` are defined by one of the following five equations:

    .. math:: 
        \frac{1}{r} = 
        \begin{cases}
         A \cosh(k\theta + \varepsilon) \\
         A \exp(k\theta + \varepsilon) \\
         A \sinh(k\theta + \varepsilon) \\
         A (k\theta + \varepsilon) \\
         A \cos(k\theta + \varepsilon) \\
        \end{cases}



    `A > 0`, `k > 0` and `\varepsilon` are arbitrary real  constants. `A` determines the size, `k` determines the shape, and `\varepsilon` determines the angular position of the spiral.

    The first and third forms are Poinsot's spirals; the second is the logarithmic spiral; the fourth is the hyperbolic spiral; the fifth is the epispiral. 


    See also  Wikipedia :cite:p:`Wikipedia2D220`,  MathWorld :cite:p:`Wolfram2D220`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')


    |Cotes_spiral_case_1_a| `\quad` |Cotes_spiral_case_1_b| `\quad` |Cotes_spiral_case_1_c|

    .. |Cotes_spiral_case_1_a| image:: ../_static/ParametricCurves/Spirals/Cotes_Spiral.*
       :width: 30 %

    .. |Cotes_spiral_case_1_b| image:: ../_static/ParametricCurves/Spirals/Cotes_Spiral.*
       :width: 30 %

    .. |Cotes_spiral_case_1_c| image:: ../_static/ParametricCurves/Spirals/Cotes_Spiral.*
       :width: 30 %





    **Left figure**: Cote's Spirals.


    **Middle figure**: Cote's Spirals.


    **Right figure**: Cote's Spirals.





|newpage|


Tanh Spiral
------------------------------------------------------------------------

.. method:: User.TanhSpiral(a, Resolution, AsPolar = false)


    This is a spiral proposed by Bourke :cite:p:`Bourke2D221`, and also discussed by  Meier :cite:p:`Meier2D221`. It has the following parametric equations:



    .. math:: x(t) = \frac{\sinh(2t)}{\cos(2at) + \cosh(2t)},

    .. math:: y(t) = \frac{\sin(2at)}{\cos(2at) + \cosh(2t)},

    with `-\pi/2 \le t \le \pi/2` and `a>0` (eg:2).



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    |Tanh_Spiral_a| `\quad` |Tanh_Spiral_b| `\quad` |Tanh_Spiral_c|

    .. |Tanh_Spiral_a| image:: ../_static/ParametricCurves/Spirals/Tanh_Spiral.*
       :width: 30 %

    .. |Tanh_Spiral_b| image:: ../_static/ParametricCurves/Spirals/Tanh_Spiral.*
       :width: 30 %

    .. |Tanh_Spiral_c| image:: ../_static/ParametricCurves/Spirals/Tanh_Spiral.*
       :width: 30 %





    **Left figure**: Tanh Spiral.


    **Middle figure**: Tanh Spiral.


    **Right figure**: Tanh Spiral.





|newpage|


Nielsens Spiral
------------------------------------------------------------------------

.. method:: User.NielsenSpiral(a, Resolution, AsPolar = false)


    Nielsen's spiral, also called the sici spiral is the spiral with parametric equations


    .. math:: x(t) = a \cdot \mathrm{ci}(t),

    .. math:: y(t) = a \cdot  \mathrm{si}(t),

    where `\mathrm{ci}(t)` is the cosine integral and `\mathrm{si}(t)` is the sine integral. 



    See also  Wikipedia :cite:p:`Wikipedia2D217`,  MathWorld :cite:p:`Wolfram2D217`,  MathCurve :cite:p:`MathCurve2D217`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')



    |Nielsens_Spiral_a| `\quad` |Nielsens_Spiral_b| `\quad` |Nielsens_Spiral_c|

    .. |Nielsens_Spiral_a| image:: ../_static/ParametricCurves/Spirals/Nielsens_Spiral.*
       :width: 30 %

    .. |Nielsens_Spiral_b| image:: ../_static/ParametricCurves/Spirals/Nielsens_Spiral.*
       :width: 30 %

    .. |Nielsens_Spiral_c| image:: ../_static/ParametricCurves/Spirals/Nielsens_Spiral.*
       :width: 30 %





    **Left figure**: Nielsens Spiral.


    **Middle figure**: Nielsens Spiral.


    **Right figure**: Nielsens Spiral.





|newpage|


Cornu Spiral
------------------------------------------------------------------------

.. method:: User.CornuSpiral(a, Resolution, AsPolar = false)


    The Cornu spiral, also known as a Euler spiral or clothoid, is the curve generated by a parametric plot of S(t) against C(t). A Cornu spiral has the property that its curvature at any point is proportional to the distance along the spiral, measured from the origin.


    .. math:: x(t) = a \cdot C(t),

    .. math:: y(t) = a \cdot S(t),

    where `C(t)` and `S(t)` are the Fresnel integrals.


    See also  Wikipedia :cite:p:`Wikipedia2D218`,  MathWorld :cite:p:`Wolfram2D218`,  MathCurve :cite:p:`MathCurve2D218`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    |Cornu_Spiral_a| `\quad` |Cornu_Spiral_b| `\quad` |Cornu_Spiral_c|

    .. |Cornu_Spiral_a| image:: ../_static/ParametricCurves/Spirals/Cornu_Spiral.*
       :width: 30 %

    .. |Cornu_Spiral_b| image:: ../_static/ParametricCurves/Spirals/Cornu_Spiral.*
       :width: 30 %

    .. |Cornu_Spiral_c| image:: ../_static/ParametricCurves/Spirals/Cornu_Spiral.*
       :width: 30 %





    **Left figure**: Cornu Spiral.


    **Middle figure**: Cornu Spiral.


    **Right figure**: Cornu Spiral.







