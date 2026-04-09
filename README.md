# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`Hiyya Pati (individual project)`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `Hiyya` | `Electronics / Coding / Fabrication / Mechanics` | `NA` | `Knowledge of basic circuitry and coding, aesthetic sensibilities` |


## 1.3 Project Title
`Ethereal Flowers`

## 1.4 One-Line Pitch
`A panel of blooming flowers which responds to the movement of your hand over it.`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`This project involves an interactive panel consisting of about 20 mechanised flowers. As the participant moves their hand over this panel, the flower(s) just underneath respond to the hand movement by blooming open. This will hopefully create a unique visual and sensory experience for the participant, with a touch of whimsical magic and fairylike charm.
The technologies involved in this project are ultrasonic sensors and servo motor mechanisms, controlled by a MicroPython code through an ESP32.`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`With this project, I seek to create a magical experience for the participant that allows them to bloom flowers with a wave of their hand. I want the participant to feel enchanted and powerful, and I hope that the experience will be delightful enough for them to want to try it again.`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`I am designing this project as if I were a small creative studio making an interactive experience for exhibition visitors of all ages.`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `[Toy / Board game / App / Video / Website / Object]` | `[Link or title]` | `[What did you learn or borrow?]` |
| `[Toy / Board game / App / Video / Website / Object]` | `[Link or title]` | `[What did you learn or borrow?]` |
| `[Toy / Board game / App / Video / Website / Object]` | `[Link or title]` | `[What did you learn or borrow?]` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`[Write here]`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`Connect and run code → move hand over panel → ultrasonic sensor detects → respective servo motor rotates → flower just under hand opens and lights up`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `Exhibition visitors or someone looking for a fun visual experience` |
| Age range | `All ages` |
| Solo or multiplayer | `Solo, can also be experienced in a group` |
| Expected duration of one round | `About 2 minutes but ideally as long as the participant wishes to engage with it` |
| What should the player feel? | `Joy, whimsical delight` |
| Is explanation required before use? | `Very minimal, just a prompt for them to move their hand over the panel` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `The participant sees the flower panel and approaches it.`
2. **Start:** `They read the instruction to move their hand over the panel.`
3. **First Action:** `They move their hand over the flowers.`
4. **Main Interaction:** `The player moves their hand across the panel, in whatever patterns they wish to create.`
5. **System Response:** `The flowers bloom as the hand moves over them, following the pattern desired by the player.`
6. **Win / Lose / End Condition:** `When the player has finished enjoying the experience. (Or could also have a timer for fixed duration.)`
7. **Reset:** `The next round begins when another participant comes over and moves their hand over the panel.`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

`NA`

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] `Mechanised flowers open and close using servo motors.`
- [ ] `Ultrasonic sensors detect hand movement to some accuracy.`
- [ ] `Flowers open up according to position of hand.`
- [ ] `Flower close back after a certain duration.`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`A single flower that blooms when it detects hand movement above it and closes back after a fixed duration.`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `Multiple flowers arranged in arrays`
- `Flowers with multiple layers of petals`
- `Flowers made of material(s) that are delicate and aesthetically pleasing`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [x] Electronics-based
- [x] Mechanical
- [x] Sensor-based
- [ ] App-connected
- [x] Motorized
- [ ] Sound-based
- [x] Light-based
- [ ] Screen/UI-based
- [x] Fabricated structure
- [ ] Game logic based
- [x] Installation / tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
- `Input: Ultrasonic sensors placed at different points on the panel detect hand movement.`
- `Processing: The sensors correspond to specific flowers based on proximity. When a sensor detects hand movement, the ESP32 sends instructions to the servo motor to rotate by a certain angle and open the flower. `
- `Output: The flower(s) underneath the hand open and light up.`
- `Physical structure: The flower uses an umbrella mechanism to open and close. A lever connects the servo to the flower handle that converts the rotational motion of the servo to the vertical motion required to open the flower. The structure is made by hand using basic materials.`
- `App interaction: NA`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `Ultrasonic Sensor` | Input | `Detects hand motion above the panel and sends corresponding signals to the ESP32` |
| `ESP32` | Processing | `Takes data from the sensor and instructs the servos and LEDs accordingly` |
| `Servo` | Output | `Opens up the petals of the flower` |
| `LED` | Output | `Lights up the flower as it blooms` |
| `Mechanical Assembly` | Physical Action | `Translates the rotational motion of the servo to a vertical motion that opens & closes the petals of the flowers` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
<img src="images/Concept sketch 1.jpeg" width="300"> <img src="images/Concept sketch 2.jpeg" width="500">

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
<p align="center">
  <img src="images/Labelled build sketch.jpeg" width="400">
