

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />







|newpage|




Decorative parametric surfaces
==============================================



https://de.mathworks.com/help/matlab/ref/plot3.html

https://doc.sagemath.org/html/en/reference/plot3d/index.html

http://www.3d-meier.de/tut3/Seite0.html

http://www.3d-meier.de/tut8/Seite3.html

https://docs.ambientcg.com/books/website-licensing/page/license-information

https://ambientcg.com/list?category=&date=&createdUsing=&basedOn=&q=&method=&type=&sort=Downloads






Bourke Seashell
-----------------------------------------


See also: http://paulbourke.net/geometry/spiral/


.. code-block:: csharp

    double n = 3;  // number of spirals
    double a = 1;  // final shell radius
    double b = 2;  // height
    double c = 0.4;  // inner radius
                
    double s = v;
    double t = u;
    double pt = t/(2*Math.PI);  // inner radius
                
    x = a * (1 - pt) * Math.Cos(n*t) * (1 + Math.Cos(s)) + c * Math.Cos(n*t);
    z = a * (1 - pt) * Math.Sin(n*t) * (1 + Math.Cos(s)) + c * Math.Sin(n*t);
    y = b * pt + a * (1 - pt) * Math.Sin(s);



|picTestBourneSeaShell1| `\quad` |picTestBourneSeaShell2|

.. |picTestBourneSeaShell1| image:: ../_static/ParametricSurfaces/Textures/TestBourneSeaShell.3D.xm.jpg
   :width: 30 %

.. |picTestBourneSeaShell2| image:: ../_static/ParametricSurfaces/Textures/TestBourneSeaShell.3D.xml.jpg
   :width: 30 %






|newpage|


Seashell (mathworld.wolfram)
---------------------------------------------

.. method:: User.Seashell(a, Resolution)


See also: https://mathworld.wolfram.com/Seashell.html



.. code-block:: csharp

    double a = Math.Exp(u / (6.0 * Math.PI));
    double b = Math.Cos(v / 2.0);

    x = 2.0 * (1.0 - a) * Math.Cos(u) * b * b;
    y = 2.0 * (-1.0 + a) * Math.Sin(u) * b * b;
    z = (1.0 - a * a - Math.Sin(v) * (1.0 - a));



|TestSeashell_a| `\quad` |TestSeashell_b|

.. |TestSeashell_a| image:: ../_static/ParametricSurfaces/Textures/TestSeashell_a.3D.xml.jpg
   :width: 30 %

.. |TestSeashell_b| image:: ../_static/ParametricSurfaces/Textures/TestSeashell_a.3D.xml.jpg
   :width: 30 %





|newpage|



3D Apple
-------------------------

.. method:: User.Apple(a, Resolution)


.. code-block:: csharp

    double R1 = 5.0;
    double R2 = 4.8;
    double su = Math.Sin(u);
    double sv = Math.Sin(v);
    double cu = Math.Cos(u);
    double c5u = Math.Cos(5*u);
    double cv = Math.Cos(v);
    x = cu * (R1 + R2 * cv) + Math.Pow(v/Math.PI, 20);
    z = su * (R1 + R2 * cv) + 0.25 * c5u;
    y = -2.3 * Math.Log(1 - v * 0.3157) + 6 * sv + 2 * cv;



|picTestApple1| `\quad` |picTestApple2|

.. |picTestApple1| image:: ../_static/ParametricSurfaces/Textures/TestApple.3D.xm.jpg
   :width: 30 %

.. |picTestApple2| image:: ../_static/ParametricSurfaces/Textures/TestApple.3D.xml.jpg
   :width: 30 %

**Left figure**: parametric plot of the Apple surface. 






|newpage|


Bow curve
----------------------------------

.. method:: User.Bow(a, Resolution)


See also: http://paulbourke.net/geometry/toroidal/


.. code-block:: csharp

    double p2 = 2*Math.PI;
    double p4 = 4*Math.PI;
    double T = 0.5; //Thickness
                
    x = (2 + T * Math.Sin(p2 * u)) * Math.Sin(p4 * v);
    y = (2 + T * Math.Sin(p2 * u)) * Math.Cos(p4 * v);
    z = T * Math.Cos(p2 * u) + 3 * Math.Cos(p2 * v);




