import turtle
import time
import textwrap

# Set up the screen
win = turtle.Screen()
win.title("A Protector's Promise")
win.bgcolor("lightblue")

# Create turtle
tiny = turtle.Turtle()
tiny.shape("turtle")
tiny.color("darkgreen")
tiny.speed(1)
tiny.hideturtle()

# Function to print multi-line wrapped text
def print_text(text, width=60):
    tiny.clear()
    wrapped_text = textwrap.wrap(text, width)
    y = 200
    tiny.penup()
    for line in wrapped_text:
        tiny.goto(-280, y)
        tiny.write(line, font=("Arial", 14, "bold"))
        y -= 25  # Adjust line spacing
    tiny.pendown()

# Story animation
print_text("Seated in a five-headed divine serpent, Shesh Ji, all the Lords bowed before Lord Vishnu, the ultimate protector. Sitting beside him was his beloved consort and Goddess of Wealth, Devi Lakshmi.")
time.sleep(3)
tiny.forward(100)

print_text("The Lords bowed before him and recited the verse. The lotus eyes of the Lord opened to dispel the sadness of his devotees.")
time.sleep(2)
tiny.left(90)
tiny.forward(100)

print_text("Upon opening his eyes, everyone bowed before Lord Vishnu.")
time.sleep(2)
tiny.right(90)
tiny.forward(100)

print_text("With his shining smile, the Lord blessed them. And enquired them for the reason of their sadness.")
time.sleep(2)
tiny.left(90)
tiny.forward(100)

print_text("The Lords described their concerns for planet Earth as it was unsafe due to the havoc caused by demons.")
time.sleep(2)
tiny.right(90)
tiny.forward(100)

print_text("Hearing their concerns, Lord promised them that he will take an incarnation and fulfill the responsibility of protecting the Earth.")
time.sleep(2)

# Final message
tiny.penup()
tiny.goto(-250, -200)
tiny.pendown()
print_text("The end.\nMay the Lord always protect us. 🌟")

turtle.done()
