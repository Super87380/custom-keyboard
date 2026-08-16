# Custom 75% Mechanical Keyboard

This is a custom 75% mechanical keyboard that I designed every part for, from the PCB to the firmware.

![Case](../Images/Case/case.png)

## Why I Built it
A while before finding out about Hack Club I wanted to make my own mechanical keyboard. After finding out how much it would cost I got de motivated and gave up on the idea.
Later I was watching YouTube when the creator mentioned Hack Club and how they help teenagers get experience in engineering. I was looking through the programs running when I saw KEEB.
With the opportunity to get the keyboard funded by Hack Club/KEEB it was the perfect chance for me to make the keyboard I had wanted to before.

## Features
- 3 Macro keys
- Rotary Encoder with a switch
- RGB back lighting
- Vast firmware support - the firmware I made uses KMK

## Designing
I started this project by brainstorming ideas for different layouts, sizes, and features. My original idea was a 75% keyboard with a screen, 1 macro key, and a rotary encoder. The idea soon evolved into what it is now.
After brainstorming I used [keyboard layout editor](https://www.keyboard-layout-editor.com/) and [photopea](https://www.photopea.com/) to design the layout and matrix wiring digitally.
I then made the first schematic and PCB in KiCad with a screen and 1 macro key. After I finished the schematic and PCB I realized I wanted to add backlighting for late night gaming/programming sessions and more macro keys, so I added sk6812 mini-e LED's under each switch and removed the screen for 2 more macro keys. After I finished with the electronics I designed a case and plate in Onshape, I found this pretty challenging as it was my first time using Onshape; I can definitely improve the case a lot. I then made the firmware, I chose to sue KMK because I have more expierence with python and have made a macropad with KMK already.

## What I Found Difficult
- LED wiring, especially because I didnt originally route with them in minde
- Modeling the case and plate in Onshape
- Sourcing cheap components with cheap shipping

## What I Learned
- Modelling in Onshape
- Better PCB design
- How mechanical keyboards work
- Reading data sheets and applying what I read
- Layers in KMK
- RGB in KMK


## Files
[PCB](..//PCB)
[CAD](..//CAD)
[Firmware](..//Firmware)
[Journals](..//Journals)
[BOM](..//BOM)

## Credits
This was made possible through the funding of Hack Club and KEEB, opensource firmware and software, everyone who helped with my questions in the slack, 3D models from grabcad, tutorials on YouTube, and inspiration from other KEEB github repos.
