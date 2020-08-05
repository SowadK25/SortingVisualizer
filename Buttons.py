# This is not needed for the sorting algorithm visuals, but used for initiating actions with buttons.
import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREEN = (29, 173, 10)
LIGHT_GREEN = (57, 229, 34)
small = pygame.font.SysFont("TimesNewRoman", 25)

height = 675
width = 675

screen = pygame.display.set_mode((height, width))  # screen display size
screen_rect = screen.get_rect()


class Button:
    """Class for game buttons"""
    def __init__(self, text, pos, color1, color2, size=(150, 40)):  # Initialize class
        super().__init__()

        self.color = color1  # Main button color
        self.color1 = color1  # Color changes if mouse is over button
        self.color2 = color2  # Text color
        self.size = size  # Button size
        self.text = text  # Button text
        self.font = pygame.font.SysFont("TimesNewRoman", 25)  # Font to be used
        self.textbox = self.font.render(self.text, 3, self.color2)  # Rendering font to put in button
        self.textrect = self.textbox.get_rect(center=[i/2 for i in self.size])  # Create rect (button)
        self.surface = pygame.surface.Surface(self.size)  # Create surface on rect
        self.rect = self.surface.get_rect(center=pos)  # Center the surface object

    def draw(self):
        """Draw mouse"""
        self.mouse_hover()  # Call mouse_hit function
        self.surface.fill(self.color1)  # Fill button with color
        self.surface.blit(self.textbox, self.textrect)  # Display button on screen
        screen.blit(self.surface, self.rect)

    def mouse_hover(self):
        """Checks if mouse is over button"""
        self.color1 = self.color  # Color changes
        position = pygame.mouse.get_pos()  # Get mouse position
        if self.rect.collidepoint(position):  # If the mouse is inside the button rect
            self.color1 = LIGHT_GREEN  # Change color to light green

