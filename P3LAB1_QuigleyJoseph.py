red = int(input())
green = int(input())
blue = int(input())
grey = 0


if (red <= green) and ( red <= blue):
    grey = red
    
if (green <= red) and ( green <= blue):
    grey = green
    
if (blue <= green) and ( blue <= red):
    grey = blue
    
red = red - grey
green = green - grey
blue = blue - grey
    
print(red, green, blue)