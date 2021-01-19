# Hello Guys Welcome to my Channel
# M Tech-G

# Follow My Commands For Rotate The Screen Of your laptop

# Firtly Open The terminal and Type:

# NOw Type This Command

import rotatescreen
import keyboard

#After This Type

screen = rotatescreen.get_primary_display()

# Now Type THis Command

keyboard.add_hotkey('ctrl+alt+up',screen.set_landscape,suppress=True)

# This Code is for normal view of Pc
# For Flipped View Type This :

keyboard.add_hotkey('ctrl+alt+down',screen.set_landscape_flipped,suppress=True)

# For Portrait View Type this Command

keyboard.add_hotkey('ctrl+alt+left',screen.set_portrait,suppress=True)

# For Portrait Flipped View Tpre

keyboard.add_hotkey('ctrl+alt+right',screen.set_portrait_flipped,suppress=True)



# HERE CTRL = Control Button
# Alt = Alt Button
# Left , Right  , UP , Down = Arrow Buttons:


# So Run THis Code Type THis :
keyboard.wait()


# Now Run this Code


# NOW IM PRESS CTRL+ ALT+ Down


# SO this Is How We Can Rotate The Screen of laptop by using python


# IF You like my video then like & Shhare this video to your friends

# Also Don't Forget to Subscribe my channel

