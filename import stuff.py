def fun():
    name = input("Who are you?").strip().title()
    if name == "Jack":
        print("COPYCAT!")
    else:
        print("Nice to meet you, " + name)
    fun()
fun()
