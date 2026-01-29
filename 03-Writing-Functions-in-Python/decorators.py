# Python Code to Implement Simple Decorators
def add_sprinkles(fx):
    def mfx(*args, **kwargs):
        print(f"Sprinkling Flakes on the {flavour} Ice Cream ✨")
        return fx(*args, **kwargs)
    return mfx

def add_fudge(fx):
    def mfx(*args, **kwargs):
        print(f"Adding Fudge to the {flavour} Ice Cream 🍫")
        return fx(*args, **kwargs)
    return mfx

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} Ice Cream 🍦")

flavour = input("What flavour Ice Cream would you like?: ")
get_ice_cream(flavour)