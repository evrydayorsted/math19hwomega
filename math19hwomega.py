from typing_extensions import runtime
from manim import *

class Intro(ThreeDScene):

    def construct(self):
        title = Title("Where does the critical point classification formula come from?")
        formula = Tex(r"$\ d_1 = f_{xx}(a, b)$", font_size = 40)
        formula2 = Tex(r"$\ d_2 = f_{xx} (a, b) f_{yy} (a, b)$", font_size = 40)
        formula3 = Tex(r"$\ {f_{xy} (a, b)} ^ 2$", font_size = 40)
        
        formula2.to_edge(RIGHT)
        formula.next_to(formula2, UP)
        formula3.next_to(formula2, DOWN)
        
        
        
        axes = ThreeDAxes(x_range=[-4,4], x_length=8)

        surfaceMin = Surface(
                lambda u, v: np.array([
                    u, v, u**2 + v**2
                ]),
                u_range=[-2, 2],
                v_range=[-2, 2], resolution = (10, 32)
            )
        surfaceMax = Surface(
                lambda u, v: np.array([
                    u, v, - u**2 - v**2
                ]),
                u_range=[-2, 2],
                v_range=[-2, 2],
                resolution = (10, 32), checkerboard_colors = [GREEN_C, GREEN_E]
            )
        surfaceSaddle = Surface(
                lambda u, v: np.array([
                    u, v, u**2 - v**2
                ]), u_range=[-2, 2], v_range= [-2, 2], resolution = (10, 32), checkerboard_colors = [MAROON_C, MAROON_E])
            
        self.set_camera_orientation(theta=-70 * DEGREES, phi=75 * DEGREES)


        # surfaceMin.width = 2
        # surfaceMin.width = 2
        # surfaceMax.width = 2
        # surfaceMax.width = 2
        # surfaceSaddle.width = 2
        # surfaceSaddle.width = 2
 
        
        question = Tex("Max, Min, Saddle???", color = BLUE)

        question.move_to(LEFT * 4)
        self.add_fixed_in_frame_mobjects(title, formula2, formula, formula3, question)
        self.remove(title, question, formula2, formula, formula3)
        self.play(FadeIn(title))
        self.begin_ambient_camera_rotation(rate = 0.2)
        self.play(Create(axes), FadeIn(formula2, formula, formula3))
        self.wait(1)
        self.play(FadeIn(surfaceSaddle))
        self.play(Transform(surfaceSaddle, surfaceMax), run_time = 5)
        self.play(Write(question))
        self.wait(1)
        self.play(Transform(surfaceMax, surfaceMin), run_time = 5)
        self.wait(1)

class howToAnswer(ThreeDScene):
    def construct(self):
        explanation = Tex("Hello\nWorld", font_size = 10)
        self.play(Write(explanation))


# class omega(ThreeDScene):
    
    
    

#     def construct(self):
#         Intro.construct()
#         howToAnswer.construct()
