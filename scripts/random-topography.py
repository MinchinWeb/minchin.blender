import bpy

import numpy as np
from scipy.spatial import Delaunay


MAX_XY = 1
MAX_Z = 0.2
POINT_COUNT = 100 * MAX_XY**2
SIDE_SPLITS = 8 * MAX_XY - 1

corners = []
for x in range(SIDE_SPLITS):
    corners.append([0, x*MAX_XY/SIDE_SPLITS])
    corners.append([MAX_XY, x*MAX_XY/SIDE_SPLITS])
    corners.append([x*MAX_XY/SIDE_SPLITS, 0])
    corners.append([x*MAX_XY/SIDE_SPLITS, MAX_XY])
corners.append([MAX_XY, MAX_XY])

points = MAX_XY * np.random.random_sample((POINT_COUNT, 2))
points = np.concatenate((corners, points))
tri = Delaunay(points)

verts = [[point[0], point[1], MAX_Z * np.random.random()] for point in points]
faces = [[face[0], face[1], face[2]] for face in tri.simplices]

mesh_data = bpy.data.meshes.new("cube_mesh_data")
mesh_data.from_pydata(verts, [], faces)
mesh_data.update()

obj = bpy.data.objects.new("Topography Mesh", mesh_data)

scene = bpy.context.scene
scene.objects.link(obj)
obj.select = True
# scene.objects.active = obj  # make the selection effective
