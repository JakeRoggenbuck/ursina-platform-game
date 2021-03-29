import random
import ursina as urs
from ursina.prefabs.first_person_controller import FirstPersonController


app = urs.Ursina()


class Platform(urs.Entity):
    def __init__(self, x=0, y=2, z=0):
        super().__init__(
            parent=urs.scene,
            model='cube',
            texture='white_cube',
            collider='box',
            color=urs.color.hex("#21a6f6"),
            scale=(20, 1, 20),
            position=(x, y, z),
        )


class Platforms:
    def __init__(self):
        self.platforms = []
        self.x, self.y, self.z = 0, 0, 0
        self.x_delta, self.z_delta = 0, 0

    def add(self):
        platform = Platform(self.x, self.y, self.z)

        # Changes the platforms location
        self.x = random.randint(-10 - self.x_delta, 10 + self.x_delta)
        self.y -= 10
        self.z += 50 + self.z_delta

        self.platforms.append(platform)
        # How much extra challenge is added, [0, 0, ..., 0, 1]
        # There is a low change the delta increases
        self.x_delta += random.choice([*[0] * 9, 1])
        self.z_delta += random.choice([*[0] * 9, 1])


if __name__ == "__main__":
    sky = urs.Sky()
    urs.scene.fog_density = 0.01

    platforms = Platforms()
    # Creates all the platforms
    [platforms.add() for _ in range(100)]
    # Colors the last one red
    platforms.platforms[-1].color = urs.color.hex("#cb2a2a")

    player = FirstPersonController()
    player.speed = 40

    app.run()
