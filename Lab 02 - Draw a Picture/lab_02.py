#homework drawing
import arcade
arcade.open_window(600, 600, "Drawing smile")


arcade.set_background_color(arcade.csscolor.HONEYDEW)

arcade.start_render()

arcade.draw_circle_filled(300, 300, 200, arcade.csscolor.ORANGE)
arcade.draw_arc_filled(300, 300, 220, -200, arcade.csscolor.RED, 0, 180)
arcade.draw_circle_filled(200,350,40, arcade.csscolor.AQUAMARINE)
arcade.draw_circle_filled(400,350,40, arcade.csscolor.AQUAMARINE)

# Finish drawing
arcade.finish_render()

arcade.run()