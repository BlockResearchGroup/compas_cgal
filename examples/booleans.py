import numpy as np

from compas.geometry import Point
from compas.geometry import Box
from compas.geometry import Sphere
from compas.datastructures import Mesh
from compas.datastructures import mesh_subdivide_quad

from compas_viewers.multimeshviewer import MultiMeshViewer
from compas_viewers.multimeshviewer import MeshObject

from compas_cgal.booleans import boolean_union
from compas_cgal.meshing import remesh

# ==============================================================================
# Make a box and a sphere
# ==============================================================================

box = Box.from_width_height_depth(2, 2, 2)
box = Mesh.from_shape(box)
box.quads_to_triangles()

A = box.to_vertices_and_faces()

sphere = Sphere(Point(1, 1, 1), 1)
sphere = Mesh.from_shape(sphere, u=30, v=30)
sphere.quads_to_triangles()

B = sphere.to_vertices_and_faces()

# ==============================================================================
# Remesh the sphere
# ==============================================================================

B = remesh(B, 0.3, 100)

# ==============================================================================
# Compute the boolean mesh
# ==============================================================================

V, F = boolean_union(A, B)

mesh = Mesh.from_vertices_and_faces(V, F)

# ==============================================================================
# Visualize
# ==============================================================================

meshes = []
meshes.append(MeshObject(mesh, color='#cccccc'))

viewer = MultiMeshViewer()
viewer.meshes = meshes

viewer.show()
