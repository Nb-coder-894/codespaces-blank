input_dict = {
    "korfu" : "dog",
    "meow" : "cat",
    "bumble" : "mouse",
    "pixel" : "dog",
    "whisker" : "cat",
    "pingpong" : "dog"
}
# the counter dict is made in order to keep count of the types of animals. The dictionary is made for, well, being a dictionary.
doggy_dict = 0
kitty_dict = 0
mousey_dict = 0
#This isn't really chatgpt's way, but I am creating separate dictionaries. Lets see what happens.

if input_dict == "korfu":
    doggy_dict += 1
elif input_dict == "pixel" or "pingpong":
    doggy_dict += 0
elif input_dict == "meow":
    kitty_dict += 1
elif input_dict == "whisker":
    kitty_dict += 0
elif input_dict  == "bumble":
    mousey_dict += 1
Total_value = kitty_dict + mousey_dict + doggy_dict    
print("The number of animals is (Total_value)")
# This is basically making the values only increase when there are certain values of input_dict.               