</p>

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[Write here]` |
| Width | `[Write here]` |
| Height | `[Write here]` |
| Estimated weight | `[Write here]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [x] Linkages
- [ ] Hinges
- [x] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [x] Sliders
- [x] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`The flower uses an umbrella mechanism to open and close. A slider on the flower stem is pulled up and down to open and close the flower, respectively. A lever connects the servo to the stem slider that converts the rotational motion of the servo to the vertical motion required to open the flower. The structure is made by hand using basic craft materials.`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
- `The petals of the flower move, creating an illusion of the flower blooming.`
- `Vertical movement of the slider causes the movement, using an umbrella mechanism.`
- `The vertical distance for full movement is about 5 cm.`
- `Speed can be controlled/changed through the servo.`
- `Umbrella mechanism doesn't work as planned, or servo rotation does not accurately convert to vertical motion.`

## 8.4 Simulation / CAD / Animation Before Making - NA
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Fusion 360 / Tinkercad / other]` | `[Link or screenshot]` | `[What did you validate?]` |
| `[Tool]` | `[Link or screenshot]` | `[What did you validate?]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`NA as mechanisms were made by hand and tested accordingly.`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `ESP32` | `1` | `Main controller` |
| `Power adapter` | `1` | `External power source` |
| `LM2596 Buck regulator` | `1` | `Provide adequate current for multiple devices` |
| `PCA9685` | `1` | `Connect multiple (16) servos to 2 pins` |
| `Ultrasonic sensors` | `16` | `Detect hand movement above panel` |
| `Servo motors` | `16` | `Open and close flowers` |
| `Breadboard` | `1` | `For electrical connections` |
| `Male and female jumper wires` | `50 (approx.)` | `To connect electrical components` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
- `LM2596 connected to wall socket via adapter.`
- `ESP32 connected to LM2596.`
- `16 servos connected to ESP32 through PCA.`
- `16 ultrasonic sensors connected to ESP32.`
- resistors, other things???????????

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `Adapter` |
| Voltage required | `[Write here]` |
| Current concerns | `[Write here]` |
| Safety concerns | `[Write here]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `MicroPython` | `Coding` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behaviour,
- communication logic,
- reset behavior.

**Response:**  
- `When code runs, all sensors get triggered.`
- `Each sensor corresponds to a flower with a servo.`
- `When a particular sensor detects an object, its corresponding servo is instructed to rotate by 180 degrees.`
- `The servo rotates with time delays for the flower to open up slowly.`
- `The servo waits for 2-3 seconds, then slowly rotates back to its original position.`
- `During this time, the servo does not react to sensor input to avoid clashing signals and malfunction.`
- `However, during this time, other servos can be activated by their respective sensors.`
- `Once the servo is back to its original position, it can again be activated by the sensor, and the loop repeats until the code is running.`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
<img src="images/Code Flowchart.jpg" width="700">

## 10.4 Pseudocode

```text
[Write your pseudocode here]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [x] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `ESP32` | `1` | `Yes` | `Yes` | `500` | `--` | `--` |
| `Adapter` | `1` | `Yes` | `No` | `0` | `--` | `--` |
| `Breadboard (joined)` | `1` | `Yes` | `No` | `0` | `--` | `--` |
| `Jumper wires (male and female)` | `50` | `Yes` | `No` | `0` | `--` | `--` |
| `Wire cutter` | `1` | `Yes` | `No` | `0` | `--` | `--` |
| `LM2596 Buck Regulator` | `1` | `No` | `Yes` | `100` | `--` | `To supply sufficient power to multiple components` |
| `PCA9685` | `1` | `No` | `No` | `0` | `--` | `To connect multiple servos to 2 ESP pins` |
| `Ultrasonic sensor` | `16` | `Yes` | `No` | `0` | `--` | `To detect user's hand` |
| `Servo motor` | `16` | `Yes` | `Yes (10)` | `1000` | `--` | `For accurate motion` |
| `Chart paper` | `2` | `No` | `No` | `0` | `--` | `For flexible build construction` |
| `Fabric` | `12 m` | `No` | `Yes` | `600` | `Polyester wrapping paper` | Translucent fabric for visual apppeal |
| `Craft wire` | `1 pack (~50)` | `No` | `No` | `0` | `Aluminium, 24 gauge` | `To give shape/structure to the flower` |
| `MDF board` | `2 sq.m` | `No` | `No` | `0` | `3 mm` | `Sturdy enough for the multi-layered base of installation` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
- `Servo over DC/stepper motor: Small size and easy connections with accurate rotation angles`
- `Paper & wire mechanism over 3D print: More scope for modification & correcting errors, less time spent on modelling and 3D printing`
- `MDF over sunboard/cardboard: More sturdiness/stability, easier to drill holes and cut accurate pieces`
- `Fabric over 3D-printed petals: Gives a delicate feel and aesthetic charm to the flowers`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `ESP32` | `For processing code` | `https://amzn.in/d/0a81HenG` | `15/04/2026` | `Received` |
| `LM2596 Buck Regulator` | `For providing adequate power` | `https://amzn.in/d/05CM7O02` | `18/04/2026` | `Received` |
| `Servo motor` | `For opening-closing mechanism` | `https://amzn.in/d/09Z82pvn` | `15/04/2026` | `Received` |
| `Fabric` | `For petals` | `https://amzn.in/d/0gyDqJPB` | `13/04/2026` | `Received` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `1600` |
| Mechanical parts | `--` |
| Fabrication materials | `600` |
| Purchased extras | `--` |
| Contingency | `--` |
| **Total** | `2200` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`I've tried to make this as cost-efficient as possible, I don't think anything else can be simplified for the required build.`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`NA (individual project)`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `Hiyya` | `2` | `01/04/2026` | `None` | `Completed` |
| T2 | `[Complete BOM]` | `Hiyya` | `1` | `07/04/2026` | `T1` | `Completed` |
| T3 | `[Test electronics]` | `Hiyya` | `2` | `15/04/2026` | `T1` | `To Do` |
| T4 | `[Build structure]` | `Hiyya` | `18` | `16/04/2026` | `T1` | `In progress` |
| T5 | `[Write control code]` | `Hiyya` | `4` | `15/04/2026` | `T3` | `To Do` |
| T6 | `[Integrate system]` | `Hiyya` | `4` | `18/04/2026` | `T4, T5` | `To Do` |
| T7 | `[Playtest]` | `Hiyya` | `2` | `19/04/2026` | `T6` | `To Do` |
| T8 | `[Refine and document]` | `Hiyya` | `4` | `20/04/2026` | `T7` | `In progress` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `Hiyya` | `NA` |
| Electronics | `Hiyya` | `NA` |
| Coding | `Hiyya` | `NA` |
| Mechanical build | `Hiyya` | `NA` |
| Testing | `Hiyya` | `NA` |
| Documentation | `Hiyya` | `NA` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [x] BOM completed
- [x] Purchase needs identified
- [x] Key uncertainty identified
- [x] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [x] Electronics tests completed
- [x] CAD / structure planning completed
- [ ] App UI started if needed
- [x] Mechanical concept tested
- [x] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [ ] Physical body built
- [ ] Electronics integrated
- [ ] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `Start working on build planning` | `Finalised idea` | `Need to make multiple flowers that interact with user` | `Plan build and mechanisms` |
| Week 2 | `Prototype the basic mechanism` | `Made a working prototype of flower` | `Need to add wire reinforcements` | `Make all the flowers` |
| Week 3 | `Finish build and start working on code and circuits` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `Complete project and documentation` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `Ultrasonic sensors don't detect motion as planned` | `Technical` | `Medium` | `High` | `Change position of sensors / use hard object to reflect sound better` | `Hiyya` |
| `Structure breaks during play` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `Hiyya` |
| `Building and integration takes too much time` | `Time` | `High` | `High` | `Reduce number of flowers / start with enough time at hand` | `Hiyya` |
| `Servo motors don't open flower as planned` | `Mechanical` | `Low` | `High` | `Change material/orientation of pull tabs` | `Hiyya` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`Integration of physical build with code and circuits, making the flowers move without assistance.`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `Servo motors` | `Test each motor individually` | `Servo rotates correctly as per code` |
| `[Mechanism movement]` | `Make 1 flower with servo connection and check if it works` | `Flower visibly opens and closes` |
| `[Sensor behavior]` | `Test each sensor individually` | `Sensor detects movement of hand ~20cm away from it` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `Players just have to move their hand over the panel, no testing required.` |
| Is the interaction satisfying? | `Will see their reaction as they interact with the installation.` |
| Do players want another turn? | `Players can interact with it ideally as long as they wish.` |
| Is the challenge balanced? | `The installation is more of an experience than a challenge. Will ask users if they enjoyed the experience.` |
| Is the response clear and immediate? | `Will find out from observing users interact with it.` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Date]` | `[Describe issue]` | `[Technical / Mechanical / UI / Gameplay]` | `[What you did]` | `[Worked / Partly / Failed]` | `[Next step]` |
| `[Date]` | `[Describe issue]` | `[Type]` | `[What you did]` | `[Result]` | `[Next step]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
- `First prototype of flower mechanism made using paper.`
- `Built 16 flowers using the same mechanism, with wire reinforcements to support the fabric petals.`
- `Tested flower movement with servo motor and code.`
- `Made an small MDF base for each flower as a separate module, with holes drilled into it for wires to pass through.`
- `Attached flower, servo, and sensor to each MDF panel.`
- `Made a larger MDF base to put together the flowers.`
- `Secured wire connections from each module to the breadboard attached to the large base`
- `Tested code with the build.`
- `Playtesting with users.`
- `Made small revisions and cleaned up the build.`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[Date]` | `[Describe]` | `[Reason]` |
| `v2` | `[Date]` | `[Describe]` | `[Reason]` |
| `v3` | `[Date]` | `[Describe]` | `[Reason]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Write here]`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
