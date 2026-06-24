import numpy as np


def motion_blur_psf(length, angle_deg):
    """
    Create a normalized linear motion-blur PSF.

    Parameters
    ----------
    length : int
        Approximate blur length in pixels.
    angle_deg : float
        Blur direction in degrees. 0° = horizontal, 90° = vertical.

    Returns
    -------
    psf : numpy.ndarray
        Normalized 2D motion-blur kernel.
    """
    size = int(length)
    if size % 2 == 0:
        size += 1

    psf = np.zeros((size, size), dtype=float)

    center = size // 2
    angle_rad = np.deg2rad(angle_deg)

    t = np.linspace(-(length - 1) / 2, (length - 1) / 2, length)

    x = center + t * np.cos(angle_rad)
    y = center + t * np.sin(angle_rad)

    x = np.rint(x).astype(int)
    y = np.rint(y).astype(int)

    valid = (
        (x >= 0) & (x < size) &
        (y >= 0) & (y < size)
    )

    psf[y[valid], x[valid]] = 1.0
    psf /= psf.sum()

    return psf

    