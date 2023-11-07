from sense_hat import SenseHat

# Initialize the SenseHat object
sense = SenseHat()

# Set text color
text_color = (255, 255, 255)

# Set background color
bg_color = (0, 0, 0)

# Set message
message = "Hello world"

# show message
sense.show_message(message, text_colour=text_color, back_colour=bg_color)

# clear message
sense.clear()