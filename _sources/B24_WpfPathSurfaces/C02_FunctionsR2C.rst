

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />





|newpage|

Functions with real input and complex results
==============================================================





Expj (Cis) function
--------------------------------------

Returns `e^{iz} = \cos(z) + i \sin(z)`. See also Wikipedia :cite:p:`WikipediaFun1035`, MathWorld :cite:p:`WolframFun1035`.




An example in C\#, for real part only

.. code-block:: csharp

    var y = Math.Sin(t);
    var x = t;
    var z = 0;



An example in C\#, for imaginary part only

.. code-block:: csharp

    var z = -Math.Cos(t);
    var x = t;
    var y = 0;



An example in C\#, for real and imaginary part combined

.. code-block:: csharp

var x = Math.Sin(t);
var y = -Math.Cos(t);
var z = t;



Some text


|Path_Func_Expj_2Dx_a| `\quad` |Path_Func_Expj_2Dy_a| `\quad` |Path_Func_Expj_a|

.. |Path_Func_Expj_2Dx_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_Expj_2Dx_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_Expj_2Dy_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_Expj_2Dy_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_Expj_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_Expj_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Expj (Cis) function, real part only. Orthographic camera. 

**Middle figure**: Expj (Cis) function, imaginary part only. Orthographic camera. 

**Right figure**: Expj (Cis) function as full 3D curve. Orthographic camera. 








|newpage|


Hankel function of the first kind `H_{1, \nu}(x)`
----------------------------------------------------------

Returns the Hankel function of the first kind, defined as `\displaystyle H^{(1)}_{\nu}(x) = J_{\nu}(x) + i Y_{\nu}(x)`.

See also  Wikipedia :cite:p:`WikipediaFun142`, MathWorld :cite:p:`WolframFun142a`, NIST :cite:p:`DLMFun142`, BoostMath :cite:p:`BoostFun142`.



An example in C\#, for real part only

.. code-block:: csharp

    var y = math53.bessel_j0(t);
    var x = t;
    var z = 0;



An example in C\#, for imaginary part only

.. code-block:: csharp

    var z = -math53.bessel_y0(t);
    var x = t;
    var y = 0;



An example in C\#, for real and imaginary part combined

.. code-block:: csharp

    var z = math53.bessel_j0(t);
    var y = -math53.bessel_y0(t);
    var x = t;




Some text


|Path_Func_Hankel1_2Dx_a| `\quad` |Path_Func_Hankel1_2Dy_a| `\quad` |Path_Func_Hankel1_a|

.. |Path_Func_Hankel1_2Dx_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_Hankel1_2Dx_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_Hankel1_2Dy_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_Hankel1_2Dy_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_Hankel1_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_Hankel1_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Hankel function of the first kind `H_{1, \nu}(x)`, real part only. Orthographic camera. 

**Middle figure**: Hankel function of the first kind `H_{1, \nu}(x)`, imaginary part only. Orthographic camera. 

**Right figure**: Hankel function of the first kind `H_{1, \nu}(x)`, as full 3D curve. Orthographic camera. 









|newpage|

Hankel function of the second kind `H_{2, \nu}(x)`
------------------------------------------------------------

Returns the Hankel function of the second kind, defined as `\displaystyle H^{(2)}_{\nu}(x) = J_{\nu}(x) - i Y_{\nu}(x)`.


See also  Wikipedia :cite:p:`WikipediaFun142`, MathWorld :cite:p:`WolframFun142b`, NIST :cite:p:`DLMFun142`, BoostMath :cite:p:`BoostFun142`.



An example in C\#, for real part only

.. code-block:: csharp

    var y = math53.bessel_j0(t);
    var x = t;
    var z = 0;



An example in C\#, for imaginary part only

.. code-block:: csharp

    var z = math53.bessel_y0(t);
    var x = t;
    var y = 0;



An example in C\#, for real and imaginary part combined

.. code-block:: csharp

    var z = math53.bessel_j0(t);
    var y = math53.bessel_y0(t);
    var x = t;





Some text


|Path_Func_Hankel2_2Dx_a| `\quad` |Path_Func_Hankel2_2Dy_a| `\quad` |Path_Func_Hankel2_a|

.. |Path_Func_Hankel2_2Dx_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_Hankel2_2Dx_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_Hankel2_2Dy_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_Hankel2_2Dy_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_Hankel2_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_Hankel2_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Hankel function of the second kind `H_{2, \nu}(x)`, real part only. Orthographic camera. 

