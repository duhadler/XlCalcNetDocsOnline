

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />






|newpage|


Boost/Odeint: Ordinary differential equations
==============================================================


Boost Odeint is a library for solving initial value problems (IVP) of ordinary differential equations. Mathematically, these problems are formulated as follows: 

.. math ::  x'(t) = f(x,t), x(0) = x0. 

x and f can be vectors and the solution is some function x(t) fulfilling both equations above. In the following we will refer to x'(t) also dxdt which is also our notation for the derivative in the source code. 

Ordinary differential equations occur nearly everywhere in natural sciences. For example, the whole Newtonian mechanics are described by second order differential equations. Be sure, you will find them in every discipline. They also occur if partial differential equations (PDEs) are discretized. Then, a system of coupled ordinary differential occurs, sometimes also referred as lattices ODEs. 


odeint provides a quite large number of different steppers such that the user is left with the question of which stepper fits his needs. Our personal recommendations are: 

runge\_kutta\_dopri5 is maybe the best default stepper. It has step size control as well as dense-output functionality. Simple create a dense-output stepper by make\_dense\_output( 1.0e-6 , 1.0e-5 , runge\_kutta\_dopri5< state\_type >() ). 

runge\_kutta4 is a good stepper for constant step sizes. It is widely used and very well known. If you need to create artificial time series this stepper should be the first choice. 

'runge\_kutta\_fehlberg78' is similar to the 'runge\_kutta4' with the advantage that it has higher precision. It can also be used with step size control. 

adams\_bashforth\_moulton is very well suited for ODEs where the r.h.s. is expensive (in terms of computation time). It will calculate the system function only once during each step. 

See also:  BoostMath :cite:p:`BoostOdeint01`,  Wikipedia :cite:p:`WikipediaAlg50`.




|newpage|


Runge-Kutta 4 method, constant stepper
------------------------------------------------------------------------------------------------------------

.. method:: ctxboost.RungeKutta4Const(F1, F2, matInput, StartTime, EndTime, \mathrm{d}t)


    Solves Ordinary differential equations using the Runge-Kutta 4 method with a constant stepper.

    See also:  Wikipedia :cite:p:`WikipediaAlg51`, :cite:t:`Runge1895`, :cite:t:`Kutta1901`.



    In numerical analysis, the Runge-Kutta methods are an important family of implicit and explicit iterative methods, which are used in temporal discretization for the approximation of solutions of ordinary differential equations. These techniques were developed around 1900 by the German mathematicians C. Runge and M. W. Kutta.

    See the article on numerical methods for ordinary differential equations for more background and other methods. See also List of Runge-Kutta methods.

    One member of the family of Runge-Kutta methods is often referred to as "RK4", "classical Runge-Kutta method" or simply as "the Runge-Kutta method".

    Let an initial value problem be specified as follows.


    Here, y is an unknown function (scalar or vector) of time t which we would like to approximate; we are told that , the rate at which y changes, is a function of t and of y itself. At the initial time  the corresponding y-value is . The function f and the data ,  are given.



**Example:**

.. code-block:: vbnet

    Public Sub matLorenz(x As dbl_mat_t, dxdt As dbl_mat_t)
        Dim sigma, R, b As Double
        sigma = 10: R = 28: b = 8 / 3
        dxdt(0) = sigma * ( x(1) - x(0) )
        dxdt(1) = R * x(0) - x(1) - x(0) * x(2)
        dxdt(2) = -b * x(2) + x(0) * x(1)
    End Sub

    Sub DemoLorenzOdeintLocal()
        Console.WriteLine( "DemoLorenzOdeintLocal(matX, StartTime, EndTime, \mathrm{d}t)")
        Dim matX3 As New dbl_mat_t()
        matX3.resize(3,1)
        matX3(0) = 10.0
        matX3(1) = 10.0
        matX3(2) = 10.0
        Dim StartTime = 0.0
        Dim EndTime = 10.0
        Dim \mathrm{d}t = 0.1
        matX3.print("matX at StartTime", 15)
        Dim ODE As New Odeint(AddressOf matLorenz, matX3, StartTime, EndTime, \mathrm{d}t)
        ODE.Integrate()
        matX3.print("matX at EndTime", 15)
    End Sub


This produces the following output:

