




.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}



.. |spacingend| raw:: latex

   \end{spacing}







.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />







|newpage|




Discrete Fourier transform (DFT)
==========================================================


Overview
----------------------------------------------------------------

Fourier analysis is a method for expressing a function as a sum of periodic components, and for recovering the function from those components. When both the function and its Fourier transform are replaced with discretized counterparts, it is called the discrete Fourier transform (DFT). The DFT has become a mainstay of numerical computing in part because of a very fast algorithm for computing it, called the Fast Fourier Transform (FFT).

It has applications in digital signal processing, e.g., for filtering, and in this context the discretized input to the transform is customarily referred to as a signal, which exists in the time domain. The output is called a spectrum or transform and exists in the frequency domain.

There are many ways to define the DFT, varying in the sign of the exponent, normalization, etc. In this implementation, the DFT is defined as

.. math:: A_k = \sum_{m=0}^{n-1} a_m \exp \left( -2 \pi i \frac{mk}{n} \right), \quad k = 0,\ldots,n-1.

The DFT is in general defined for complex inputs and outputs, and a single-frequency component at linear frequency `f` is represented by a complex exponential `a_m = \exp(2 \pi i f m \Delta t)`, where `\Delta t` is the sampling interval.

The values in the result follow so-called "standard" order: If ``A = fft(a, n)``, then ``A[0]`` contains the zero-frequency term (the sum of the signal), which is always purely real for real inputs. Then ``A[1:n/2]`` contains the positive-frequency terms, and ``A[n/2+1:]`` contains the negative-frequency terms, in order of decreasingly negative frequency. For an even number of input points, ``A[n/2]`` represents both positive and negative Nyquist frequency, and is also purely real for real input. For an odd number of input points, ``A[(n-1)/2]`` contains the largest positive frequency, while ``A[(n+1)/2]`` contains the largest negative frequency. The routine ``np.fft.fftfreq(n)`` returns an array giving the frequencies of corresponding elements in the output. The routine ``np.fft.fftshift(A)`` shifts transforms and their frequencies to put the zero-frequency components in the middle, and ``np.fft.ifftshift(A)`` undoes that shift.

When the input a is a time-domain signal and ``A = fft(a), np.abs(A)`` is its amplitude spectrum and ``np.abs(A)**2`` is its power spectrum. The phase spectrum is obtained by ``np.angle(A)``.

The inverse DFT is defined as

.. math:: a_m = \frac{1}{n} \sum_{k=0}^{n-1} A_k \exp \left( 2 \pi i \frac{mk}{n} \right), \quad m = 0,\ldots, n-1.

It differs from the forward transform by the sign of the exponential argument and the default normalization by `1/n`.




One-dimensional discrete Fourier Transform (fft)
-------------------------------------------------------------------------------

.. method:: ctx.fft(res, data, population, opt)

    Compute the one-dimensional discrete Fourier Transform.

    This function computes the one-dimensional n-point discrete Fourier Transform (DFT) with the efficient Fast Fourier Transform (FFT) algorithm. 



    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html#numpy.fft.fft




    Return the real part of the complex argument.

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.fft.fft(np.exp(2j * np.pi * np.arange(8) / 8))
        array([-2.33486982e-16+1.14423775e-17j,  8.00000000e+00-1.25557246e-15j,
                2.33486982e-16+2.33486982e-16j,  0.00000000e+00+1.22464680e-16j,
               -1.14423775e-17+2.33486982e-16j,  0.00000000e+00+5.20784380e-16j,
                1.14423775e-17+1.14423775e-17j,  0.00000000e+00+1.22464680e-16j])

    In this example, real input has an FFT which is Hermitian, i.e., symmetric in the real part and anti-symmetric in the imaginary part, as described in the numpy.fft documentation:

        >>> import matplotlib.pyplot as plt
        >>> t = np.arange(256)
        >>> sp = np.fft.fft(np.sin(t))
        >>> freq = np.fft.fftfreq(t.shape[-1])
        >>> plt.plot(freq, sp.real, freq, sp.imag)
        [<matplotlib.lines.Line2D object at 0x...>, <matplotlib.lines.Line2D object at 0x...>]
        >>> plt.show()








One-dimensional inverse discrete Fourier Transform (ifft)
-------------------------------------------------------------------------------

