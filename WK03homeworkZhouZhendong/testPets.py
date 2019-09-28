from pets import Pets, Cat, Dog


def main():
    tom = Pets("汤姆", "红色")
    print(tom)

    tommy = Cat("汤米", "灰色", "美国短毛猫", "短毛猫")
    print(tommy)

    linyheart = Dog("Linyheart", "蓝色", "柴犬", "大型犬")
    print(linyheart)

    tom.takefood()
    tom.sleep()

    tommy.takefood()
    tommy.sleep()
    tommy.meow()
    tommy.scratch()

    linyheart.takefood()
    linyheart.sleep()
    linyheart.bark()
    linyheart.bite()


main()