.. code-block:: none

    DemoLorenzOdeintLocal(matX, StartTime, EndTime, \mathrm{d}t)
    matX at StartTime
    10, 
    10, 
    10, 

    matX at EndTime
    -2.43203453419697, 
    0.560815431795122, 
    25.4697563106702,





|newpage|



Cash-Karp method, constant stepper
------------------------------------------------------------------------------------------------------------

.. method:: ctxboost.CashKarpConst(F1, F2, matInput, StartTime, EndTime, \mathrm{d}t)


    Solves Ordinary differential equations using the Cash-Karp method, using a constant stepper

    See also:  Wikipedia :cite:p:`WikipediaAlg52`, :cite:t:`Cash1990`.

    In numerical analysis, the Cash-Karp method is a method for solving ordinary differential equations (ODEs). It was proposed by Professor Jeff R. Cash [1] from Imperial College London and Alan H. Karp from IBM Scientific Center. The method is a member of the Runge-Kutta family of ODE solvers. More specifically, it uses six function evaluations to calculate fourth- and fifth-order accurate solutions. The difference between these solutions is then taken to be the error of the (fourth order) solution. This error estimate is very convenient for adaptive stepsize integration algorithms. Other similar integration methods are Fehlberg (RKF) and Dormand-Prince (RKDP).






|newpage|


Dormand-Prince 5 method, constant stepper
------------------------------------------------------------------------------------------------------------

.. method:: ctxboost.DormandPrince5Const(F1, F2, matInput, StartTime, EndTime, \mathrm{d}t, epsabs, epsrel)


    Solves Ordinary differential equations using the Dormand-Prince method, using a constant stepper

    See also:  Wikipedia :cite:p:`WikipediaAlg53`, :cite:t:`Dormand1980`.


    In numerical analysis, the Dormand-Prince method, or DOPRI method, is an explicit method for solving ordinary differential equations \citep{Dormand1980}. The method is a member of the Runge-Kutta family of ODE solvers. More specifically, it uses six function evaluations to calculate fourth- and fifth-order accurate solutions. The difference between these solutions is then taken to be the error of the (fourth-order) solution. This error estimate is very convenient for adaptive stepsize integration algorithms. Other similar integration methods are Fehlberg (RKF) and Cash-Karp (RKCK).

    The Dormand-Prince method has seven stages, but it uses only six function evaluations per step because it has the FSAL (First Same As Last) property: the last stage is evaluated at the same point as the first stage of the next step. Dormand and Prince choose the coefficients of their method to minimize the error of the fifth-order solution. This is the main difference with the Fehlberg method, which was constructed so that the fourth-order solution has a small error. For this reason, the Dormand-Prince method is more suitable when the higher-order solution is used to continue the integration, a practice known as local extrapolation (Shampine 1986; Hairer, Nørsett \& Wanner 2008, pp. 178-179).








|newpage|


Fehlberg 78 method, constant stepper
------------------------------------------------------------------------------------------------------------

.. method:: ctxboost.Fehlberg78Const(F1, F2, matInput, StartTime, EndTime, \mathrm{d}t, epsabs, epsrel)


    Solves Ordinary differential equations using the Fehlberg 78 method, using a constant stepper

    See also:  Wikipedia :cite:p:`WikipediaAlg54`, :cite:t:`Fehlberg1970`.

    In mathematics, the Runge-Kutta-Fehlberg method (or Fehlberg method) is an algorithm in numerical analysis for the numerical solution of ordinary differential equations. It was developed by the German mathematician Erwin Fehlberg and is based on the large class of Runge-Kutta methods.

    The novelty of Fehlberg's method is that it is an embedded method from the Runge-Kutta family, meaning that identical function evaluations are used in conjunction with each other to create methods of varying order and similar error constants. The method presented in Fehlberg's 1969 paper has been dubbed the RKF45 method, and is a method of order O(h4) with an error estimator of order O(h5).[1] By performing one extra calculation, the error in the solution can be estimated and controlled by using the higher-order embedded method that allows for an adaptive stepsize to be determined automatically.




|newpage|



Adams-Bashforth-Moulton, constant stepper
------------------------------------------------------------------------------------------------------------

