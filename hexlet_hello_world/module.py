# hexlet_hello_world/module.py

from more_itertools import sliced, substrings

from hexlet_hello_world.example import example_function

subs = ["".join(s) for s in substrings("more")]
print(subs)

slices = list(sliced((1, 2, 3, 4, 5, 6, 7, 8), 3))
print(slices)


def main():
    print("Запуск приложения")
    example_function()


if __name__ == "__main__":
    main()

