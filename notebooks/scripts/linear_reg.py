"""
Linear regression plot from scratch, with numpy and scipy
Inspired by Erik Bern's blog post on uncertainty estimates:
  https://erikbern.com/2018/10/08/the-hackers-guide-to-uncertainty-estimates.html

Requires NumPy and SciPy installed
"""

# Import Modules
import random
import numpy as np
import scipy.optimize as opt


def linear_eq(x, m, c):
    """Function (or a model) to do linear equation; y = mx + c
    Also written as kx + m in some texts. Confusing, I know

    Arg:
      x: x value
      m: the slope
      c: y-intercept

    Returns y
    """
    return m * x + c


def l2_loss(tup, x, y):
    """L2 Loss function a.k.a least square errors (LS)

    Arg:
      tup: Using value from x0 (initial guess), see opt.minimize() block below.
           Unpacks into m and c
      x: The x-values
      y: The v-values
    """
    m, c = tup
    delta = linear_eq(x, m, c) - y  # Get the difference between actual and predicted
    return np.dot(delta, delta)     # Square that difference


def confidence_interval(ax, x, y, n=250, conf_curve=False, conf_band=True):
    """Plot confidence interval using bootstrapping approach

    Arg:
      ax: The Axes object to draw on
      x: The x-values (array)
      y: The y-values (array)
      n: The number of times to perform the bootstrap, default of 250 (arbitrarily chosen)
      conf_curve: Draw confidence interval curve (default: False)
      conf_band: Draw confidence interval band (default: True)
    """
    xys = list(zip(x, y))
    curves = []

    # Calculate confidence interval by bootstrapping
    # The opt.minimize().x access the x portion of the returned value: an array of m and c in this case
    for i in range(n):
        bootstrap = [random.choice(xys) for _ in xys]
        bootstrap_x = np.array([x for x, y in bootstrap])
        bootstrap_y = np.array([y for x, y in bootstrap])
        m_hat, c_hat = opt.minimize(l2_loss, x0=(0, 0), args=(bootstrap_x, bootstrap_y)).x
        curves.append(linear_eq(x, m_hat, c_hat))

    # Plot individual confidence interval lines
    if conf_curve:
        for curve in curves:
            ax.plot(x, curve, alpha=0.1, linewidth=2, color="lightsteelblue")

    # Plot confidence interval band (97.5 - 2.5 = 95%).
    # Sort them all with np.sort() so ax.fill_between() can properly work
    if conf_band:
        lo, hi = np.percentile(curves, (2.5, 97.5), axis=0)
        ax.fill_between(x=np.sort(x), y1=np.sort(lo), y2=np.sort(hi), color="lightsteelblue", alpha=0.25)


def lin_reg_plot(ax, data, x_var, y_var, n=250, conf_curve=False, conf_band=True):
    """Linear regression plot, a wrapper function of all of the above
    By convention, the term "hat" refers to "estimates".

    Arg:
      ax: The Axes object to draw plot on
      data: Pandas DataFrame, where variables have their own columns (wide-format)
      x_var: Variable on the x-axis
      y_var: Variable on the y-axis
      n: Number of times to perform the bootstrap, default of 250
      conf_curve: Draw confidence curves?
      conf_band: Draw confidence band?
    """
    x = data[x_var].to_numpy()
    y = data[y_var].to_numpy()

    m_hat, c_hat = opt.minimize(l2_loss, x0=(0,0), args=(x, y)).x
    ax.scatter(x, y, alpha=0.5, s=50)
    ax.plot(x, linear_eq(x, m_hat, c_hat), color="cornflowerblue", linewidth=2.5, alpha=0.5)
    confidence_interval(ax, x=x, y=y, n=n, conf_curve=conf_curve, conf_band=conf_band)
