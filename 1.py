import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((1000, 800))
done = False
clock = pygame.time.Clock()
clock_image = pygame.image.load(r"clock.png")
minute_arrow = pygame.image.load(r"minut.png")
sec_arrow = pygame.image.load(r"sec.png")
pos_clock = (100, 100)
pos_minute = (335, 90)
pivot_minute = (350, 350)
offset_minute = pygame.math.Vector2(-1, -120)

pos_sec = (334, 135)
pivot_sec = (350, 350)
offset_sec = pygame.math.Vector2(0, -100)

def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.
    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    time = datetime.datetime.today()
    minute = time.minute
    second = time.second
    angle1 = second * 6 #second angle
    angle2 = (minute * 6) + (second / 10) #minute angle

    new_sec, rect1 = rotate(sec_arrow, angle2, pivot_sec, offset_sec)
    new_minute, rect2 = rotate(minute_arrow, angle1, pivot_minute, offset_minute)

    screen.fill((0, 0, 0))
    screen.blit(clock_image, pos_clock)
    screen.blit(new_sec, rect1)
    screen.blit(new_minute, rect2)

    pygame.display.flip()
    clock.tick(60)