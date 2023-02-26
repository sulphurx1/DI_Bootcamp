users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
disney_users_A = {}

for x, user in enumerate(users):
    disney_users_A.update({user: x})

# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
disney_users_B = {}

for x, user in enumerate(users):
    disney_users_B.update({x: user})

# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
new_users  = sorted(users)
disney_users_C = {}

for x, user in enumerate(new_users):
    disney_users_C.update({user: x})

# Only recreate the 1st result for: The characters, which names contain the letter “i”.
only_contain_i = {}

for x, user in enumerate(users):
    if "i" in user:
        only_contain_i.update({user: x})

# Only recreate the 1st result for: The characters, which names start with the letter “m” or “p”.
start_with_m_or_p = {}

for x, user in enumerate(users):
    if user.startswith('M') or user.startswith('P'):
        start_with_m_or_p.update({user: x})

