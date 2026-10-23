# Custom 75% Mechanical Keyboard

This is a custom 75% mechanical keyboard with 3 macro keys that I designed every part for, from the PCB to the firmware.

![Case](Images/Case/case.png)

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

<img width="1225" height="827" alt="image" src="https://github.com/user-attachments/assets/6153b32f-142e-4564-8010-f7911233e43d" />
<img width="1090" height="455" alt="image" src="https://github.com/user-attachments/assets/d2a8b777-40d2-48f2-b0fc-4bcd612ccd78" />

## BOM
| Sl No. | Name | Notes | Quantity | Price Per Unit | Cost | Shipping | Link |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | PCB | Manufactured by JLCPBC (minimum 5, order through JLclone desktop app - saves money) | 1 | $25.50 | $25.50 | $15.00 | [JLCPCB](JLCPCB) |
| 2 | Diode (1N4148) | Diodes to prevent ghosting (need 84, minimum 100) | 100 | $0.0295 | $2.95 | $13.54 | [LCSC](https://www.lcsc.com/product-detail/C258182.html) |
| 3 | Resistor (0805W8F5600T5E) | For start and end of LED data signals (only need 2, minimum of 100) | 100 | $0.0028 | $0.28 | Included* | [LCSC](https://www.lcsc.com/product-detail/C28636.html) |
| 4 | Capacitor (CC0603KRX7R7BB104) | Decoupling capacitors for LED's (need 83, multiples of 50) | 100 | $0.0142 | $1.42 | Included* | [LCSC](https://www.lcsc.com/product-detail/C108079.html?s_z=n_q_CC0603KRX7R7BB104) |
| 5 | LED (SK6812MINI-E) | LED's for backglow of the keyboard (order in multiples of 5) | 85 | $0.0651 | $5.53 | Included* | [LCSC](https://www.lcsc.com/product-detail/C5149201.html?s_z=n_SK6812%2520MINI-E) |
| 6 | Raspberry Pi Pico W (with headers) | The microcontroller for the keyboard (already owned) | 1 | $0.00 | $0.00 | $0.00 | [PiShop](https://www.pishop.ca/product/raspberry-pi-pico-w/) |
| 7 | Switches | Mechanical keyboard switches (pack of 100) | 100 | $0.20 | $20.00 | $0.00 | [Amazon](https://www.amazon.com/dp/B0CX8X1X7P) |
| 8 | Keycaps | Keycaps for the switches | 1 | $10.09 | $10.09 | $0.00 | [AliExpress](https://www.aliexpress.com/item/1005009162201589.html) |
| 9 | Rotary Encoder | Rotary encoder for volume and play/pause media (already owned) | 1 | $0.00 | $0.00 | $0.00 | [DigiKey](https://www.digikey.ca/en/products/detail/bourns-inc/PEC11R-4220F-S0012/4499661) |
| 10 | Rotary Encoder Knob | Knob for the rotary encoder, 3D printed | 1 | $0.00 | $0.00 | $0.00 | — |
| 11 | Case + plate | 3D printed | 1 | $0.00 | $0.00 | $0.00 | — |
| 12 | Stabilizers | 7x 2u, 1x 6.25u | 1 | $12.05 | $12.05 | $0.00 | [Walmart](https://www.walmart.ca/en/ip/Mechanical-Keyboard-Cherry-Mx-Switch-Pcb-Mounted-Cherry-Stabilizer-Clear-Transparent-Case-6-25U-Modifier-Key-Stabiliser/7HYKUIE7RG06) |
| 13 | USB C Cable | Aviation style, coiled | 1 | $7.56 | $7.56 | $0.00 | [Amazon](https://www.amazon.ca/Coiled-Keyboards-Aviation-Mechanical-70-87inch/dp/B0GYD7GZT2) |
| 14 | Type C to Micro USB | For connecting the USB C cable to the pico | 1 | $1.78 | $1.78 | $0.00 | [Amazon](https://www.amazon.ca/dp/B0D8ZSWC1D) |

> **Additional Notes:** Items from Amazon may have shipping charges; Amazon Prime is used so shipping costs are not included. 
> 
> All LCSC items share a combined shipping fee of **$13.54 USD**. PCB shipping is estimated at **$15.00 USD**. Total shipping: **$28.54 USD**.

- **Sub Total:** $87.16 USD
- **Shipping Total:** $28.54 USD
- **Total USD:** $115.70 USD

## Files
[PCB](PCB)
[CAD](CAD)
[Firmware](Firmware)
[Journal](JOURNAL.md)
[BOM](BOM)

## Credits
This was made possible through the funding of Hack Club and KEEB, opensource firmware and software, everyone who helped with my questions in the slack, 3D models from grabcad, tutorials on YouTube, and inspiration from other KEEB github repos.
