

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />









|newpage|




Nonorientable (one-sided) Surfaces
========================================




Moebius Strip
------------------------------------------


See also: http://en.wikipedia.org/wiki/M%C3%B6bius_strip

See also: https://mathworld.wolfram.com/MoebiusStrip.html


.. code-block:: csharp

    x = (1 + (v / 2) * Math.Cos(u / 2)) * Math.Cos(u);
    z = (1 + (v / 2) * Math.Cos(u / 2)) * Math.Sin(u);
    y = (v / 2) * Math.Sin(u / 2);


|TestMoebius_a| `\quad` |TestMoebius_b|

.. |TestMoebius_a| image:: ../_static/ParametricSurfaces/Nonorientable/TestMoebius_a.3D.xml.jpg
   :width: 30 %

.. |TestMoebius_b| image:: ../_static/ParametricSurfaces/Nonorientable/TestMoebius_a.3D.xml.jpg
   :width: 30 %


**Left figure**: Moebius Strip (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Moebius Strip (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).







|newpage|






Cross-Cap Surface
------------------------------


See also: https://mathworld.wolfram.com/Cross-Cap.html

See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.



.. code-block:: csharp

    double su = Math.Sin(u);
    double sv = Math.Sin(v);
    double s2v = Math.Sin(2*v);
    double cu = Math.Cos(u);
    double cv = Math.Cos(v);
    x = 0.5 * cu * s2v;
    z = 0.5 * su * s2v;
    y = 0.5 * (cv*cv - cu*cu * sv*sv);



|TestCrossCap_a| `\quad` |TestCrossCap_b|

.. |TestCrossCap_a| image:: ../_static/ParametricSurfaces/Nonorientable/TestCrossCap_a.3D.xml.jpg
   :width: 30 %

.. |TestCrossCap_b| image:: ../_static/ParametricSurfaces/Nonorientable/TestCrossCap_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Cross-Cap Surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Cross-Cap Surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).






|newpage|



Pseudo Cross-Cap Surface
--------------------------------------------


See also: https://mathworld.wolfram.com/Pseudocrosscap.html

See also: http://www.3d-meier.de/tut3/Seite51.html

See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.


.. code-block:: csharp

    double sv = Math.Sin(v);
    double s2v = Math.Sin(2*v);
    x = (1 - u*u) * sv;
    y = (1 - u*u) * s2v;
    z = u;



|TestPseudoCrossCap_a| `\quad` |TestPseudoCrossCap_b|

.. |TestPseudoCrossCap_a| image:: ../_static/ParametricSurfaces/Removal/TestPseudoCrossCap_a.3D.xml.jpg
   :width: 30 %

.. |TestPseudoCrossCap_b| image:: ../_static/ParametricSurfaces/Removal/TestPseudoCrossCap_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Pseudo Cross-Cap Surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Pseudo Cross-Cap Surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).





|newpage|


Roman Surface (or Steiner Surface)
-----------------------------------------------


See also: https://mathworld.wolfram.com/RomanSurface.html

See also: https://en.wikipedia.org/wiki/Roman_surface

See also: http://paulbourke.net/geometry/steiner/


.. code-block:: csharp

    double r2 = 1;
    double su = Math.Sin(u);
    double sv = Math.Sin(v);
    double cu = Math.Cos(u);
    double cv = Math.Cos(v);
    x = r2 * cu * su * sv;
    y = r2 * cu * su * cv;
    z = r2 * cu*cu * sv * cv;


See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.


|TestRoman_a| `\quad` |TestRoman_b|

.. |TestRoman_a| image:: ../_static/ParametricSurfaces/Nonorientable/TestRoman_a.3D.xml.jpg
   :width: 30 %

.. |TestRoman_b| image:: ../_static/ParametricSurfaces/Nonorientable/TestRoman_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Roman Surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Roman Surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).









|newpage|


Klein bagel
-----------------------------


