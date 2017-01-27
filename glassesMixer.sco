rtsetparams(44100, 8, 24)
set_option("clobber = on", "play = off")
rtoutput("/Users/aaronstepp/Desktop/glassesBounce.aif")

rtinput("/Users/anstepp/Desktop/glassesOne.aif")
MIX(0, 0, DUR(), 1, 0, 1, 2, 3, 4, 5, 6, 7)

rtinput("/Users/anstepp/Desktop/glassesTwo.aif")
MIX(0, 0, DUR(), 1, 0, 1, 2, 3, 4, 5, 6, 7)

rtinput("/Users/anstepp/Desktop/glassesThree.aif")
MIX(0, 0, DUR(), 1, 0, 1, 2, 3, 4, 5, 6, 7)

rtinput("/Users/anstepp/Desktop/glassesFour.aif")
MIX(0, 0, DUR(), 1, 0, 1, 2, 3, 4, 5, 6, 7)

rtinput("/Users/anstepp/Desktop/glassesFive.aif")
MIX(0, 0, DUR(), 1, 0, 1, 2, 3, 4, 5, 6, 7)