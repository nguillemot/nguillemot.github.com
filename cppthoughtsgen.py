title = "C++ Thoughts"

intro =  \
"Random little thoughts about C++ coding that have sprung up in my head over the years. Sometimes inspired by other people, sometimes inspired by my mistakes."

# (header, body, footer)
thoughts = [

("Copy and move are quirky",
"Copy and move are quirky; their performance characteristics differ greatly depending on the implementation details of the class. If you want to use specific operations for performance reasons, use functions that actually do what you want (eg. swap) rather than assuming the implementation of a move is the one you expect.",
"Inspired by the contrast of reasoning about performance between Mike Acton and Herb Sutter's keynotes at cppcon 2014."),

("Movable classes are containers",
"""If you make a class movable, it will behave as if it was a container rather than the object itself. 
That is because the address of an object can no longer be used to represent the identity of the instance.
This makes it impossible to reliably track an object using its address, since the object would have to provide a hook in its move assignment operator that patches the pointer used to track the object.
Doing such actual work in a move constructor feels wrong, but might be an important detail for a C++11 observer pattern implementation that doesn't want to require wrapping everything in another container like shared_ptr.""",
"Inspired from somebody's tweet about the error of using an address as an identity for an object, and finding myself making the same mistake later."),

("Don't build coding standards assumptions into your interfaces",
"""C++ simplifies code by letting you build assumptions about usage into the interface of a class, and offers a wide variety of methods for implementing those same assumptions using very different coding standards conventions (eg. exceptions versus error codes.)
It's hard to build a timeless interface when you build assumptions about usage into it, so offer an interface layer for your code with fewer assumptions.
An easy way to do this is to limit your interface to be implemented as a C header, which actually comes with other bonuses like ABI stability.""",
"Inspired from Stefanus Du Toit's talk on Hourglass Interfaces"),

("bool(ean) is a pretty bad name for a true/false type",
"""This is not strictly restricted to C++.
The etymology of primitive types generally makes sense: int for integers, float for floating point, long for bigger numbers... but \"bool\" remains kinda meaningless.
It's just some guy's name. I think this just needlessly increases the learning curve for teaching programming to young students who have not yet studied boolean algebra.
There are probably better names out there.
Some suggestions: tof/torf (true or false), truth, predicate, logic, bit... Or as C did it, just keep them ints.""",
"Inspired by my difficulty to grasp booleans as a youngster.")

] # End of thoughts

from datetime import datetime

print("<html>")

print("<head>")
print("<title>")
print(title)
print("</title>")
print("</head>")

print("<body>")

print("<h1>" + title + "</h1>")
print("<p>")
print(intro)
print("</p>")

print("<i>Last updated %s</i>" %
    datetime.now().strftime("%B %d %Y"))

for thought in thoughts:
    thoughtHeader = thought[0]
    thoughtBody = thought[1]
    thoughtFooter = thought[2]

    print("")
    escapedHeader = thoughtHeader.replace(' ', '_')
    print("<h2 id=\"#%s\">%s</h2>" %
        (escapedHeader, thoughtHeader))

    print("<p>")
    print(thoughtBody)
    print("</p>")

    print("<i>" + thoughtFooter + "</i>")
    print("</br>")

print("</body>")
print("</html>")
