import turtle


def draw_pifagor_tree(branch_length, level):
    if level == 0:
        return
    # рисуємо основну гілку
    turtle.forward(branch_length)
    turtle.right(45)

    # рекурсивно малюємо праву гілку
    draw_pifagor_tree(0.7 * branch_length, level - 1)
    turtle.left(90)

    # рекурсивно малюємо ліву гілку
    draw_pifagor_tree(0.7 * branch_length, level - 1)
    turtle.right(45)
    turtle.backward(branch_length)


def main():
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("green")
    turtle.left(90)
    turtle.up()
    turtle.backward(200)
    turtle.down()
    level = int(input("Введіть рівень рекурсії: "))
    draw_pifagor_tree(100, level)
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