.. method:: ctxboost.AdamsBashforthMoultonConst(F1, F2, matInput, StartTime, EndTime, \mathrm{d}t, epsabs, epsrel)


    Solves Ordinary differential equations using the Adams-Bashforth-Moulton method, using a constant stepper

    See also:  Wikipedia :cite:p:`WikipediaAlg55`.


    The methods of Euler, Heun, Taylor and Runge-Kutta are called single-step methods because they use only the information from one previous point to compute the successive point, that is, only the initial point    is used to compute    and in general    is needed to compute  .  After several points have been found it is feasible to use several prior points in the calculation.  The Adams-Bashforth-Moulton method uses   in the calculation of .  This method is not self-starting;  four initial points  , , ,  and  must be given in advance in order to generate the points .  

    A desirable feature of a multistep method is that the local truncation error (L. T. E.) can be determined and a correction term can be included, which improves the accuracy of the answer at each step.  Also, it is possible to determine if the step size is small enough to obtain an accurate value for  , yet large enough so that unnecessary and time-consuming calculations are eliminated.  If the code for the subroutine is fine-tuned, then the combination of a  predictor and corrector requires only two function evaluations of  f(t,y)  per step. 


|newpage|


Cash-Karp method, adaptive stepper
------------------------------------------------------------------------------------------------------------

.. method:: ctxboost.CashKarpAdaptive(F1, F2, matInput, StartTime, EndTime, \mathrm{d}t, epsabs, epsrel)


    Solves Ordinary differential equations using the Adams-Bashforth-Moulton method with an adaptive stepper.

    See also:  Wikipedia :cite:p:`WikipediaAlg52`, :cite:t:`Cash1990`.

    In numerical analysis, the Cash-Karp method is a method for solving ordinary differential equations (ODEs). It was proposed by Professor Jeff R. Cash [1] from Imperial College London and Alan H. Karp from IBM Scientific Center. The method is a member of the Runge-Kutta family of ODE solvers. More specifically, it uses six function evaluations to calculate fourth- and fifth-order accurate solutions. The difference between these solutions is then taken to be the error of the (fourth order) solution. This error estimate is very convenient for adaptive stepsize integration algorithms. Other similar integration methods are Fehlberg (RKF) and Dormand-Prince (RKDP).




|newpage|



Dormand-Prince 5 method, adaptive stepper
------------------------------------------------------------------------------------------------------------

.. method:: ctxboost.DormandPrince5Adaptive(F1, F2, matInput, StartTime, EndTime, \mathrm{d}t, epsabs, epsrel)


    Solves Ordinary differential equations using the Dormand-Prince 5 method with an adaptive stepper.

    See also:  Wikipedia :cite:p:`WikipediaAlg53`, :cite:t:`Dormand1980`.



    In numerical analysis, the Dormand-Prince method, or DOPRI method, is an explicit method for solving ordinary differential equations \citep{Dormand1980}. The method is a member of the Runge-Kutta family of ODE solvers. More specifically, it uses six function evaluations to calculate fourth- and fifth-order accurate solutions. The difference between these solutions is then taken to be the error of the (fourth-order) solution. This error estimate is very convenient for adaptive stepsize integration algorithms. Other similar integration methods are Fehlberg (RKF) and Cash-Karp (RKCK).

    The Dormand-Prince method has seven stages, but it uses only six function evaluations per step because it has the FSAL (First Same As Last) property: the last stage is evaluated at the same point as the first stage of the next step. Dormand and Prince choose the coefficients of their method to minimize the error of the fifth-order solution. This is the main difference with the Fehlberg method, which was constructed so that the fourth-order solution has a small error. For this reason, the Dormand-Prince method is more suitable when the higher-order solution is used to continue the integration, a practice known as local extrapolation (Shampine 1986; Hairer, Nørsett \& Wanner 2008, pp. 178-179).







|newpage|


Fehlberg 78 method, adaptive stepper
------------------------------------------------------------------------------------------------------------

