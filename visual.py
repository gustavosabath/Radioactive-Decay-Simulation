import pyray as ray
import visual_processing as vp

BLUE = ray.Color(0x4a, 0x91, 0xc7, 0xff)
GRAY = ray.Color(0xc2, 0xcb, 0xd1, 128)
RED = ray.Color(0xab, 0x32, 0x3a, 0xff)

framerate = 60 # 1second
ray.init_window(0, 0, "Radioactive Decay Simulation")
ray.set_target_fps(framerate)
width = ray.get_screen_width()
height = ray.get_screen_height()

nBallsline = 30
nBallscolumn = 15

ballRadius = 10
ballBoxFillSize = 25

usefulWidth = width-100
usefulHeight = height-100
unitOfWidth = usefulWidth/nBallsline
unitOfHeight = usefulHeight/nBallscolumn
balls = [[int((unitOfWidth*i)+78), int((unitOfHeight*j)+85), True] for i in range(nBallsline) for j in range(nBallscolumn)]
canStart = False

while not ray.window_should_close():
    frameCount = 0
    if ray.is_key_pressed(ray.KeyboardKey.KEY_SPACE):
        canStart = True
    if (frameCount % framerate == 0) and canStart:
        vp.simulate(balls)
    
    ray.begin_drawing()
    ray.clear_background(ray.WHITE)
    # ray.draw_rectangle_lines(50, 50, width-100, height-100, ray.BLACK)
    for ballX, ballY, alive in balls:
        ray.draw_rectangle(ballX-ballRadius-(ballBoxFillSize//2), ballY-ballRadius-(ballBoxFillSize//2), 2*ballRadius+ballBoxFillSize, 2*ballRadius+ballBoxFillSize, GRAY)
        ray.draw_rectangle_lines(ballX-ballRadius-(ballBoxFillSize//2), ballY-ballRadius-(ballBoxFillSize//2), 2*ballRadius+ballBoxFillSize, 2*ballRadius+ballBoxFillSize, BLUE if alive else RED)
        ray.draw_circle(ballX, ballY, ballRadius, BLUE if alive else RED)
    ray.end_drawing()
    frameCount += 1
ray.close_window()