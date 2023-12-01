import arcade

class Forme:
    def __init__(self, x, y, change_x, change_y, color):
        # Initialise les attributs communs à toutes les formes
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def update(self, width, height):
        # Met à jour la position de la forme en fonction de sa vitesse
        self.x += self.change_x
        self.y += self.change_y

        # Valide que la forme ne sorte pas de l'écran
        if self.x < 0 or self.x > width:
            self.change_x *= -1
        if self.y < 0 or self.y > height:
            self.change_y *= -1



class Balle(Forme):
    def __init__(self, x, y, change_x, change_y, rayon, color):
        # Initialise les attributs spécifiques à la balle
        super().__init__(x, y, change_x, change_y, color)
        self.rayon = rayon

    def draw(self):
        # Dessine la balle sur l'écran
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class Rectangle(Forme):
    def __init__(self, x, y, change_x, change_y, width, height, color):
        # Initialise les attributs spécifiques au rectangle
        super().__init__(x, y, change_x, change_y, color)
        self.width = width
        self.height = height

    def draw(self):
        # Dessine le rectangle sur l'écran
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Configure la couleur de fond de la fenêtre
        arcade.set_background_color(arcade.color.WHITE)

        # Liste pour contenir les formes (balles et rectangles)
        self.formes = []

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            # Ajoute une balle à l'endroit du clic
            self.formes.append(Balle(x, y, 2, 2, 20, arcade.color.RED))
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            # Ajoute un rectangle à l'endroit du clic
            self.formes.append(Rectangle(x, y, 3, 3, 40, 30, arcade.color.GREEN))

    def on_draw(self):
        # Débute le rendu
        arcade.start_render()

        # Dessine toutes les formes
        for forme in self.formes:
            forme.draw()

    def on_update(self, delta_time):
        # Met à jour la position de toutes les formes
        for forme in self.formes:
            forme.update(self.width, self.height)

def main():
    # Définis les dimensions de la fenêtre et le titre
    width = 800
    height = 600
    title = "Ajout de Balles et Rectangles"
    # Crée une instance de la classe MyGame
    window = MyGame(width, height, title)
    # Démarre la boucle de jeu d'Arcade
    arcade.run()

if __name__ == "__main__":
    main()