**Middle figure**: Hankel function of the second kind `H_{2, \nu}(x)`, imaginary part only. Orthographic camera. 

**Right figure**: Hankel function of the second kind `H_{2, \nu}(x)`, as full 3D curve. Orthographic camera. 








|newpage|

Kelvin functions ber and bei
------------------------------------------

Returns the Kelvin functions ber bei. See also  Wikipedia :cite:p:`WikipediaFun1040`, MathWorld :cite:p:`WolframFun1040`, NIST :cite:p:`DLMFun1040`.


The following conventions are used as in Maple (with `a = \sqrt{2}/2`):

.. math::  \text{ber}(\nu, x) + i \text{bei}(\nu, x) = J_{\nu}(x(-a + i a))

.. math::  \text{ber}(\nu, x) - i \text{bei}(\nu, x) = J_{\nu}(x(-a - i a))



An example in C\#, for real part only

.. code-block:: csharp

    var a = math53.exp(t / math53.sqrt(2));
    var y = math53.kelvin_ber(t) / a;
    var x = t;
    var z = 0;



An example in C\#, for imaginary part only

.. code-block:: csharp

    var a = math53.exp(t / math53.sqrt(2));
    var z = -math53.kelvin_bei(t) / a;
    var x = t;
    var y = 0;



An example in C\#, for real and imaginary part combined

.. code-block:: csharp

    var a = math53.exp(t / math53.sqrt(2));
    var z = math53.kelvin_ber(t) / a;
    var y = -math53.kelvin_bei(t) / a;
    var x = t;




Some text


|Path_Func_KelvinBerBei_2Dx_a| `\quad` |Path_Func_KelvinBerBei_2Dy_a| `\quad` |Path_Func_KelvinBerBei_a|

.. |Path_Func_KelvinBerBei_2Dx_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_KelvinBerBei_2Dx_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_KelvinBerBei_2Dy_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_KelvinBerBei_2Dy_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_KelvinBerBei_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_KelvinBerBei_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Kelvin functions ber. Orthographic camera. 

**Middle figure**: Kelvin function bei. Orthographic camera. 

**Right figure**: Kelvin functions ber and bei, as full 3D curve. Orthographic camera. 







|newpage|

Kelvin functions ker and kei
---------------------------------------

Returns the Kelvin function ker.  See also  Wikipedia :cite:p:`WikipediaFun1042`, MathWorld :cite:p:`WolframFun1042`, NIST :cite:p:`DLMFun1040`.


The following conventions are used as in Maple (with `a = \sqrt{2}/2`):


.. math::  \text{ker}(\nu, x) + i \text{kei}(\nu, x) = e^{-i \nu \pi/2} K_{\nu}(x(a + i a))

.. math::  \text{ker}(\nu, x) - i \text{kei}(\nu, x) = e^{i \nu \pi/2} K_{\nu}(x(a - i a))



An example in C\#, for real part only

.. code-block:: csharp

    var a = math53.exp(t / math53.sqrt(2));
    var y = math53.kelvin_ker(t) * a;
    var x = t;
    var z = 0;



An example in C\#, for imaginary part only

.. code-block:: csharp

    var a = math53.exp(t / math53.sqrt(2));
    var z = -math53.kelvin_kei(t) * a;
    var x = t;
    var y = 0;



An example in C\#, for real and imaginary part combined

.. code-block:: csharp

    var a = math53.exp(t / math53.sqrt(2));
    var z = math53.kelvin_ker(t) * a;
    var y = -math53.kelvin_kei(t) * a;
    var x = t;




Some text


|Path_Func_KelvinKerKei_2Dx_a| `\quad` |Path_Func_KelvinKerKei_2Dy_a| `\quad` |Path_Func_KelvinKerKei_a|

.. |Path_Func_KelvinKerKei_2Dx_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_KelvinKerKei_2Dx_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_KelvinKerKei_2Dy_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_KelvinKerKei_2Dy_a.3D.xml.jpg
   :width: 30 %

.. |Path_Func_KelvinKerKei_a| image:: ../_static/PathSurfaces/Real2Cplx/Path_Func_KelvinKerKei_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Kelvin functions ker. Orthographic camera. 

**Middle figure**: Kelvin function kei. Orthographic camera. 

**Right figure**: Kelvin functions ker and kei, as full 3D curve. Orthographic camera. 




