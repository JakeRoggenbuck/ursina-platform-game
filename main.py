import random
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()


class Platform(Entity):
    def __init__(self, x=0, y=2, z=0):
        self.z = z
        self.y = y
        super().__init__(
            parent=scene,
            model='cube',
            collider='box',
            color=color.hex("#21a6f6"),
            scale=(20, 1, 20),
            position=(x, y, z),
        )


class Platforms:
    def __init__(self):
        self.platforms = []
        self.x = 0
        self.y = 0
        self.z = 0

    def add(self):
        platform = Platform(self.x, self.y, self.z)
        self.x = random.randint(-10, 10)
        self.y -= 10
        self.z += 50
        self.platforms.append(platform)


if __name__ == "__main__":
    plat = Platforms()
    [plat.add() for _ in range(100)]

    player = FirstPersonController()
    player.speed = 40

    app.run()
