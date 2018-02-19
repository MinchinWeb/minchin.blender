import bpy

from .geometry import north, south, east, west, add_z, poly_area2D
from .measurements import ft


class UnknownCommandError(KeyError):
    pass


def build_room(room_name, edges, floor_height):
    """
    Generate a mesh corresponding to the room's footprint.

    *edges* is assumed to be a series of tuples, listing a direction and
    distanace. Alternate valid "directions" include *start*, paired with a 2D
    point, and *close*, to finish the shape.ValueError
    """
    current_location = None
    locations = []

    def set_location(_, location):
        # will drop 3rd dimension
        if len(location) == 2:
            return location
        else:
            return (location[0], location[1])

    def pass_function(_, _2):
        return None
    
    command_options = {
        "start": set_location,
        "north": north,
        "south": south,
        "east": east,
        "west": west,
        "close": pass_function,
    }

    for command, distance in edges:
        if command in command_options.keys():
            new_location = command_options[command](current_location, distance)
            if new_location:
                current_location = new_location
                locations.append(add_z(current_location, z=floor_height))
        else:
            raise UnknownCommandError(command)
    
    faces = [[i for i in range(len(locations))]]

    mesh_data = bpy.data.meshes.new("cube_mesh_data")
    mesh_data.from_pydata(locations, [], faces)
    mesh_data.update()

    obj = bpy.data.objects.new("{} Mesh".format(room_name), mesh_data)

    scene = bpy.context.scene
    scene.objects.link(obj)

    # calculate area
    locations_2D = [[i[0], i[1]] for i in locations]
    area = poly_area2D(locations_2D)
    area = area / (ft**2)

    to_return= {
        "name": room_name,
        "verts": locations,
        "faces": faces,
        "mesh": mesh_data,
        "obj": obj,
        "area": area,
    }

    return to_return


