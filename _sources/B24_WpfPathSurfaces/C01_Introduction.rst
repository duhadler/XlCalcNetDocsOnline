

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />






Introduction to path surfaces
==============================================================




Borromean rings, A, B, C
---------------------------------------------------------

Some text explaining the importance of building the mesh in x-direction.


An example in C\#, for A

.. code-block:: csharp

    var r = Math.Sqrt(3) / 3;
    var x = Math.Cos(t);
    var y = Math.Sin(t) + r;
    var z = Math.Cos(3 * t) / 3;


An example in C\#, for B

.. code-block:: csharp

    var r = Math.Sqrt(3) / 3;
    var x = Math.Cos(t) + 0.5;
    var y = Math.Sin(t) - r / 2;
    var z = Math.Cos(3 * t) / 3;


An example in C\#, for C

.. code-block:: csharp

    var r = Math.Sqrt(3) / 3;
    var x = Math.Cos(t) - 0.5;
    var y = Math.Sin(t) - r / 2;
    var z = Math.Cos(3 * t) / 3;







|newpage|



Ellipses, A, B, C
---------------------------------------------------------

Some text explaining the importance of building the mesh in x-direction.


An example in C\#, for A, B, C

.. code-block:: csharp

    var x = 2 * Math.Cos(t);
    var y = Math.Sin(t);
    var z = 0.0;

For A, the final rotations are: X=0, Y=0, Z=0.

For B, the final rotations are: X=90, Y=0, Z=90.

For C, the final rotations are: X=0, Y=90, Z=90.




|newpage|



Trefoil 2
---------------------------------------------------------

Some text explaining the importance of building the mesh in x-direction.


An example in C\#, for A, B, C

.. code-block:: csharp

    var D = 2.0; //  D = 1.0;  D = 2.0;
    var x = D * Math.Sin(t) + 2 * Math.Sin(2 * t);
    var y = D * Math.Cos(t) - 2 * Math.Cos(2 * t);
    var z = -D * Math.Sin(3 * t);




|newpage|




Formatting options for path surfaces, Trefoil 5
----------------------------------------------------


These are the rough versions


An example in C\#, for A, B, C

.. code-block:: csharp

    var D = 1.0; //  D = 1.0;  D = 2.0;
    var x = D * Math.Sin(t) + 2 * Math.Sin(2 * t);
    var y = D * Math.Cos(t) - 2 * Math.Cos(2 * t);
    var z = -D * Math.Sin(3 * t);



|TestALines_Trefoil05_a| `\quad` |TestALines_Trefoil05W_a| `\quad` |TestALines_Trefoil05WO_a|

.. |TestALines_Trefoil05_a| image:: ../_static/PathSurfaces/Intro/TestALines_Trefoil05_a.3D.xml.jpg
   :width: 30 %

.. |TestALines_Trefoil05W_a| image:: ../_static/PathSurfaces/Intro/TestALines_Trefoil05W_a.3D.xml.jpg
   :width: 30 %

.. |TestALines_Trefoil05WO_a| image:: ../_static/PathSurfaces/Intro/TestALines_Trefoil05WO_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Trefoil, rough version (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 

**Middle figure**: Trefoil, rough version (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 

**Right figure**: Trefoil, rough version (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 






These are the smooth versions



|TestALines_Trefoil05S_a| `\quad` |TestALines_Trefoil05WS_a| `\quad` |TestALines_Trefoil05WSO_a|

.. |TestALines_Trefoil05S_a| image:: ../_static/PathSurfaces/Intro/TestALines_Trefoil05S_a.3D.xml.jpg
   :width: 30 %

.. |TestALines_Trefoil05WS_a| image:: ../_static/PathSurfaces/Intro/TestALines_Trefoil05WS_a.3D.xml.jpg
   :width: 30 %

.. |TestALines_Trefoil05WSO_a| image:: ../_static/PathSurfaces/Intro/TestALines_Trefoil05WSO_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Trefoil, smooth version (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 

**Middle figure**: Trefoil, smooth version (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 

**Right figure**: Trefoil, smooth version (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`). 



