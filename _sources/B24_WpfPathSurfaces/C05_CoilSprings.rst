

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />







|newpage|


Coil springs
==============================================================


See also: https://en.wikipedia.org/wiki/Coil_spring

See also: https://en.wikipedia.org/wiki/Spring_(device)


Spring 2
--------------------------------------------



An example in C\#

.. code-block:: csharp

    var x = ((-3.75 * t + 100) * Math.Sin(t * Math.PI)) / 100;
    var z = (20 * t) / 100;
    var y = ((-3.75 * t + 100) * Math.Cos(t * Math.PI)) / 100;


Some text


|Path_Spiral2_Aa| `\quad` |Path_Spiral2_Ba|

.. |Path_Spiral2_Aa| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral2_Aa.3D.xml.jpg
   :width: 30 %

.. |Path_Spiral2_Ba| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral2_Ba.3D.xml.jpg
   :width: 30 %




**Left figure**: Spiral 2 (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 

**Right figure**: Spiral 2 (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 



|newpage|

Spring 6
---------------------------------------------


An example in C\#

.. code-block:: csharp

    var x = (Math.Sqrt(10000 - 100 * t * t) * Math.Sin(t * Math.PI)) / 100;
    var z = (20 * t) / 100;
    var y = (Math.Sqrt(10000 - 100 * t * t) * Math.Cos(t * Math.PI)) / 100;



Some text


|Path_Spiral6_Aa| `\quad` |Path_Spiral6_Ba|

.. |Path_Spiral6_Aa| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral6_Aa.3D.xml.jpg
   :width: 30 %

.. |Path_Spiral6_Ba| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral6_Ba.3D.xml.jpg
   :width: 30 %




**Left figure**: Spiral 6 (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 

**Right figure**: Spiral 6 (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 





|newpage|

Spring 7a
----------------------------------------


An example in C\#

.. code-block:: csharp

    var x = (Math.Sqrt(10000 - 100 * t * t) * Math.Sin(t * Math.PI)) / 100;
    var z = 209.22 * (Math.Tanh(0.1896 * t)) / 100;
    var y = (Math.Sqrt(10000 - 100 * t * t) * Math.Cos(t * Math.PI)) / 100;


Some text


|Path_Spiral7a_Aa| `\quad` |Path_Spiral7a_Ba|

.. |Path_Spiral7a_Aa| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral7a_Aa.3D.xml.jpg
   :width: 30 %

.. |Path_Spiral7a_Ba| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral7a_Ba.3D.xml.jpg
   :width: 30 %




**Left figure**: Spiral 7a (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 

**Right figure**: Spiral 7a (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 






|newpage|

Spring 7b
------------------------------------------


An example in C\#

.. code-block:: csharp

    var x = (200 * Math.Cos(0.05 * t * Math.PI) * Math.Sin(t * Math.PI)) / 100;
    var z = 209.22 * (Math.Tanh(0.1896 * t)) / 100;
    var y = (200 * Math.Cos(0.05 * t * Math.PI) * Math.Cos(t * Math.PI)) / 100;

Some text


|Path_Spiral7b_Aa| `\quad` |Path_Spiral7b_Ba|

.. |Path_Spiral7b_Aa| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral7b_Aa.3D.xml.jpg
   :width: 30 %

.. |Path_Spiral7b_Ba| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral7b_Ba.3D.xml.jpg
   :width: 30 %




**Left figure**: Spiral 7b (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 

**Right figure**: Spiral 7b (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 









|newpage|

Spring 7c
--------------------------------------------


An example in C\#

.. code-block:: csharp

    double e = Math.Exp(-(0.2 * t) * (0.2 * t));
    var x = (200 * e * Math.Sin(t * Math.PI)) / 100;
    var z = 209.22 * (Math.Tanh(0.1896 * t)) / 100;
    var y = (200 * e * Math.Cos(t * Math.PI)) / 100;


Some text


|Path_Spiral7c_Aa| `\quad` |Path_Spiral7c_Ba|

.. |Path_Spiral7c_Aa| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral7c_Aa.3D.xml.jpg
   :width: 30 %

.. |Path_Spiral7c_Ba| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral7c_Ba.3D.xml.jpg
   :width: 30 %




**Left figure**: Spiral 7c (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 

**Right figure**: Spiral 7c (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 








|newpage|

Spring 7d
------------------------------------------


An example in C\#

.. code-block:: csharp

    double e = Math.Exp(-(0.2 * t) * (0.2 * t));
    var x = ((200 - 140 * e) * Math.Sin(t * Math.PI)) / 100;
    var z = 207.46 * (Math.Tanh(0.2 * t)) / 100;
    var y = ((200 - 140 * e) * Math.Cos(t * Math.PI)) / 100;


Some text


|Path_Spiral7d_Aa| `\quad` |Path_Spiral7d_Ba|

.. |Path_Spiral7d_Aa| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral7d_Aa.3D.xml.jpg
   :width: 30 %

.. |Path_Spiral7d_Ba| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral7d_Ba.3D.xml.jpg
   :width: 30 %




**Left figure**: Spiral 7d (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 

**Right figure**: Spiral 7d (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 







|newpage|

Spring 8
-------------------------------------------


An example in C\#

.. code-block:: csharp

    var x = (200 * Math.Cos(t) * Math.Cos(Math.Atan(0.15 * t))) / 100;
    var z = -200 * Math.Sin(Math.Atan(0.15 * t)) / 100;
    var y = (200 * Math.Sin(t) * Math.Cos(Math.Atan(0.15 * t))) / 100;



Some text


|Path_Spiral8_Aa| `\quad` |Path_Spiral8_Ba|

.. |Path_Spiral8_Aa| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral8_Aa.3D.xml.jpg
   :width: 30 %

.. |Path_Spiral8_Ba| image:: ../_static/PathSurfaces/CoilSprings/Path_Spiral8_Ba.3D.xml.jpg
   :width: 30 %




**Left figure**: Spiral 8 (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 

**Right figure**: Spiral 8 (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 











