from turtle import *
instructions = "ESDSSSSSSEEEUENDNNNNUNWDWWUEEEEEDEEEEWWWWSSSEEWWSSSEEEEUEENNNNNNDSSSSUSEDUSEDUNEDUNEDNNNNUEEDEEEEWWWWSSSSSSEEEEUEEDNNNNNNSSSEEEENNNSSSSSSUEEDNNNNUNEDUNEDUSEDUSEDSWWWEEESSSUEEDNNNNNNEEESSSNNNEEESSSSSSUEEDNNNNNNEEESSSWWUSSSEEEEEEEDWWNNNNNNEEUEEDSSSSSSEEEEUEEDNNNNNNUEEDSSSSSSEEEEUEEEENDNNNNSSWWEEEEUEENNNDEEEEWWWWSSSSSSEEEEUEENNNNNNDSSSSSSEEEENNNNNNUEEDEEEEEEWWWSSSSSSUEEEEEDNNNNNNEEEEWWWWSSSEEWWSSSEEEEUEEEENDNNNNSSWWEEEEUEENNNDSSSSSSEEEENNNWWWEENNNWWUEEEEEDSSSSSSEEEENNNNNNWWWWUEEEEEEDEEEEEEWWWSSSSSSUEEEEEDEENNNNNNWW"
pu()
color('red', 'yellow')
left(90)
setx(-400)
speed(0)
for i in instructions:
    if i == "N": fd(10)
    if i == "S": right(180); fd(10); right(180);
    if i == "W": left(90); fd(10); right(90);
    if i == "E": right(90); fd(10); left(90);
    if i == "D": pd()
    if i == "U": pu()

