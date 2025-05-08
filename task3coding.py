# importing the GUI library turtle
import turtle

# main function
def make_my_tree(branch_length, my_tree_left_angle, right_angle, my_tree_depth, my_tree_reduction_factor):
    # first define if depth 0 true
    if my_tree_depth == 0:
        return
    
    # trank color 
    if my_tree_depth > 3:  
        turtle.color("brown")
        # branch color gree
    else:       
        turtle.color("green")
    
    # making a current branch
    turtle.pensize(my_tree_depth)  # Thicker branches near trunk
    turtle.forward(branch_length)
    
    # saving the my tree current position and heading
    my_tree_current_pos = turtle.position()
    my_tree_current_heading = turtle.heading()
    
    # drawing the left branch of tree
    turtle.left(my_tree_left_angle)
    make_my_tree(branch_length * my_tree_reduction_factor, my_tree_left_angle, right_angle, my_tree_depth-1, my_tree_reduction_factor)
    
    # return to saved position and heading of my tree
    turtle.penup()
    turtle.goto(my_tree_current_pos)
    turtle.setheading(my_tree_current_heading)
    turtle.pendown()
    
    # drawing the right branch of tree
    turtle.right(right_angle)
    make_my_tree(my_tree_branch_length * my_tree_reduction_factor, my_tree_left_angle, my_tree_right_angle, my_tree_depth-1, my_tree_reduction_factor)
    
    # return to saved position and heading of my tree
    turtle.penup()
    turtle.goto(my_tree_current_pos)
    turtle.setheading(my_tree_current_heading)
    turtle.pendown()


# taking user input
print("This is the code for my tree drawing ")
my_tree_left_angle = int(input("First add value for branch angle in degrees please :  "))
my_tree_right_angle = int(input("now add  for right branch angle in degrees: "))
my_tree_branch_length = int(input("Now add add value for starting branch length in pixels: "))
my_tree_depth = int(input("now value for recursion my_tree_depth 5-10 recommended: "))
my_tree_reduction_factor = float(input("add value for branch reduction factor (0.6-0.8 recommended): "))

# staring point 
turtle.left(90) 
turtle.penup()
turtle.goto(0, -200) 
turtle.pendown()

#starting color 
turtle.color("brown")

# making my tree 
make_my_tree(my_tree_branch_length, my_tree_left_angle, my_tree_right_angle, my_tree_depth, my_tree_reduction_factor)



