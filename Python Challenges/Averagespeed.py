Cyclistone=10
Cyclisttwo=20
Cyclistthree=30
Average=(Cyclistone+Cyclisttwo+Cyclistthree)/3
if Average>Cyclistone and Average>Cyclisttwo and Average>Cyclistthree:
    print(f"{Average} is higher than {Cyclistone},{Cyclisttwo},{Cyclistthree}")
elif Average>Cyclistone and Average>Cyclisttwo:
    print(f"{Average} is higher than {Cyclistone},{Cyclisttwo}")
elif Average>Cyclistone  and Average>Cyclistthree:
    print(f"{Average} is higher than {Cyclistone},{Cyclistthree}")
elif Average>Cyclistone :
    print(f"{Average} is higher than {Cyclistone}")
elif Average>Cyclisttwo :
    print(f"{Average} is higher than {Cyclisttwo}")
elif Average>Cyclistthree :
    print(f"{Average} is higher than {Cyclistthree}")
else:
    print("invalid")