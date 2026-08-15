

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />








|newpage|


Decorative curves
==============================================================



Fish curve
--------------------------------------------------------------------------------

.. method:: User.FishCurve(a, Resolution, AsPolar = false)


    The fish curve has the parametric equation


    .. math:: x(t) = a \cos(t) - \frac{a \sin^2(t)}{\sqrt{2}},

    .. math:: y(t) = a \cos(t) \sin(t).


    See also  Wikipedia :cite:p:`Wikipedia2D111`,  MathWorld :cite:p:`Wolfram2D111`, MathCurve :cite:p:`MathCurve2D111`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')



    |Fish_curve_a| `\quad` |Fish_curve_b| `\quad` |Fish_curve_c|

    .. |Fish_curve_a| image:: ../_static/ParametricCurves/Decorative/Fish_Curve.*
       :width: 30 %

    .. |Fish_curve_b| image:: ../_static/ParametricCurves/Decorative/Fish_Curve.*
       :width: 30 %

    .. |Fish_curve_c| image:: ../_static/ParametricCurves/Decorative/Fish_Curve.*
       :width: 30 %





    **Left figure**: Fish curve


    **Middle figure**: Fish curve


    **Right figure**: Fish curve









|newpage|


Heart curve
--------------------------------------------------------------------------------


.. method:: User.HeartCurve(a, Resolution, AsPolar = false)



    The heart curve has the parametric equation

    .. math:: x(t) = 16 \sin^3(t),

    .. math:: y(t) = 13 \cos(t) - 5 \cos(2t) - 2 \cos(3t) - \cos(4t)



    See also  Wikipedia :cite:p:`Wikipedia2D112`,  MathWorld :cite:p:`Wolfram2D112`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')

    An example in C\#

    .. code-block:: csharp

        using User;
        Curve = User.Cardioid(a: 1, Resolution: 200, AsPolar: true);
        User.Chart2D.Show(Curve, Template = "PolarCurve", Title = "Cardioid");


    |Heart_curve_a| `\quad` |Heart_curve_b| `\quad` |Heart_curve_c|

    .. |Heart_curve_a| image:: ../_static/ParametricCurves/Decorative/Heart_Curve.*
       :width: 30 %

    .. |Heart_curve_b| image:: ../_static/ParametricCurves/Decorative/Heart_Curve.*
       :width: 30 %

    .. |Heart_curve_c| image:: ../_static/ParametricCurves/Decorative/Heart_Curve.*
       :width: 30 %





    **Left figure**: Heart curve


    **Middle figure**: Heart curve


    **Right figure**: Heart curve












|newpage|


Chrysanthemum curve
-------------------------------------------------------------------------------

.. method:: User.ChrysanthemumCurve(a, Resolution, AsPolar = false)



    The chrysanthemum curve (see Bourke :cite:p:`Bourke2D222`) is given in polar coordinates by the following

    .. math:: r = 5 (1 + \sin(11 t / 5)) - 4 \sin^4(17 t / 3) \sin^8(2 \cos(3 t) - 28 t)\quad \text{where } 0 \le t \le 21 \pi

    and in Cartesian coordinates

    .. math:: x = r \cos(t)
    .. math:: y = r \sin(t) 



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')

    An example in C\#

    .. code-block:: csharp

        using User;
        Curve = User.Cardioid(a: 1, Resolution: 200, AsPolar: true);
        User.Chart2D.Show(Curve, Template = "PolarCurve", Title = "Cardioid");


    |Chrysanthemum_curve_a| `\quad` |Chrysanthemum_curve_b| `\quad` |Chrysanthemum_curve_c|

    .. |Chrysanthemum_curve_a| image:: ../_static/ParametricCurves/Decorative/Chrysanthemum_Curve.*
       :width: 30 %

    .. |Chrysanthemum_curve_b| image:: ../_static/ParametricCurves/Decorative/Chrysanthemum_Curve.*
       :width: 30 %

    .. |Chrysanthemum_curve_c| image:: ../_static/ParametricCurves/Decorative/Chrysanthemum_Curve.*
       :width: 30 %





    **Left figure**: Chrysanthemum curve


    **Middle figure**: Chrysanthemum curve


    **Right figure**: Chrysanthemum curve








|newpage|


Butterfly curve
-------------------------------------------------------------------------------

.. method:: User.ButterflyCurve(a, Resolution, AsPolar = false)


    See also  Wikipedia :cite:p:`Wikipedia2D216`,  MathWorld :cite:p:`Wolfram2D216`.


    The butterfly curve is given in polar coordinates by the following

    .. math:: r = \exp(\cos(t)) - 2 \cos(4t) - \sin^5(t/12)

    and in Cartesian coordinates

    .. math:: x = r \cos(t)
    .. math:: y = r \sin(t) 



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')

    An example in C\#

    .. code-block:: csharp

        using User;
        Curve = User.Cardioid(a: 1, Resolution: 200, AsPolar: true);
        User.Chart2D.Show(Curve, Template = "PolarCurve", Title = "Cardioid");


    |Butterfly_curve_a| `\quad` |Butterfly_curve_b| `\quad` |Butterfly_curve_c|

    .. |Butterfly_curve_a| image:: ../_static/ParametricCurves/Decorative/Butterfly_Curve.*
       :width: 30 %

    .. |Butterfly_curve_b| image:: ../_static/ParametricCurves/Decorative/Butterfly_Curve.*
       :width: 30 %

    .. |Butterfly_curve_c| image:: ../_static/ParametricCurves/Decorative/Butterfly_Curve.*
       :width: 30 %





    **Left figure**: Butterfly curve


    **Middle figure**: Butterfly curve


    **Right figure**: Butterfly curve







