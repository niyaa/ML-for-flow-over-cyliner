import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import meshio
from glob import glob
import numpy as np
import os
from scipy.interpolate import griddata

starting_path = os.getcwd()

FilePath = 'D:\OneDrive - Politechnika Warszawska\cylinder_data'

os.chdir(FilePath)

ReList = glob("*/");

cwd = os.getcwd()

for i in ReList[0:1]:
    os.chdir(cwd)
    print(i)
    os.chdir(i)

    Re = int(i.split(".")[0])

    vtu_file_List = glob("*.vtu")

    for j in vtu_file_List[-2:-1]:
        mesh = meshio.read(j)

        u = mesh.point_data.__getitem__("u")
        v = mesh.point_data.__getitem__("v")

        a=mesh.points
        X = a[:, 0]
        Y = a[:, 1]

        c = np.column_stack((X, Y, u))
        c = c[ c[:,0].argsort()]    

  

        grid_x, grid_y = np.mgrid[min(X):max(X):0.01, min(Y):max(Y):0.01]
        grid_z2 = griddata(c[:,0:2], c[:,2],  (grid_x, grid_y), method='cubic')
        plt.imshow(grid_z2.T, extent=(0,1,0,1), origin='lower')


        #X, Y = np.meshgrid(X, Y)
        #U, V = np.meshgrid(u, v)


        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        # Plot the surface.
        surf = ax.plot_surface(X, Y, u, cmap=cm.coolwarm,
                            linewidth=0, antialiased=False)

        # Customize the z axis.
        ax.set_zlim(-1.01, 1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        # A StrMethodFormatter is used automatically
        ax.zaxis.set_major_formatter('{x:.02f}')

        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.show()


os.chdir(starting_path)