See also: https://en.wikipedia.org/wiki/Klein_bottle#The_figure_8_immersion

See also: https://mathworld.wolfram.com/KleinBottle.html


.. code-block:: csharp

    double r = 2.1;
    x = (r + Math.Cos(u / 2) * Math.Sin(v) - Math.Sin(u / 2) * Math.Sin(2 * v)) * Math.Cos(u);
    z = (r + Math.Cos(u / 2) * Math.Sin(v) - Math.Sin(u / 2) * Math.Sin(2 * v)) * Math.Sin(u);
    y = Math.Sin(u / 2) * Math.Sin(v) + Math.Cos(u / 2) * Math.Sin(2 * v);



This is the 'bagel' form of a Klein bottle, a 4 dimensional object with a single surface (lacking 'inside' or 'outside'), projected into 3-space as a self-intersecting solid.


|TestKleinBagel_a| `\quad` |TestKleinBagel_b|

.. |TestKleinBagel_a| image:: ../_static/ParametricSurfaces/Nonorientable/TestKleinBagel_a.3D.xml.jpg
   :width: 30 %

.. |TestKleinBagel_b| image:: ../_static/ParametricSurfaces/Nonorientable/TestKleinBagel_a.3D.xml.jpg
   :width: 30 %


**Left figure**: Klein bagel (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Klein bagel (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).






|newpage|


Klein bottle, version 3
---------------------------------------


See also: http://www.mapleprimes.com/maplesoftblog/95570-Klein-Bottle-Plot

See also: http://www.chebfun.org/examples/geom/ParametricSurfaces.html

See also: https://mathworld.wolfram.com/KleinBottle.html


.. code-block:: csharp

    double a = Math.Cos(u);
    double b = Math.Sin(u);
    double c = Math.Cos(v);
    double a2 = a * a;
    double a4 = a2 * a2;
    x = -(2.0 / 15.0) * a * (3 * c + b * (-30 + a4 * (90 - 60 * a2) + 5 * a * c));
    z = -(1.0 / 15.0) * b * b * (c * b * (3 - 48 * a4 + 5 * a * b * (1 - 16 * a4)) - 60);
    y = -(2.0 / 15.0) * (3 + 5 * a * b) * Math.Sin(v);




|TestKleinBottle3_a| `\quad` |TestKleinBottle3_b|

.. |TestKleinBottle3_a| image:: ../_static/ParametricSurfaces/Nonorientable/TestKleinBottle3_a.3D.xml.jpg
   :width: 30 %

.. |TestKleinBottle3_b| image:: ../_static/ParametricSurfaces/Nonorientable/TestKleinBottle3_a.3D.xml.jpg
   :width: 30 %


**Left figure**: Klein bottle, version 3 (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Klein bottle, version 3 (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).






|newpage|


Klein bottle, version 2
-----------------------------------


See also: https://mathworld.wolfram.com/KleinBottle.html

The following parametrization is from the English Wikipedia article:

https://en.wikipedia.org/wiki/Klein_bottle#Bottle_shape



There is also a different parametrization in the German Wikipedia article:

https://de.wikipedia.org/wiki/Kleinsche_Flasche#Beschreibung_im_dreidimensionalen_Raum



.. code-block:: csharp

    double sinV = Math.Sin(v);
    double cosV = Math.Cos(v);
    double sinU = Math.Sin(u);
    double cosU = Math.Cos(u);
    double cosU2 = cosU * cosU;
    double cosU3 = cosU2 * cosU;
    double cosU4 = cosU3 * cosU;
    double cosU5 = cosU4 * cosU;
    double cosU6 = cosU5 * cosU;
    double cosU7 = cosU6 * cosU;

    x = -2.0 / 15 * cosU * (3 * cosV - 30 * sinU + 90 * cosU4 * sinU -
        60 * cosU6 * sinU + 5 * cosU * cosV * sinU);
    y = -1.0 / 15 * sinU * (3 * cosV - 3 * cosU2 * cosV -
        48 * cosU4 * cosV + 48 * cosU6 * cosV -
        60 * sinU + 5 * cosU * cosV * sinU - 5 * cosU3 * cosV * sinU -
        80 * cosU5 * cosV * sinU + 80 * cosU7 * cosV * sinU);
    z = 2.0 / 15 * (3 + 5 * cosU * sinU) * sinV;

    // Note: Move y up a bit and invert.
    // Invert x to orient the "outer" parts of the bottle outwardly.
    // If you don't use a BackMaterial, then parts inside the opening are culled.
    double a = 1.5;
    x = a * (-x);
    y = a * (2 - y);
    z = a * (z);



|TestKleinBottle2_a| `\quad` |TestKleinBottle2_b|

.. |TestKleinBottle2_a| image:: ../_static/ParametricSurfaces/Nonorientable/TestKleinBottle2_a.3D.xml.jpg
   :width: 30 %

.. |TestKleinBottle2_b| image:: ../_static/ParametricSurfaces/Nonorientable/TestKleinBottle2_a.3D.xml.jpg
   :width: 30 %


**Left figure**: Klein bottle, version 2 (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Klein bottle, version 2 (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).







|newpage|


Klein bottle, version 1
------------------------------------


See also: http://www.mapleprimes.com/maplesoftblog/95570-Klein-Bottle-Plot

See also: http://www.chebfun.org/examples/geom/ParametricSurfaces.html

See also: https://mathworld.wolfram.com/KleinBottle.html



.. code-block:: csharp

    x = (3 * (1 + Math.Sin(v)) + 2 * (1 - Math.Cos(v) / 2) * Math.Cos(u)) * Math.Cos(v);
    y = (-2 * (1 - Math.Cos(v) / 2) * Math.Sin(u));
    z = (4 + 2 * (1 - Math.Cos(v) / 2) * Math.Cos(u)) * Math.Sin(v);



|TestKleinBottle_a| `\quad` |TestKleinBottle_b|

.. |TestKleinBottle_a| image:: ../_static/ParametricSurfaces/Nonorientable/TestKleinBottle_a.3D.xml.jpg
   :width: 30 %

.. |TestKleinBottle_b| image:: ../_static/ParametricSurfaces/Nonorientable/TestKleinBottle_a.3D.xml.jpg
   :width: 30 %


**Left figure**: Klein bottle, version 1 (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Klein bottle, version 1 (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).






|newpage|



3D Boy Surface, version 1
-----------------------------------


See also: https://en.wikipedia.org/wiki/Boy%27s_surface

See also: http://mathworld.wolfram.com/BoySurface.html



.. code-block:: csharp

    double sqrt5 = Math.Sqrt(5);
    // w = u*e^(iv)
    double wr = Math.Cos(v);
    double wi = Math.Sin(v);
    Complex w = u * new Complex(wr, wi);
    Complex w3 = w * w * w;
    Complex w4 = w3 * w;
    Complex w6 = w3 * w3;
    Complex d = w6 + sqrt5 * w3 - 1;
    Complex wa = w * (1 - w4) / d;
    Complex wb = w * (1 + w4) / d;
    Complex wc = (1 + w6) / d;
    double g1 = -1.5 * wa.Imaginary;
    double g2 = -1.5 * wb.Real;
    double g3 = wc.Imaginary - 0.5;
    double l2 = g1 * g1 + g2 * g2 + g3 * g3;
    x = g1 / l2;
    y = -g2 / l2;
    z = g3 / l2;



|picTestBoy1a| `\quad` |picTestBoy1b|

.. |picTestBoy1a| image:: ../_static/ParametricSurfaces/Nonorientable/TestBoy.3D.xm.jpg
   :width: 30 %

.. |picTestBoy1b| image:: ../_static/ParametricSurfaces/Nonorientable/TestBoy.3D.xml.jpg
   :width: 30 %


**Left figure**: parametric plot of the Boy Surface (parametrization 1). 


**Reft figure**: parametric plot of the Boy Surface (parametrization 1). 




|newpage|



3D Boy Surface, version 2
-------------------------------------------


See also: https://en.wikipedia.org/wiki/Boy%27s_surface

See also: http://mathworld.wolfram.com/BoySurface.html



.. code-block:: csharp

    double sqrt2 = Math.Sqrt(2);
    double s2v = Math.Sin(2 * v);
    double cu = Math.Cos(u);
    double cv = Math.Cos(v);
    double cv2 = cv * cv;
    double n1 = sqrt2 * cv2 * Math.Cos(2*u);
    double xn = sqrt2 * cv2 * Math.Cos(2 * u) + cu * s2v;
    double yn = sqrt2 * cv2 * Math.Sin(2 * u) - Math.Sin(u) * s2v;
    double zn = 3 * cv2;
    double d = 2 - sqrt2 * Math.Sin(3 * u) * s2v;
    x = xn / d;
    y = yn / d;
    z = zn / d;




|picTestBoy2a| `\quad` |picTestBoy2b|

.. |picTestBoy2a| image:: ../_static/ParametricSurfaces/Nonorientable/TestBoySurface2_a.3D.xml.jpg
   :width: 30 %

.. |picTestBoy2b| image:: ../_static/ParametricSurfaces/Nonorientable/TestBoySurface2_b.3D.xml.jpg
   :width: 30 %


**Left figure**: parametric plot of the Boy Surface (parametrization 1). 

**Reft figure**: parametric plot of the Boy Surface (parametrization 1). 






|newpage|



Morin Surface
-------------------------------------------


// See also: http://www.3d-meier.de/tut3/Seite221.html  // Morin Surface
// See also: https://mathcurve.com/surfaces.gb/morin/morin.shtml
// See also: https://en.wikipedia.org/wiki/Morin_surface
// See also: Bednorz 2019


.. code-block:: csharp

    var k = 1.0;
    var n = 3.0;

    var Sqrt2 = Math.Sqrt(2);
    var cu = Math.Cos(u);
    var su = Math.Sin(u);
    var K = cu / (Sqrt2 - k * Math.Sin(2 * u) * Math.Sin(n * v));

    var x = K * (2 / (n - 1) * cu * Math.Cos((n - 1) * v) + Sqrt2 * su * Math.Cos(v));
    var y = K * (2 / (n - 1) * cu * Math.Sin((n - 1) * v) - Sqrt2 * su * Math.Sin(v));
    var z = K * cu;



|11a_TestMorin3| `\quad` |12a_TestMorin5| `\quad` |13a_TestMorin9|

.. |11a_TestMorin3| image:: ../_static/ParametricSurfaces/Nonorientable/11a_TestMorin3.3D.xml.jpg
   :width: 30 %

.. |12a_TestMorin5| image:: ../_static/ParametricSurfaces/Nonorientable/12a_TestMorin5.3D.xml.jpg
   :width: 30 %

.. |13a_TestMorin9| image:: ../_static/ParametricSurfaces/Nonorientable/13a_TestMorin9.3D.xml.jpg
   :width: 30 %



**Left figure**: Morin Surface  (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Morin Surface  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Morin Surface  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).



|11b_TestMorin3| `\quad` |12b_TestMorin5| `\quad` |13b_TestMorin9|

.. |11b_TestMorin3| image:: ../_static/ParametricSurfaces/Nonorientable/11b_TestMorin3.3D.xml.jpg
   :width: 30 %

.. |12b_TestMorin5| image:: ../_static/ParametricSurfaces/Nonorientable/12b_TestMorin5.3D.xml.jpg
   :width: 30 %

.. |13b_TestMorin9| image:: ../_static/ParametricSurfaces/Nonorientable/13b_TestMorin9.3D.xml.jpg
   :width: 30 %



**Left figure**: Morin Surface  (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Morin Surface  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Morin Surface  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).







