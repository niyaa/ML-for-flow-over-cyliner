import meshio
from glob import glob
import numpy as np
import os

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
        mesh = meshio.read(j)

        u = mesh.point_data.__getitem__("u")
        v = mesh.point_data.__getitem__("v")

        uv = np.column_stack( (u,v ) )

        del u, v

        fileIndex = int(j.split(".")[0].split("_")[1]) 

        np.savetxt( "ml-Re-"+str(Re)+"-fileIndex-"+str(fileIndex), uv)       

 
    