.. method:: ctxboost.Fehlberg78Adaptive(F1, F2, matInput, StartTime, EndTime, \mathrm{d}t, epsabs, epsrel)


    Solves Ordinary differential equations using the Fehlberg 78 method with an adaptive stepper.

    See also:  Wikipedia :cite:p:`WikipediaAlg54`, :cite:t:`Fehlberg1970`.



    In mathematics, the Runge-Kutta-Fehlberg method (or Fehlberg method) is an algorithm in numerical analysis for the numerical solution of ordinary differential equations. It was developed by the German mathematician Erwin Fehlberg and is based on the large class of Runge-Kutta methods.

    The novelty of Fehlberg's method is that it is an embedded method from the Runge-Kutta family, meaning that identical function evaluations are used in conjunction with each other to create methods of varying order and similar error constants. The method presented in Fehlberg's 1969 paper has been dubbed the RKF45 method, and is a method of order O(h4) with an error estimator of order O(h5).[1] By performing one extra calculation, the error in the solution can be estimated and controlled by using the higher-order embedded method that allows for an adaptive stepsize to be determined automatically.



|newpage|



Bulirsch-Stoer method, adaptive stepper
------------------------------------------------------------------------------------------------------------

.. method:: ctxboost.BulirschStoerAdaptive(F1, F2, matInput, StartTime, EndTime, \mathrm{d}t, epsabs, epsrel)


    Solves Ordinary differential equations using the Bulirsch-Stoer method, with an adaptive stepper

    See also:  Wikipedia :cite:p:`WikipediaAlg56`, :cite:t:`Hairer1993`.


    In numerical analysis, the Bulirsch-Stoer algorithm is a method for the numerical solution of ordinary differential equations which combines three powerful ideas: Richardson extrapolation, the use of rational function extrapolation in Richardson-type applications, and the modified midpoint method, to obtain numerical solutions to ordinary differential equations (ODEs) with high accuracy and comparatively little computational effort. It is named after Roland Bulirsch and Josef Stoer. It is sometimes called the Gragg-Bulirsch-Stoer (GBS) algorithm because of the importance of a result about the error function of the modified midpoint method, due to William B. Gragg.




|newpage|


Dormand-Prince 5 method, dense output stepper
------------------------------------------------------------------------------------------------------------

.. method:: ctxboost.DormandPrince5DenseOutput(F1, F2, matInput, StartTime, EndTime, \mathrm{d}t, epsabs, epsrel)


    Solves Ordinary differential equations using the Dormand-Prince 5 method, with a dense output stepper.

    See also:  Wikipedia :cite:p:`WikipediaAlg53`, :cite:t:`Dormand1980`.

    In numerical analysis, the Dormand-Prince method, or DOPRI method, is an explicit method for solving ordinary differential equations \citep{Dormand1980}. The method is a member of the Runge-Kutta family of ODE solvers. More specifically, it uses six function evaluations to calculate fourth- and fifth-order accurate solutions. The difference between these solutions is then taken to be the error of the (fourth-order) solution. This error estimate is very convenient for adaptive stepsize integration algorithms. Other similar integration methods are Fehlberg (RKF) and Cash-Karp (RKCK).

    The Dormand-Prince method has seven stages, but it uses only six function evaluations per step because it has the FSAL (First Same As Last) property: the last stage is evaluated at the same point as the first stage of the next step. Dormand and Prince choose the coefficients of their method to minimize the error of the fifth-order solution. This is the main difference with the Fehlberg method, which was constructed so that the fourth-order solution has a small error. For this reason, the Dormand-Prince method is more suitable when the higher-order solution is used to continue the integration, a practice known as local extrapolation (Shampine 1986; Hairer, Nørsett \& Wanner 2008, pp. 178-179).



|newpage|




Bulirsch-Stoer method, dense output stepper
------------------------------------------------------------------------------------------------------------

.. method:: ctxboost.BulirschStoerDenseOutput(F1, F2, matInput, StartTime, EndTime, \mathrm{d}t, epsabs, epsrel)


    Solves Ordinary differential equations using the Bulirsch-Stoer method, with a dense output stepper.

    See also:  Wikipedia :cite:p:`WikipediaAlg56`, :cite:t:`Hairer1993`.

    In numerical analysis, the Bulirsch-Stoer algorithm is a method for the numerical solution of ordinary differential equations which combines three powerful ideas: Richardson extrapolation, the use of rational function extrapolation in Richardson-type applications, and the modified midpoint method, to obtain numerical solutions to ordinary differential equations (ODEs) with high accuracy and comparatively little computational effort. It is named after Roland Bulirsch and Josef Stoer. It is sometimes called the Gragg-Bulirsch-Stoer (GBS) algorithm because of the importance of a result about the error function of the modified midpoint method, due to William B. Gragg.