.. method:: ctx.ifft(res, data, population, opt)

    Compute the one-dimensional inverse discrete Fourier Transform.

    This function computes the inverse of the one-dimensional n-point discrete Fourier transform computed by fft. In other words, ``ifft(fft(a)) == a`` to within numerical accuracy. 

    The input should be ordered in the same way as is returned by fft, i.e.,

    * ``a[0]`` should contain the zero frequency term,

    * ``a[1:n//2]`` should contain the positive-frequency terms,

    * ``a[n//2 + 1:]`` should contain the negative-frequency terms, in increasing order starting from the most negative frequency.

    For an even number of input points, ``A[n//2]`` represents the sum of the values at the positive and negative Nyquist frequencies, as the two are aliased together. 

    If the input parameter n is larger than the size of the input, the input is padded by appending zeros at the end. Even though this is the common approach, it might lead to surprising results. If a different padding is desired, it must be performed before calling ifft.


    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft



    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.fft.ifft([0, 4, 0, 0])
        array([ 1.+0.j,  0.+1.j, -1.+0.j,  0.-1.j]) # may vary

    Create and plot a band-limited signal with random phases:

        >>> import matplotlib.pyplot as plt
        >>> t = np.arange(400)
        >>> n = np.zeros((400,), dtype=complex)
        >>> n[40:60] = np.exp(1j*np.random.uniform(0, 2*np.pi, (20,)))
        >>> s = np.fft.ifft(n)
        >>> plt.plot(t, s.real, label='real')
        [<matplotlib.lines.Line2D object at ...>]
        >>> plt.plot(t, s.imag, '--', label='imaginary')
        [<matplotlib.lines.Line2D object at ...>]
        >>> plt.legend()
        <matplotlib.legend.Legend object at ...>
        >>> plt.show()









One-dimensional discrete Fourier Transform for real input (rfft)
-------------------------------------------------------------------------------

.. method:: ctx.rfft(res, data, population, opt)

    Compute the one-dimensional discrete Fourier Transform for real input.

    This function computes the one-dimensional n-point discrete Fourier Transform (DFT) of a real-valued array.
    When the DFT is computed for purely real input, the output is Hermitian-symmetric, i.e. the negative frequency terms are just the complex conjugates of the corresponding positive-frequency terms, and the negative-frequency terms are therefore redundant. This function does not compute the negative frequency terms, and the length of the transformed axis of the output is therefore ``n//2 + 1``.

    When ``A = rfft(a)`` and fs is the sampling frequency, ``A[0]`` contains the zero-frequency term 0*fs, which is real due to Hermitian symmetry.

    If n is even, ``A[-1]`` contains the term representing both positive and negative Nyquist frequency (+fs/2 and -fs/2), and must also be purely real. If n is odd, there is no term at fs/2; ``A[-1]`` contains the largest positive frequency (fs/2*(n-1)/n), and is complex in the general case.

    If the input a contains an imaginary part, it is silently discarded.


    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft



    Return the real part of the complex argument.

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.fft.fft([0, 1, 0, 0])
        array([ 1.+0.j,  0.-1.j, -1.+0.j,  0.+1.j]) # may vary
        >>> np.fft.rfft([0, 1, 0, 0])
        array([ 1.+0.j,  0.-1.j, -1.+0.j]) # may vary









One-dimensional inverse discrete Fourier Transform of rfft (irfft)
-------------------------------------------------------------------------------

.. method:: ctx.irfft(res, data, population, opt)

    Computes the inverse of rfft.

    This function computes the inverse of the one-dimensional n-point discrete Fourier Transform of real input computed by rfft. In other words, ``irfft(rfft(a), len(a)) == a`` to within numerical accuracy. (See Notes below for why ``len(a)`` is necessary here.)

    The input is expected to be in the form returned by rfft, i.e. the real zero-frequency term followed by the complex positive frequency terms in order of increasing frequency. Since the discrete Fourier Transform of real input is Hermitian-symmetric, the negative frequency terms are taken to be the complex conjugates of the corresponding positive frequency terms.

    Returns the real valued n-point inverse discrete Fourier transform of a, where a contains the non-negative frequency terms of a Hermitian-symmetric sequence. n is the length of the result, not the input.

    If you specify an n such that a must be zero-padded or truncated, the extra/removed values will be added/removed at high frequencies. One can thus resample a series to m points via Fourier interpolation by: ``a_resamp = irfft(rfft(a), m)``.

    The correct interpretation of the hermitian input depends on the length of the original data, as given by n. This is because each input shape could correspond to either an odd or even length signal. By default, irfft assumes an even output length which puts the last entry at the Nyquist frequency; aliasing with its symmetric counterpart. By Hermitian symmetry, the value is thus treated as purely real. To avoid losing information, the correct length of the real input **must** be given.

    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy.fft.irfft


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.fft.ifft([1, -1j, -1, 1j])
        array([0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j]) # may vary
        >>> np.fft.irfft([1, -1j, -1])
        array([0.,  1.,  0.,  0.])


    Notice how the last term in the input to the ordinary ifft is the complex conjugate of the second term, and the output has zero imaginary part everywhere. When calling irfft, the negative frequencies are not specified, and the output array is purely real.






FFT of a signal that has Hermitian symmetry, i.e., a real spectrum (hfft)
-------------------------------------------------------------------------------

.. method:: ctx.hfft(res, data, population, opt)

    Compute the FFT of a signal that has Hermitian symmetry, i.e., a real spectrum.

    ``hfft/ihfft`` are a pair analogous to ``rfft/irfft``, but for the opposite case: here the signal has Hermitian symmetry in the time domain and is real in the frequency domain. So here it’s hfft for which you must supply the length of the result if it is to be odd.

    * even: ``ihfft(hfft(a, 2*len(a) - 2)) == a``, within roundoff error,

    * odd: ``ihfft(hfft(a, 2*len(a) - 1)) == a``, within roundoff error.

    The correct interpretation of the hermitian input depends on the length of the original data, as given by n. This is because each input shape could correspond to either an odd or even length signal. By default, ``hfft`` assumes an even output length which puts the last entry at the Nyquist frequency; aliasing with its symmetric counterpart. By Hermitian symmetry, the value is thus treated as purely real. To avoid losing information, the shape of the full signal **must** be given.



    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html#numpy.fft.hfft



    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> signal = np.array([1, 2, 3, 4, 3, 2])
        >>> np.fft.fft(signal)
        array([15.+0.j,  -4.+0.j,   0.+0.j,  -1.-0.j,   0.+0.j,  -4.+0.j]) # may vary
        >>> np.fft.hfft(signal[:4]) # Input first half of signal
        array([15.,  -4.,   0.,  -1.,   0.,  -4.])
        >>> np.fft.hfft(signal, 6)  # Input entire signal and truncate
        array([15.,  -4.,   0.,  -1.,   0.,  -4.])

        >>> signal = np.array([[1, 1.j], [-1.j, 2]])
        >>> np.conj(signal.T) - signal   # check Hermitian symmetry
        array([[ 0.-0.j,  -0.+0.j], # may vary
               [ 0.+0.j,  0.-0.j]])
        >>> freq_spectrum = np.fft.hfft(signal)
        >>> freq_spectrum
        array([[ 1.,  1.],
               [ 2., -2.]])








Inverse FFT of a signal that has Hermitian symmetry (ihfft)
-------------------------------------------------------------------------------

.. method:: ctx.ihfft(res, data, population, opt)

    Compute the inverse FFT of a signal that has Hermitian symmetry.
    ``hfft/ihfft`` are a pair analogous to ``rfft/irfft``, but for the opposite case: here the signal has Hermitian symmetry in the time domain and is real in the frequency domain. So here it’s ``hfft`` for which you must supply the length of the result if it is to be odd:

    * even: ``ihfft(hfft(a, 2*len(a) - 2)) == a``, within roundoff error,

    * odd: ``ihfft(hfft(a, 2*len(a) - 1)) == a``, within roundoff error.



    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.fft.ihfft.html#numpy.fft.ihfft



    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> spectrum = np.array([ 15, -4, 0, -1, 0, -4])
        >>> np.fft.ifft(spectrum)
        array([1.+0.j,  2.+0.j,  3.+0.j,  4.+0.j,  3.+0.j,  2.+0.j]) # may vary
        >>> np.fft.ihfft(spectrum)
        array([ 1.-0.j,  2.-0.j,  3.-0.j,  4.-0.j]) # may vary











Discrete Fourier Transform sample frequencies (fftfreq)
-------------------------------------------------------------------------------

.. method:: ctx.fftfreq(res, data, population, opt)

    Return the Discrete Fourier Transform sample frequencies.

    The returned float array f contains the frequency bin centers in cycles per unit of the sample spacing (with zero at the start). For instance, if the sample spacing is in seconds, then the frequency unit is cycles/second.

    Given a window length n and a sample spacing d:


    .. code-block:: pycon

        f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (d*n)   if n is even
        f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (d*n)   if n is odd


    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.fft.fftfreq.html#numpy.fft.fftfreq



    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5], dtype=float)
        >>> fourier = np.fft.fft(signal)
        >>> n = signal.size
        >>> timestep = 0.1
        >>> freq = np.fft.fftfreq(n, d=timestep)
        >>> freq
        array([ 0.  ,  1.25,  2.5 , ..., -3.75, -2.5 , -1.25])









Discrete Fourier Transform sample frequencies for usage with rfft, irfft (rfftfreq)
---------------------------------------------------------------------------------------

.. method:: ctx.rfftfreq(res, data, population, opt)

    Return the Discrete Fourier Transform sample frequencies (for usage with rfft, irfft).

    The returned float array f contains the frequency bin centers in cycles per unit of the sample spacing (with zero at the start). For instance, if the sample spacing is in seconds, then the frequency unit is cycles/second.

    Given a window length n and a sample spacing d:

    .. code-block:: pycon

        f = [0, 1, ...,     n/2-1,     n/2] / (d*n)   if n is even
        f = [0, 1, ..., (n-1)/2-1, (n-1)/2] / (d*n)   if n is odd

    Unlike ``fftfreq`` (but like ``scipy.fftpack.rfftfreq``) the Nyquist frequency component is considered to be positive.

    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftfreq.html#numpy.fft.rfftfreq


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5, -3, 4], dtype=float)
        >>> fourier = np.fft.rfft(signal)
        >>> n = signal.size
        >>> sample_rate = 100
        >>> freq = np.fft.fftfreq(n, d=1./sample_rate)
        >>> freq
        array([  0.,  10.,  20., ..., -30., -20., -10.])
        >>> freq = np.fft.rfftfreq(n, d=1./sample_rate)
        >>> freq
        array([  0.,  10.,  20.,  30.,  40.,  50.])