|picTestBowCurve1| `\quad` |picTestBowCurve2|

.. |picTestBowCurve1| image:: ../_static/ParametricSurfaces/Textures/TestBowCurve.3D.xm.jpg
   :width: 30 %

.. |picTestBowCurve2| image:: ../_static/ParametricSurfaces/Textures/TestBowCurve.3D.xml.jpg
   :width: 30 %



**Left figure**: Bow curve (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Bow curve (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).




|newpage|


Fish Surface
--------------------------------------

.. method:: User.Fish3D(a, Resolution)


See also: http://www.3d-meier.de/tut3/Seite47.html



See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.


.. code-block:: csharp

    double su = Math.Sin(u);
    double s2u = Math.Sin(2*u);
    double sv = Math.Sin(v);
    double cu = Math.Cos(u);
    double c2u = Math.Cos(2*u);
    double cv = Math.Cos(v);
    x = (cu - c2u) * cv / 4.0;
    y = (su - s2u) * sv / 4.0;
    z = cu;



|TestFish_a| `\quad` |TestFish_b|

.. |TestFish_a| image:: ../_static/ParametricSurfaces/Textures/TestFish_a.3D.xml.jpg
   :width: 30 %

.. |TestFish_b| image:: ../_static/ParametricSurfaces/Textures/TestFish_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Fish Surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Fish Surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).






|newpage|


Bourke Horn
--------------------------------------

.. method:: User.BourkeHorn3D(a, Resolution)


See also: http://paulbourke.net/geometry/spiral/


.. code-block:: csharp

    double p2 = 2*Math.PI;
    x = (2 + u * Math.Cos(v)) * Math.Sin(p2 * u);
    y = (2 + u * Math.Cos(v)) * Math.Cos(p2 * u) + 2 * u;
    z = u * Math.Sin(v);



|picTestBourneHorn1| `\quad` |picTestBourneHorn2|

.. |picTestBourneHorn1| image:: ../_static/ParametricSurfaces/Textures/TestBourneHorn.3D.xm.jpg
   :width: 30 %

.. |picTestBourneHorn2| image:: ../_static/ParametricSurfaces/Textures/TestBourneHorn.3D.xml.jpg
   :width: 30 %
   

