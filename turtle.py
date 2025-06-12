import turtle
import time

win = turtle.Screen()
win.title("A Protector's Promise")

tiny = turtle.Turtle()  # Define tiny as a Turtle object

def print_text(text):
    global tiny
    tiny.clear()
    tiny.penup()
    tiny.goto(-200, 200)
    tiny.pendown()
    tiny.write(text, font=("Arial", 16, "normal"))

tiny.shape("turtle")  # Set the shape of the turtle
tiny.speed(1)  # Set the speed of the turtle

print_text("Seated in a five headed divine serpent, Shesh Ji, all the Lords bowed before Lord Vishnu, the ultimate protector. Sitting beside him was his beloved consort and Goddess of Wealth, Devi Lakshmi")
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

print_text("Hearing their concerns, Lord promised them that he will take an incarnation and fulfill the responsibility of protecting the Earth..")
time.sleep(2)
tiny.penup()
tiny.goto(-200, -200)
tiny.pendown()
print_text("The end.")

turtle.done()


