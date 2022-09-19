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

for i in ReList:
    os.chdir(cwd)
    print(i)
    os.chdir(i)

    Re = int(i.split(".")[0])

    vtu_file_List = glob("*.vtu")

    for j in vtu_file_List:
        print(j)
        mesh = meshio.read(j)

        u = mesh.point_data.__getitem__("u")
        v = mesh.point_data.__getitem__("v")



        fileIndex = int(j.split(".")[0].split("_")[1]) 


        a=mesh.points
        X = a[:, 0]
        Y = a[:, 1]

        c = np.column_stack((X, Y, u, v))
        c = c[ c[:,0].argsort()]    

  

        grid_x, grid_y = np.mgrid[min(X):max(X):0.01, min(Y):max(Y):0.01]
        grid_u = griddata(c[:,0:2], c[:,2],  (grid_x, grid_y),  method='linear')

        grid_v = griddata(c[:,0:2], c[:,3],  (grid_x, grid_y),  method='linear')

        np.savetxt( "u-Re-"+str(Re)+"-fileIndex-"+str(fileIndex), grid_u.T)      
        np.savetxt( "v-Re-"+str(Re)+"-fileIndex-"+str(fileIndex), grid_v.T)    


os.chdir(starting_path)
 
    

