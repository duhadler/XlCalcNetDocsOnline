

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />






|newpage|

Lissajous knots
==============================================================

See also: https://en.wikipedia.org/wiki/Lissajous_knot

See also: https://mathcurve.com/courbes3d.gb/lissajous3d/noeudlissajous.shtml

See also: https://knotplot.com/manual/LissajousParams.html


The Lissajous knots are the knots associated to the 3D Lissajous curves when they are closed and without double point.

As is proved in the above article by Jones and Przytycki, they also are the knots associated to the trajectories of a ball (not subject to gravity) in a parallelepipedic billiard, or even a cubic one (imagine a glass box).

It can be proved that for all values of p, q, r, there exist values of j and y such that the knot is trivial, and that certain knots such as the trefoil knot are not Lissajous knots. 


See also: https://mathcurve.com/courbes3d.gb/lissajous3d/lissajous3d.shtml


The 3D Lissajous curves are the trajectories of a point in space the rectangular components of which have a sinusoidal motion.
The projections on the 3 coordinate planes are the classic 2D Lissajous curves.

For n = 1 or n = m, we get a cylindrical sine wave.
We get a closed curve if and only if n and m are rational.

When the curve does not have double points, nor a cusp, it forms a knot in space, called Lissajous knot, equivalent to a cubic billiard knot.







|newpage|

Lissajous knot 1-1-1
----------------------------------


An example in C\#

.. code-block:: csharp

    double pi = Math.PI;
    double a1, k1, l1;
    double a2, k2, l2;
    double a3, k3, l3;
    a1 = 100; k1 = 1; l1 = 0;
    a2 = 100; k2 = 1; l2 = pi / 2;
    a3 = 100; k3 = 1; l3 = pi / 2;
    var x = (a1 * Math.Cos(k1 * t + l1)) / 50;
    var y = (a3 * Math.Cos(k3 * t + l3)) / 50;
    var z = (a2 * Math.Cos(k2 * t + l2)) / 50;




|PathP_111_LKnot_P090T090a| `\quad` |PathP_111_LKnot_P090T180a| `\quad` |PathP_111_LKnot_P135T180a|

.. |PathP_111_LKnot_P090T090a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_111_LKnot_P090T090a.3D.xml.jpg
   :width: 30 %

.. |PathP_111_LKnot_P090T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_111_LKnot_P090T180a.3D.xml.jpg
   :width: 30 %

.. |PathP_111_LKnot_P135T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_111_LKnot_P135T180a.3D.xml.jpg
   :width: 26 %




**Left figure**: Lissajous knot 1-1-1. Perspective camera. 

**Middle figure**: Lissajous knot 1-1-1. Perspective camera. 

**Right figure**: Lissajous knot 1-1-1. Perspective camera. 




Some text


|PathO_111_LKnot_P090T090a| `\quad` |PathO_111_LKnot_P090T180a| `\quad` |PathO_111_LKnot_P135T180a|

.. |PathO_111_LKnot_P090T090a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_111_LKnot_P090T090a.3D.xml.jpg
   :width: 30 %

.. |PathO_111_LKnot_P090T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_111_LKnot_P090T180a.3D.xml.jpg
   :width: 30 %

.. |PathO_111_LKnot_P135T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_111_LKnot_P135T180a.3D.xml.jpg
   :width: 22 %




**Left figure**: Lissajous knot 1-1-1. Orthographic camera. 

**Middle figure**: Lissajous knot 1-1-1. Orthographic camera. 

**Right figure**: Lissajous knot 1-1-1. Orthographic camera. 








|newpage|



Lissajous knot 1-2-1
-------------------------------------


An example in C\#

.. code-block:: csharp

    double pi = Math.PI;
    double a1, k1, l1;
    double a2, k2, l2;
    double a3, k3, l3;
    a1 = 100; k1 = 1; l1 = 0;
    a2 = 100; k2 = 2; l2 = pi / 2;
    a3 = 100; k3 = 1; l3 = pi / 2;
    var x = (a1 * Math.Cos(k1 * t + l1)) / 50;
    var y = (a3 * Math.Cos(k3 * t + l3)) / 50;
    var z = (a2 * Math.Cos(k2 * t + l2)) / 50;


