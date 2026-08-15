

.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}



.. |spacingend| raw:: latex

   \end{spacing}



.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />







Eigen: Polynomials
===============================================================================



RootsToMonicPolynomial
------------------------------------------------------------------------------------------------------------

.. method:: matA.RootsToMonicPolynomial(results, matB)

    Calculates the monic polynomial of the matrix.

    See also: Eigen :cite:p:`EigenMat170`.



PolyEval
------------------------------------------------------------------------------------------------------------

.. method:: matA.PolyEval(roots)

    Evaluates a real polynomial

    See also: Eigen :cite:p:`EigenMat170`.





PolyEvalComplex
------------------------------------------------------------------------------------------------------------

.. method:: matA.PolyEvalComplex(cplxroots))

    Evaluates a complex polynomial

    See also: Eigen :cite:p:`EigenMat170`.




PolynomialSolver
------------------------------------------------------------------------------------------------------------

.. method:: matA.PolynomialSolver()

    Call a polynomial solver

    See also: Eigen :cite:p:`EigenMat171`.





.. code-block:: vbnet

    Sub DemoCplxPoly()
        Console.WriteLine("Hello TestCplxPoly!")
        Dim digits = 35
        Dim roots, polynomial, evaluations As New dbl_mat_t
        Dim cplxroots, cplxevaluations As New cplx_mat_t

        roots.random(14, 1)
        roots.Print("roots: ")

        polynomial = roots.Roots_To_MonicPolynomial()
        polynomial.Print("polynomial: ")

        evaluations = polynomial.Poly_Eval(roots)
        evaluations.print("evaluations: ")

        cplxroots = polynomial.PolynomialSolver()
        cplxroots.print("cplxroots: ")

        cplxevaluations = polynomial.Poly_Eval_Complex(cplxroots)
        cplxevaluations.print("cplxevaluations: ")
    End Sub   



.. code-block:: none

    Hello TestCplxPoly!
    roots: 
    -9.974975E-001; 
     1.271706E-001; 
    -6.133915E-001; 
     6.174810E-001; 
     1.700186E-001; 
    -4.025391E-002; 
    -2.994171E-001; 
     7.919248E-001; 
     6.456801E-001; 
     4.932096E-001; 
    -6.517838E-001; 
     7.178869E-001; 
     4.210028E-001; 
     2.706992E-002; 

    polynomial: 
    -1.324054E-007; 
     3.782047E-006; 
     8.591809E-005; 
    -1.904538E-003; 
     8.812963E-003; 
     1.182314E-002; 
    -1.546459E-001; 
     2.026388E-001; 
     5.469460E-001; 
    -1.344237E+000; 
    -2.382208E-001; 
     2.544029E+000; 
    -1.154391E+000; 
    -1.409101E+000; 
     1.000000E+000; 

    evaluations: 
     1.082393E-015; 
     2.646978E-022; 
     1.958817E-018; 
    -3.192732E-018; 
     9.264423E-022; 
     2.646978E-023; 
     1.117025E-020; 
    -7.522727E-017; 
    -7.709588E-018; 
    -5.386335E-019; 
     5.154090E-018; 
    -2.002452E-017; 
    -3.200196E-020; 
     0.000000E+000; 

    cplxroots: 
    -0.997497+0.000000j; 
     0.717887+0.000000j; 
     0.791925+0.000000j; 
     0.645680+0.000000j; 
     0.617481+0.000000j; 
     0.493210+0.000000j; 
    -0.299417+0.000000j; 
     0.421003+0.000000j; 
    -0.040254+0.000000j; 
     0.027070+0.000000j; 
     0.127171+0.000000j; 
     0.170019+0.000000j; 
    -0.651784+0.000000j; 
    -0.613392+0.000000j; 

    cplxevaluations: 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 






