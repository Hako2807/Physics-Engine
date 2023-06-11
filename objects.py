class Physics:
    def __init__(self) -> None:
        pass


class Vector3:
    def __init__(self, x = 0, y = 0, z = 0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.value = [x, y, z]

class Vector:
    def add(u: Vector3, v: Vector3) -> Vector3:
        return Vector3(u.x +v.x, u.y +v.y, u.z + v.z)
    
    def scale(k: float, u: Vector3) -> Vector3:
        return Vector3(k * u.x, k * u.y, k * u.z)

class Object(Physics):
    def __init__(self, m) -> None:
        super().__init__()
        self.m = m
        self.pos = Vector3()
        self.vel = Vector3()
        self.acc = Vector3()
    
    def add_force(self, f: Vector3) -> None:
        self.acc = Vector.add(self.acc, Vector.scale(1/self.m, f)) 

a = Object(10)
print(a.acc.value)
force = Vector3(0, -9.81, 0)
a.add_force(force)
print(a.acc.value)