|PathP_121_LKnot_P090T090a| `\quad` |PathP_121_LKnot_P090T180a| `\quad` |PathP_121_LKnot_P135T180a|

.. |PathP_121_LKnot_P090T090a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_121_LKnot_P090T090a.3D.xml.jpg
   :width: 30 %

.. |PathP_121_LKnot_P090T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_121_LKnot_P090T180a.3D.xml.jpg
   :width: 30 %

.. |PathP_121_LKnot_P135T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_121_LKnot_P135T180a.3D.xml.jpg
   :width: 26 %




**Left figure**: Lissajous knot 1-2-1. Perspective camera. 

**Middle figure**: Lissajous knot 1-2-1. Perspective camera. 

**Right figure**: Lissajous knot 1-2-1. Perspective camera. 




Some text


|PathO_121_LKnot_P090T090a| `\quad` |PathO_121_LKnot_P090T180a| `\quad` |PathO_121_LKnot_P135T180a|

.. |PathO_121_LKnot_P090T090a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_121_LKnot_P090T090a.3D.xml.jpg
   :width: 30 %

.. |PathO_121_LKnot_P090T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_121_LKnot_P090T180a.3D.xml.jpg
   :width: 30 %

.. |PathO_121_LKnot_P135T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_121_LKnot_P135T180a.3D.xml.jpg
   :width: 22 %




**Left figure**: Lissajous knot 1-2-1. Orthographic camera. 

**Middle figure**: Lissajous knot 1-2-1. Orthographic camera. 

**Right figure**: Lissajous knot 1-2-1. Orthographic camera. 















|newpage|


Lissajous knot 1-5-3
----------------------------------


An example in C\#

.. code-block:: csharp

    double pi = Math.PI;
    double a1, k1, l1;
    double a2, k2, l2;
    double a3, k3, l3;
    a1 = 100; k1 = 1; l1 = 0;
    a2 = 100; k2 = 5; l2 = pi / 2;
    a3 = 100; k3 = 3; l3 = pi / 2;
    var x = (a1 * Math.Cos(k1 * t + l1)) / 50;
    var y = (a3 * Math.Cos(k3 * t + l3)) / 50;
    var z = (a2 * Math.Cos(k2 * t + l2)) / 50;


|PathP_153_LKnot_P090T090a| `\quad` |PathP_153_LKnot_P090T180a| `\quad` |PathP_153_LKnot_P135T180a|

.. |PathP_153_LKnot_P090T090a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_153_LKnot_P090T090a.3D.xml.jpg
   :width: 30 %

.. |PathP_153_LKnot_P090T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_153_LKnot_P090T180a.3D.xml.jpg
   :width: 30 %

.. |PathP_153_LKnot_P135T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_153_LKnot_P135T180a.3D.xml.jpg
   :width: 26 %




**Left figure**: Lissajous knot 1-5-3. Perspective camera. 

**Middle figure**: Lissajous knot 1-5-3. Perspective camera. 

**Right figure**: Lissajous knot 1-5-3. Perspective camera. 




Some text


|PathO_153_LKnot_P090T090a| `\quad` |PathO_153_LKnot_P090T180a| `\quad` |PathO_153_LKnot_P135T180a|

.. |PathO_153_LKnot_P090T090a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_153_LKnot_P090T090a.3D.xml.jpg
   :width: 30 %

.. |PathO_153_LKnot_P090T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_153_LKnot_P090T180a.3D.xml.jpg
   :width: 30 %

.. |PathO_153_LKnot_P135T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_153_LKnot_P135T180a.3D.xml.jpg
   :width: 22 %




**Left figure**: Lissajous knot 1-5-3. Orthographic camera. 

**Middle figure**: Lissajous knot 1-5-3. Orthographic camera. 

**Right figure**: Lissajous knot 1-5-3. Orthographic camera. 














|newpage|


Lissajous knot 3-5-2
--------------------------------


An example in C\#

