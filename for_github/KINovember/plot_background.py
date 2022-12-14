import matplotlib.pyplot as plt
import numpy as np

#  Hilfsfunktion plot_background_image
#  Wertet die Funktion f auf einem regelmäßigen Gitter aus und plottet sie.
#
#  f:          Funktion, mit deren Hilfe Z-Werte berechnet werden können
#              Bekommt als Übergabeparameter ein np.array der Größe (xres*yres,2) und
#              muss eines der Größe (xres*yres,1) zurückgeben
#  resolution: Anzahl der Pixel in x- und y-Richtung
#  extent:     Tupel: (left, right, bottom, top) legt den Wertebereich fest
def plot_background_image(f, xres=200, yres=200, extent = (-1.2,2.0,-1.2,2.0)):
    left,right,bottom,top = extent
    x_values=np.linspace(left,right,xres)
    y_values=np.linspace(bottom,top,yres)
    x1,y1=np.meshgrid(x_values,y_values)
    pixels=xres*yres
    x1 = x1.reshape(pixels,1)
    y1 = y1.reshape(pixels,1)
    X_grid=np.column_stack((x1, y1))
    Z=f(X_grid).reshape(xres,yres)
    plt.imshow(Z,origin="lower",extent=extent, cmap="Wistia")
    plt.show()
   