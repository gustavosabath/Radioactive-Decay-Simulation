import pyray as ray

BLUE = ray.Color(0x4a, 0x91, 0xc7, 0xff)
GRAY = ray.Color(0xc2, 0xcb, 0xd1, 128)

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

while not ray.window_should_close():
    ray.begin_drawing()
    ray.clear_background(ray.WHITE)
    # ray.draw_rectangle_lines(50, 50, width-100, height-100, ray.BLACK)
    for i in range(nBallsline):
        ballX = int((unitOfWidth*i)+78)
        for j in range(nBallscolumn):
            ballY = int((unitOfHeight*j)+85)
            ray.draw_rectangle(ballX-ballRadius-(ballBoxFillSize//2), ballY-ballRadius-(ballBoxFillSize//2), 2*ballRadius+ballBoxFillSize, 2*ballRadius+ballBoxFillSize, GRAY)
            ray.draw_rectangle_lines(ballX-ballRadius-(ballBoxFillSize//2), ballY-ballRadius-(ballBoxFillSize//2), 2*ballRadius+ballBoxFillSize, 2*ballRadius+ballBoxFillSize, BLUE)
            ray.draw_circle(ballX, ballY, ballRadius, BLUE)
    ray.end_drawing()
ray.close_window()