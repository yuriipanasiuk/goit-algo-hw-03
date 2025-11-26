import turtle


def koch_curve(t: turtle.Turtle, order: int, size: float) -> None:
    """Recursively draws one side of a Koch snowflake"""
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order: int, size: float = 300) -> None:
    """Draws a complete Koch snowflake"""
    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"Koch Snowflake - level {order}")

    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    t.pensize(2)

    t.penup()
    t.goto(-size / 2, -size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    t.penup()
    t.goto(0, -size / 2 - 30)
    t.write(f"Recursion level: {order}", align="center", font=("Arial", 16, "bold"))

    window.mainloop()


def main() -> None:
    while True:
        try:
            level = input("Enter the recursion level: ").strip()
            order = int(level)
            if order < 0 or order > 8:
                print("Please enter a number from 0 to 8")
                continue
            break
        except ValueError:
            print("Enter a whole number!")

    size_map = {0: 400, 1: 400, 2: 400, 3: 300, 4: 300, 5: 200, 6: 150}
    size = size_map.get(order, 100)

    draw_koch_snowflake(order, size)


if __name__ == "__main__":
    main()