**Left figure**: Bourne Horn (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Bourne Horn (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).









|newpage|





Hexa torus
--------------------------------------

.. method:: User.HexaTorus3D(a, Resolution)


See also: http://paulbourke.net/geometry/toroidal/

The C\# code for the Klein bottle: 

.. code-block:: csharp

    double a = Math.Cos(u);
    double b = Math.Sin(u);
    double c = Math.Cos(v);
    double a2 = a * a;
    double a4 = a2 * a2;

    x = -(2.0 / 15.0) * a * (3 * c + b * (-30 + a4 * (90 - 60 * a2) + 5 * a * c));
    z = -(1.0 / 15.0) * b * b * (c * b * (3 - 48 * a4 + 5 * a * b * (1 - 16 * a4)) - 60);
    y = (2.0 / 15.0) * (3 + 5 * a * b) * Math.Sin(v);




|picHexaTorus1| `\quad` |picHexaTorus2|

.. |picHexaTorus1| image:: ../_static/ParametricSurfaces/Textures/TestHexaTorus.3D.xm.jpg
   :width: 30 %

.. |picHexaTorus2| image:: ../_static/ParametricSurfaces/Textures/TestHexaTorus.3D.xml.jpg
   :width: 30 %



**Left figure**: Hexa torus (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Hexa torus (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).







|newpage|





3D Breather Surface
-------------------------

.. method:: User.Breather3D(a, Resolution)

.. code-block:: csharp

    const double b = 0.4;
    double r = 1 - b * b;
    double w = Math.Sqrt(r);
    double denom = b * (
        (w * Math.Cosh(b * u)) * (w * Math.Cosh(b * u)) +
        (b * Math.Sin(w * v)) * (b * Math.Sin(w * v)));
    
    x = -u + (2 * r * Math.Cosh(b * u) * Math.Sinh(b * u)) / denom;
    y = (2 * w * Math.Cosh(b * u) * (-(w * Math.Cos(v) * Math.Cos(w * v)) - Math.Sin(v) * Math.Sin(w * v))) / denom;
    z = (2 * w * Math.Cosh(b * u) * (-(w * Math.Sin(v) * Math.Cos(w * v)) + Math.Cos(v) * Math.Sin(w * v))) / denom;




|picTestBreather1| `\quad` |picTestBreather2|

.. |picTestBreather1| image:: ../_static/ParametricSurfaces/Textures/TestBreather.3D.xm.jpg
   :width: 30 %

.. |picTestBreather2| image:: ../_static/ParametricSurfaces/Textures/TestBreather.3D.xml.jpg
   :width: 30 %

**Left figure**: parametric plot of the Breather Surface. 





|newpage|


Kuen surface
----------------------------------

.. method:: User.Kuen3D(a, Resolution)


See also: https://mathworld.wolfram.com/KuenSurface.html

See also: https://virtualmathmuseum.org/Surface/kuen/kuen.html

See also: https://mathcurve.com/surfaces.gb/kuen/kuen.shtml



.. code-block:: csharp

    double a = 1.0 * Math.Sin(v);
    double b = 1.0 + u * u * a * a;

    x = 2.0 * a * (Math.Cos(u) + u * Math.Sin(u)) / b;
    z = 2.0 * a * (Math.Sin(u) - u * Math.Cos(u)) / b;
    y = Math.Log(Math.Tan(v / 2.0)) + 2.0 * Math.Cos(v) / b;




|TestKuen_a| `\quad` |TestKuen_b|

.. |TestKuen_a| image:: ../_static/ParametricSurfaces/Textures/TestKuen_a.3D.xml.jpg
   :width: 30 %

.. |TestKuen_b| image:: ../_static/ParametricSurfaces/Textures/TestKuen_a.3D.xml.jpg
   :width: 30 %


**Left figure**: Kuen surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Kuen surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).











|newpage|


Tranguloid trefoil
--------------------------------------

.. method:: User.TranguloidTrefoil3D(a, Resolution)


See also: http://paulbourke.net/geometry/tranguloid/




There are other parametrizations:

See also: http://www.3d-meier.de/tut3/Seite56.html
See also: https://mathart.org/sw/GreenSnake/Toroid2.html

See also: http://www.3d-meier.de/tut3/Seite159.html


.. code-block:: csharp

    double p2 = 2*Math.PI/3;
    x = 2 * Math.Sin(3 * u) / (2 + Math.Cos(v));
    y = 2 * (Math.Sin(u) + 2 * Math.Sin(2 * u)) / (2 + Math.Cos(v + p2));
    z = (Math.Cos(u) - 2 * Math.Cos(2 * u)) * (2 + Math.Cos(v)) * (2 + Math.Cos(v + p2)) / 4;




|picTestTrefoil1| `\quad` |picTestTrefoil2|

.. |picTestTrefoil1| image:: ../_static/ParametricSurfaces/Textures/TestTrefoil.3D.xm.jpg
   :width: 30 %

.. |picTestTrefoil2| image:: ../_static/ParametricSurfaces/Textures/TestTrefoil.3D.xml.jpg
   :width: 30 %



**Left figure**: Tranguloid trefoil (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Tranguloid trefoil (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).





|newpage|


Triaxial teardrop
--------------------------------------

.. method:: User.TriaxialTeardrop3D(a, Resolution)


See also: http://paulbourke.net/geometry/triaxtear/

See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.



.. code-block:: csharp

    double p2 = 2*Math.PI/3;
    x = ( 1 - Math.Cos(u) ) * Math.Cos(u + p2) * Math.Cos(v + p2) / 2;
    y = -( 1 - Math.Cos(u) ) * Math.Cos(u + p2) * Math.Cos(v - p2) / 2;
    z = Math.Cos(u - p2);




|TestTearDrop_a| `\quad` |TestTearDrop_b|

.. |TestTearDrop_a| image:: ../_static/ParametricSurfaces/Textures/TestTearDrop_a.3D.xml.jpg
   :width: 30 %

.. |TestTearDrop_b| image:: ../_static/ParametricSurfaces/Textures/TestTearDrop_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Bours Minimal Surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Bours Minimal Surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).






|newpage|


Gray Bottle
--------------------------------------

.. method:: User.GrayBottle3D(a, Resolution)


See also: http://paulbourke.net/geometry/toroidal/


.. code-block:: csharp

    x = Math.Cos(v) * Math.Sqrt(Math.Abs(Math.Sin(2 * u))) * Math.Cos(u);
    y = Math.Cos(v) * Math.Sqrt(Math.Abs(Math.Sin(2 * u))) * Math.Sin(u);
    z = x*x - y*y + 2 * x * y * Math.Tan(v) * Math.Tan(v);



|picGrayBottel1| `\quad` |picGrayBottel2|

.. |picGrayBottel1| image:: ../_static/ParametricSurfaces/Textures/TestGrayBottel.3D.xm.jpg
   :width: 30 %

.. |picGrayBottel2| image:: ../_static/ParametricSurfaces/Textures/TestGrayBottel.3D.xml.jpg
   :width: 30 %


**Left figure**: Gray Bottle (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Gray Bottle (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).








|newpage|

Surfaces mimicking snail shells
-----------------------------------------------

.. method:: User.Snail1(a, Resolution)


See also: http://www.3d-meier.de/tut3/Seite89.html


|TestSnail1_a| `\quad` |TestSnail1_b|

.. |TestSnail1_a| image:: ../_static/ParametricSurfaces/Textures/TestSnail1_a.3D.xml.jpg
   :width: 30 %

.. |TestSnail1_b| image:: ../_static/ParametricSurfaces/Textures/TestSnail1_a.3D.xml.jpg
   :width: 30 %


**Left figure**: Pseudoheliceras subcatenatum surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Pseudoheliceras subcatenatum surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).




.. code-block:: csharp

    double R = 1;
    double a = 1.6;
    double b = 1.6;
    double c = 1.0;
    double h = 1.5;
    double k = -7.0;
    double w = 0.075;
    //  umin = -50, umax = -1,    name:  Pseudoheliceras subcatenatum
                
    double su = Math.Sin(u);
    double scu = Math.Sin(c*u);
    double sv = Math.Sin(v);
    double cv = Math.Cos(v);
    double ccu = Math.Cos(c*u);
                
    double ewu = Math.Exp(w*u);
                
    x = ewu * (h+a*cv) * ccu;
    z = R * ewu * (h+a*cv) * scu;
    y = ewu * (k + b * sv);




|newpage|



|TestSnail2_a| `\quad` |TestSnail3_a| `\quad` |TestSnail4_a|

.. |TestSnail2_a| image:: ../_static/ParametricSurfaces/Removal/TestSnail2_a.3D.xml.jpg
   :width: 30 %

.. |TestSnail3_a| image:: ../_static/ParametricSurfaces/Removal/TestSnail3_a.3D.xml.jpg
   :width: 30 %

.. |TestSnail4_a| image:: ../_static/ParametricSurfaces/Removal/TestSnail4_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Astroceras surface.

**Middle figure**: Bellerophina surface.

**Right figure**: Euhoplites Surface.




|TestSnail5_a| `\quad` |TestSnail6_a| `\quad` |TestSnail7_a|

.. |TestSnail5_a| image:: ../_static/ParametricSurfaces/Removal/TestSnail5_a.3D.xml.jpg
   :width: 30 %

.. |TestSnail6_a| image:: ../_static/ParametricSurfaces/Removal/TestSnail6_a.3D.xml.jpg
   :width: 30 %

.. |TestSnail7_a| image:: ../_static/ParametricSurfaces/Removal/TestSnail7_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Nautilus surface.

**Middle figure**: Natica stellata surface.

**Right figure**: Mya arenaria Surface.



