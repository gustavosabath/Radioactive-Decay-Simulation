import pyray as ray
import visual_processing as vp

BLUE = ray.Color(0x1e, 0x88, 0xe5, 0xff)
GRAY = ray.Color(0xc2, 0xcb, 0xd1, 128)
MAGENTA = ray.Color(0xd8, 0x1b, 0x60, 0xff)
BACKGROUND = ray.Color(0xf2, 0xf4, 0xf7, 0xff)

framerate = 60 # 1second
ray.set_config_flags(ray.ConfigFlags.FLAG_MSAA_4X_HINT)
ray.init_window(0, 0, "Radioactive Decay Simulation")
ray.set_target_fps(framerate)
InterFont = ray.load_font("assets/Inter.ttf")
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
canRun = False

title = "Carbon-14"
titleVector = ray.measure_text_ex(InterFont, title, 35, 0)

dt = 10
timeElapsed = 0.0

while not ray.window_should_close():
    frametime = ray.get_frame_time()
    if ray.is_key_pressed(ray.KeyboardKey.KEY_SPACE):
        canRun = True
    if ray.is_key_pressed(ray.KeyboardKey.KEY_LEFT_SHIFT) and not canRun:
        dt += 10
    if ray.is_key_pressed(ray.KeyboardKey.KEY_LEFT_CONTROL) and not canRun:
        dt -= 10
        dt = max(10, dt)
    if ray.is_key_down(ray.KeyboardKey.KEY_X) and not canRun:
        dt += 100*frametime
    if ray.is_key_down(ray.KeyboardKey.KEY_Z) and not canRun:
        dt -= 100*frametime
        dt = max(10, dt)
    if canRun:
        vp.simulate(balls, frametime, dt)
    
    ray.begin_drawing()
    ray.clear_background(BACKGROUND)
    # ray.draw_rectangle_lines(50, 50, width-100, height-100, ray.BLACK)
    ray.draw_text_ex(InterFont, title, ray.Vector2((width - titleVector.x)/2, 30-titleVector.y/2), 35, 0, ray.BLACK)
    ray.draw_text_ex(InterFont, f"{ray.get_fps()} FPS", ray.Vector2(int(0.94*width), int(0.02*height)), 20, 0, ray.BLACK)

    for ballX, ballY, alive in balls:
        ray.draw_rectangle(ballX-ballRadius-(ballBoxFillSize//2), ballY-ballRadius-(ballBoxFillSize//2), 2*ballRadius+ballBoxFillSize, 2*ballRadius+ballBoxFillSize, GRAY)
        ray.draw_rectangle_lines_ex(ray.Rectangle(ballX - ballRadius - (ballBoxFillSize // 2), ballY - ballRadius - (ballBoxFillSize // 2), 2 * ballRadius + ballBoxFillSize, 2 * ballRadius + ballBoxFillSize), 3 if alive else 1, BLUE if alive else MAGENTA)
        ray.draw_circle(ballX, ballY, ballRadius if alive else 7, BLUE if alive else MAGENTA)
    
    remaingNuclei = sum([1 if nucleus[2] else 0 for nucleus in balls])
    decayedNuclei = sum([1 if not nucleus[2] else 0 for nucleus in balls])
    legend = f"Time scale: {dt:.0f} {"years"}/second | Remaining: {remaingNuclei} | Decayed: {decayedNuclei}"
    legendVector = ray.measure_text_ex(InterFont, legend, 25, 0)
    ray.draw_text_ex(InterFont, legend, ray.Vector2((width - legendVector.x)/2, height-30-(legendVector.y/2)), 25, 0, ray.BLACK)
    ray.draw_text_ex(InterFont, f"Time elapsed: {timeElapsed:.2f} s", ray.Vector2(56, int(0.02*height)), 25, 0, ray.BLACK)
    ray.end_drawing()
    if remaingNuclei == 0: canRun = False
    timeElapsed += ray.get_frame_time() if canRun else 0
ray.unload_font(InterFont)
ray.close_window()