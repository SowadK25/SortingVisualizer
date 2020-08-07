import pygame
import random
from Buttons import Button

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
PURPLE = (104, 21, 166)
RED = (255, 0, 0)
DARK_GREEN = (29, 173, 10)
LIGHT_GREEN = (57, 229, 34)

heights = []


def generate_array(size, array):
    array.clear()
    for i in range(size):
        array.append(random.randrange(50, 500))


def array_bars(array, window, color):
    for i in range(len(array)):
        pygame.draw.rect(window, color, (15 + 15*i, 0, 10, array[i]))


def bubble_sort_visual(array, window, delay):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                pygame.draw.rect(screen, RED, (15 + 15*j, 0, 10, temp))
                pygame.display.update()

            window.fill(GREEN)
            array_bars(heights, screen, WHITE)
            pygame.time.delay(delay)
            pygame.display.update()

        if i == len(array) - 1:
            array_bars(heights, screen, PURPLE)
            pygame.display.update()


def selection_sort_visual(array, window, delay):
    for i in range(len(array)):
        smallest = i
        for j in range(i+1, len(array)):
            if array[smallest] > array[j]:
                smallest = j

            window.fill(GREEN)
            array_bars(heights, screen, WHITE)
            pygame.time.delay(delay)
            pygame.display.update()

        array[i], array[smallest] = array[smallest], array[i]

        if i == len(array) - 1:
            array_bars(heights, screen, PURPLE)
            pygame.display.update()


def insertion_sort_visual(array, window, delay):
    for i in range(len(array)):
        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            window.fill(GREEN)
            array_bars(heights, screen, WHITE)
            pygame.time.delay(delay)
            pygame.display.update()
        array[j + 1] = key

        if i == len(array) - 1:
            array_bars(heights, screen, PURPLE)
            pygame.display.update()


pygame.init()

screen_size = (1000, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("A sorting visualizer")
screen.fill(GREEN)

new_array_button = Button("New Array", (100, 550), DARK_GREEN, WHITE)
bubble_sort_button = Button("Bubble Sort", (275, 550), DARK_GREEN, WHITE)
selection_sort_button = Button("Selection sort", (450, 550), DARK_GREEN, WHITE)
insertion_sort_button = Button("Insertion sort", (625, 550), DARK_GREEN, WHITE)
quit_button = Button("X", (950, 550), RED, WHITE, (40, 40))

buttons = [new_array_button, bubble_sort_button, selection_sort_button, insertion_sort_button, quit_button]

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if new_array_button.rect.collidepoint(position):
                screen.fill(GREEN)
                generate_array(65, heights)
                array_bars(heights, screen, WHITE)
                pygame.display.update()

            if quit_button.rect.collidepoint(position):
                running = False

            if bubble_sort_button.rect.collidepoint(position):
                bubble_sort_visual(heights, screen, 8)

            if selection_sort_button.rect.collidepoint(position):
                selection_sort_visual(heights, screen, 2)

            if insertion_sort_button.rect.collidepoint(position):
                insertion_sort_visual(heights, screen, 8)

    for button in buttons:
        button.draw()
    pygame.display.update()

