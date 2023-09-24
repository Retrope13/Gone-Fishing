
##I'm handling the if statment to determine who it is on this side because it'll be easier to read
def handle_message(sender, subject, content, army):
    if sender == "thejennymckay@gmail.com":
        handle_J(subject, content, army[1])
    if sender == "thepaulmckay@gmail.com":
        handle_P(subject, content, army[2])
    elif sender == 'sammckay31@gmail.com':
        handle_S(subject, content, army[0])
    return
        
###Handling and flipping cards based on person sending message
def handle_J(subject, content, J):
    J.setMessage(content)
    if subject == "Gone":
        ##Gone == 1
        J.flip_logic(1, "gone")
    elif subject == "Home":
        ##Home == 0
        J.flip_logic(1, "home")
    else:
        J.flip_logic(1)
    

def handle_P(subject, content, P):
    P.setMessage(content)
    if subject == "gone":
    ##Gone == 1
        P.flip_logic(2, "gone")
    elif subject == "home":
        ##Home == 0
        P.flip_logic(2, "home")
    else:
        P.flip_logic(2)
        
        
        
def handle_S(subject, content, Hokage):
    Hokage.setMessage(content)
    if subject == "gone":
        ##Gone == 1
        Hokage.flip_logic(0, "gone")
    elif subject == "home":
        ##Home == 0
        Hokage.flip_logic(0, "home")
    else:
        Hokage.flip_logic(0)    