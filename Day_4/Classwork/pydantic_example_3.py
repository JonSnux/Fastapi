from pydantic import BaseModel, ConfigDict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Point1D:
    def __init__(self, x):
        self.x = x


class PointSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    x: int
    y: int | None = None
    z: int | None = None


point = Point(x=10, y=25)
schema = PointSchema.model_validate(point)
print(f'{schema = }')
point_json = schema.model_dump_json(indent=4)
print(point_json)

point_3d = Point3D(x=1, y=2, z=3)
schema = PointSchema.model_validate(point_3d)
point_json = schema.model_dump_json(indent=4)
print(point_json)


point_1d = Point1D(x=100)
try:
    schema_1d = PointSchema.model_validate(point_1d)
    point_json = schema_1d.model_dump_json(indent=4)
    print(point_json)
except Exception as e:
    print(f"Validation error: {e}")


