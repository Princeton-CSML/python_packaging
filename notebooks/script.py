import mod

# only execute code in a particular scope, when script.py read from standard input
# i.e., script.py is entrypoint of application
if __name__ == "__main__":
    print(mod.circ_area(3))
