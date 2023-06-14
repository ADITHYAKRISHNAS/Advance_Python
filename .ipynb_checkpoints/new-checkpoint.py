x = "global x"

def level_seven():
    def please_dont_do_this():
        if False:

            a = None

        def gen_func():
            nonlocal a
            for v in range(10):
                a =  v
                yield v
        return gen_func(), lambda:a
    
    gen, fun = please_dont_do_this()
    
    # print(fun())
    next(gen)
    print(fun())
    next(gen)
    print(fun())

level_seven()