.. code-block:: csharp

    double pi = Math.PI;
    double a1, k1, l1;
    double a2, k2, l2;
    double a3, k3, l3;
    a1 = 100; k1 = 3; l1 = 0;
    a2 = 100; k2 = 5; l2 = pi / 2;
    a3 = 100; k3 = 2; l3 = pi / 2;
    var x = (a1 * Math.Cos(k1 * t + l1)) / 50;
    var y = (a3 * Math.Cos(k3 * t + l3)) / 50;
    var z = (a2 * Math.Cos(k2 * t + l2)) / 50;



|PathP_352_LKnot_P090T090a| `\quad` |PathP_352_LKnot_P090T180a| `\quad` |PathP_352_LKnot_P135T180a|

.. |PathP_352_LKnot_P090T090a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_352_LKnot_P090T090a.3D.xml.jpg
   :width: 30 %

.. |PathP_352_LKnot_P090T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_352_LKnot_P090T180a.3D.xml.jpg
   :width: 30 %

.. |PathP_352_LKnot_P135T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_352_LKnot_P135T180a.3D.xml.jpg
   :width: 26 %




**Left figure**: Lissajous knot 3-5-2. Perspective camera. 

**Middle figure**: Lissajous knot 3-5-2. Perspective camera. 

**Right figure**: Lissajous knot 3-5-2. Perspective camera. 




Some text


|PathO_352_LKnot_P090T090a| `\quad` |PathO_352_LKnot_P090T180a| `\quad` |PathO_352_LKnot_P135T180a|

.. |PathO_352_LKnot_P090T090a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_352_LKnot_P090T090a.3D.xml.jpg
   :width: 30 %

.. |PathO_352_LKnot_P090T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_352_LKnot_P090T180a.3D.xml.jpg
   :width: 30 %

.. |PathO_352_LKnot_P135T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_352_LKnot_P135T180a.3D.xml.jpg
   :width: 22 %




**Left figure**: Lissajous knot 3-5-2. Orthographic camera. 

**Middle figure**: Lissajous knot 3-5-2. Orthographic camera. 

**Right figure**: Lissajous knot 3-5-2. Orthographic camera. 

















|newpage|


Lissajous knot 3-5-7
----------------------------


An example in C\#

.. code-block:: csharp

    double pi = Math.PI;
    double a1, k1, l1;
    double a2, k2, l2;
    double a3, k3, l3;
    a1 = 100; k1 = 3; l1 = 7;
    a2 = 100; k2 = 5; l2 = 5;
    a3 = 100; k3 = 7; l3 = 3;
    var x = (a1 * Math.Cos(k1 * t + l1)) / 50;
    var y = (a3 * Math.Cos(k3 * t + l3)) / 50;
    var z = (a2 * Math.Cos(k2 * t + l2)) / 50;


|PathP_357_LKnot_P090T090a| `\quad` |PathP_357_LKnot_P090T180a| `\quad` |PathP_357_LKnot_P135T180a|

.. |PathP_357_LKnot_P090T090a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_357_LKnot_P090T090a.3D.xml.jpg
   :width: 30 %

.. |PathP_357_LKnot_P090T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_357_LKnot_P090T180a.3D.xml.jpg
   :width: 30 %

.. |PathP_357_LKnot_P135T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathP_357_LKnot_P135T180a.3D.xml.jpg
   :width: 26 %




**Left figure**: Lissajous knot 3-5-7. Perspective camera. 

**Middle figure**: Lissajous knot 3-5-7. Perspective camera. 

**Right figure**: Lissajous knot 3-5-7. Perspective camera. 




Some text


|PathO_357_LKnot_P090T090a| `\quad` |PathO_357_LKnot_P090T180a| `\quad` |PathO_357_LKnot_P135T180a|

.. |PathO_357_LKnot_P090T090a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_357_LKnot_P090T090a.3D.xml.jpg
   :width: 30 %

.. |PathO_357_LKnot_P090T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_357_LKnot_P090T180a.3D.xml.jpg
   :width: 30 %

.. |PathO_357_LKnot_P135T180a| image:: ../_static/PathSurfaces/LissajousKnots/PathO_357_LKnot_P135T180a.3D.xml.jpg
   :width: 22 %




**Left figure**: Lissajous knot 3-5-7. Orthographic camera. 

**Middle figure**: Lissajous knot 3-5-7. Orthographic camera. 

**Right figure**: Lissajous knot 3-5-7. Orthographic camera. 



















