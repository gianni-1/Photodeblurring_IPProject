import numpy as np


def apply_motion_blur(image, psf):
    """
    Apply 2D motion blur to a single image channel using FFT convolution
    with reflective padding.

    Parameters
    ----------
    image : numpy.ndarray
        2D image channel.
    psf : numpy.ndarray
        Normalized 2D motion-blur kernel.

    Returns
    -------
    blurred : numpy.ndarray
        Blurred image channel with the original shape.
    """
    pad_y = psf.shape[0] // 2
    pad_x = psf.shape[1] // 2

    padded_image = np.pad(
        image,
        pad_width=((pad_y, pad_y), (pad_x, pad_x)),
        mode="reflect"
    )

    H = np.fft.fft2(
        np.fft.ifftshift(psf),
        s=padded_image.shape
    )

    F = np.fft.fft2(padded_image)

    blurred_padded = np.real(np.fft.ifft2(H * F))

    return blurred_padded[
        pad_y:pad_y + image.shape[0],
        pad_x:pad_x + image.shape[1]
    ]