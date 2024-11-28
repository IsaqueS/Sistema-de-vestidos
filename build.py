import subprocess

def build() -> None:
    print("This Script its made to Build the App.")
    options = """\n1. Windows (Must execute on Windows)
2. Linux (Not implemented) (Must execute on Linux)
3. Mac OS (Not implemented) (Must execute on Mac)
4. Web (Not implemented)
    """
    print("Please select the platform you want to build the App.\n(You will need flet and Flutter to be installed on your machine, or enviroment)")
    print(options)
    
    option = None

    while not isinstance(option, int):
        try:
            option = int(input("type: option here: "))
        except Exception:
            print("The number must be an Integer!")

    match option:
        case 1:
            print("Building on Windows...")
            subprocess.run(
                ["flet", "build", "windows"]
            )

        case 2:
            print("Sorry, Linux, its not implemented yet. :P")
        case 3:
            print("Sorry, Mac OS, its not implemented yet. :P")
        case 4:
            print("Sorry, Web, its not implemented yet. :P")
        case _:
            print("Not an valid :P")
    print("Build Process done!")

if __name__ == "__main__":
    build()
