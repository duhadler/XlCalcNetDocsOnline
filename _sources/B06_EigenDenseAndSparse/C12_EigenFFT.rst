

.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}



.. |spacingend| raw:: latex

   \end{spacing}



.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />







|newpage|

Eigen: Fast Fourier Transform
===============================================================================

The default implementation is based on kissfft. 

The following design decisions were made concerning scaling and half-spectrum for real FFT.

The intent is to facilitate generic programming and ease migrating code from Matlab/octave. We think the default behavior of Eigen/FFT should favor correctness and generality over speed. Of course, the caller should be able to "opt-out" from this behavior and get the speed increase if they want it.

1) Scaling: Other libraries (FFTW,IMKL,KISSFFT) do not perform scaling, so there is a constant gain incurred after the forward&inverse transforms , so IFFT(FFT(x)) = Kx; this is done to avoid a vector-by-value multiply. The downside is that algorithms that worked correctly in Matlab/octave don't behave the same way once implemented in C++.

How Eigen/FFT differs: invertible scaling is performed so IFFT( FFT(x) ) = x.

2) Real FFT half-spectrum Other libraries use only half the frequency spectrum (plus one extra sample for the Nyquist bin) for a real FFT, the other half is the conjugate-symmetric of the first half. This saves them a copy and some memory. The downside is the caller needs to have special logic for the number of bins in complex vs real.

How Eigen/FFT differs: The full spectrum is returned from the forward transform. This facilitates generic template programming by obviating separate specializations for real vs complex. On the inverse transform, only half the spectrum is actually used if the output type is real. 




FFT FORWARD(X)
------------------------------------------------------------------------------------------------------------

.. method:: matA.FFTFwd()

    Calculates the Fourier transform.

    See also: Eigen :cite:p:`EigenMat180`.




FFT BACKWARD(X)
------------------------------------------------------------------------------------------------------------

.. method:: matA.FFTInv()

    Calculates the Fourier transform.


    See also: Eigen :cite:p:`EigenMat180`.




.. code-block:: vbnet

    Sub DemoCplxFFT()        
        Console.WriteLine("Hello DemoCplxFFT!")
        Dim digits = 15
        Dim n As Int32 = 4
        Dim A, B, TA, TB, TC, C, A2, B2, C2 As New cplx_mat_t
        Dim A_real, B_real, C_Real As New dbl_mat_t

        A.setZero(2*n,1)        
        A_real.Random(n, 1)
        For i=0 To n-1
            A(i) = New Complex(A_real(i), 0.0)
        Next
        A.Print("A: ")

        B.setZero(2*n,1)
        B_real.Random(n, 1)
        For i=0 To n-1
            B(i) = New Complex(B_real(i), 0.0)
        Next
        B.Print("B: ")

        TA = A.FFT_Fwd()
        TA.Print("TA: ")

        TB = B.FFT_Fwd()
        TB.Print("TB: ")

        TC.setZero(2*n,1)        
        For i=0 To 2*n-1
            TC(i) = TA(i) * TB(i)
        Next
        TC.Print("TC: ")
        C2 = TC.FFT_Inv()
        C2.Print("C2: ")

        C_Real.setZero(2*n,1)        
        For i As Integer = 0 To n-1
            For j As Integer = 0 To n-1
                C_Real(i+j) = C_Real(i+j) + A_Real(i) * B_Real(j)
            Next j
        Next i
        C_Real.Print("C_Real: ")
    End Sub



.. code-block:: none

    Hello DemoCplxFFT!
    A: 
    -0.997497+0.000000j; 
     0.127171+0.000000j; 
    -0.613392+0.000000j; 
     0.617481+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 

    B: 
     0.170019+0.000000j; 
    -0.040254+0.000000j; 
    -0.299417+0.000000j; 
     0.791925+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 
     0.000000+0.000000j; 

    TA: 
    -0.866237+0.000000j; 
    -1.344199+0.086843j; 
    -0.384106+0.490310j; 
    -0.650796-1.139940j; 
    -2.355541+0.000000j; 
    -0.650796+1.139940j; 
    -0.384106-0.490310j; 
    -1.344199-0.086843j; 

    TB: 
     0.622272+0.000000j; 
    -0.418421-0.232094j; 
     0.469436+0.832179j; 
     0.758458-0.830929j; 
    -0.881069+0.000000j; 
     0.758458+0.830929j; 
     0.469436-0.832179j; 
    -0.418421+0.232094j; 

    TC: 
    -0.539036+0.000000j; 
     0.582597+0.275644j; 
    -0.588339-0.089476j; 
    -1.440810-0.323831j; 
     2.075395+0.000000j; 
    -1.440810+0.323831j; 
    -0.588339+0.089476j; 
     0.582597-0.275644j; 

    C2: 
    -0.169593+0.000000j; 
     0.061775+0.000000j; 
     0.189261+0.000000j; 
    -0.698345+0.000000j; 
     0.259513+0.000000j; 
    -0.670644+0.000000j; 
     0.488999+0.000000j; 
     0.000000+0.000000j; 

    C_Real: 
    -1.695931E-001; 
     6.177455E-002; 
     1.892607E-001; 
    -6.983454E-001; 
     2.595135E-001; 
    -6.706443E-001; 
     4.889985E-001; 
     0.000000E+000; 





