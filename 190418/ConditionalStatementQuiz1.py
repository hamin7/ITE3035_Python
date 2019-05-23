def which_prize(points):
    
    prize = None
    if 1 <= points <= 50:
        prize = "Congratulations! You won a [wooden rabbit]"
    elif 51 <= points <= 150:
        prize = "Oh dear, no prize this time."
    elif 151 <= points <= 180:
        prize = "Congratulations! You won a [wafer-thin mint]"
    elif 181 <= points <= 200:
        prize = "Congratulations! You won a [penguin]"
   
    if prize:
        return "Congratulations! You have won " + prize +"!"

print (which_prize(174))
