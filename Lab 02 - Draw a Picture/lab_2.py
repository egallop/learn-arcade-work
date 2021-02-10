import arcade
arcade.open_window(800, 600, "Drawing Farm full of white squirrels in a blizzard")

arcade.set_background_color(arcade.csscolor.ORCHID)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.csscolor.DARK_KHAKI)
# head
arcade.draw_ellipse_filled(400, 400, 175, 150, arcade.csscolor.GREENYELLOW)
# body
arcade.draw_circle_filled(400, 250, 125, arcade.csscolor.GREENYELLOW)
# arm outlines
arcade.draw_ellipse_outline(350, 275, 40, 100, arcade.csscolor.BLACK,1, -45)

arcade.draw_ellipse_outline(450, 275, 40, 100, arcade.csscolor.BLACK,1,45)
# arm covers
arcade.draw_circle_filled(325, 290, 30, arcade.csscolor.GREENYELLOW)

arcade.draw_circle_filled(475, 290, 30, arcade.csscolor.GREENYELLOW)
# under eyes
arcade.draw_circle_filled(425, 410, 15, arcade.csscolor.LIGHT_PINK)

arcade.draw_circle_filled(375, 410, 15, arcade.csscolor.LIGHT_PINK)
# eyes
arcade.draw_circle_filled(383, 415, 15, arcade.csscolor.BLACK)

arcade.draw_circle_filled(418, 415, 15, arcade.csscolor.BLACK)
# ears
arcade.draw_triangle_filled(427, 425, 475, 425, 475, 525, arcade.csscolor.GREENYELLOW)

arcade.draw_triangle_filled(327, 425, 375, 430, 325, 525, arcade.csscolor.GREENYELLOW)
# ear insides
arcade.draw_arc_filled(340, 455, 20, 60, arcade.csscolor.ORANGE_RED, 0, 190)

arcade.draw_arc_filled(460, 455, 20, 60, arcade.csscolor.ORANGE_RED, 0, 190)
# feet
arcade.draw_circle_filled(325, 175, 60, arcade.csscolor.GREENYELLOW)

arcade.draw_circle_filled(460, 175, 60, arcade.csscolor.GREENYELLOW)
# foot pads
arcade.draw_circle_filled(325, 175, 40, arcade.csscolor.LIME_GREEN)

arcade.draw_circle_filled(460, 175, 40, arcade.csscolor.LIME_GREEN)
# mouth
arcade.draw_arc_filled(400, 380, 50, -75, arcade.csscolor.MEDIUM_VIOLET_RED, 0, 180)

arcade.finish_render()
arcade.run()