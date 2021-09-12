# Simulation Experiments
Based on the simulation environment what are the questions to be asked.

## Questions/Experiments
Variables to be considered:
- Patch density 
- Prey density
- Angle of turn
- Turn variability
- Prey replacement

### ER0: Random Search in Single Patch with Replacement
Given random search with a set angle of turn and varience within a single patch/environment what is the number of prey captured. 
 Variables to be modified:
 - Single Patch equal to environment size:
 - Prey density increasing 10, 20 ,40, 80, 160, etc
 - Modify angle of turn between 30, 60, and 90 degrees
 - Modify variance in angle of turn between low and high variablity
 - Prey get replaced on removal so density stays the same

This represents a homogenous environment where prey are distributed randomly. So we are looking at three variables and determining their relationship. There are about 30 combinations here (Density=5) x (Angle Turn=3) x (Varience=low|high). Whilst these combinations may not reflect the true experimental space they are a start and so may provide some insight.

#### ER0.1 Vary by prey density with low turn rate. low varience
 - Prey density = 10, 20, 40, 80, 160
 - Angle turn = 30
 - Angle varience = low

#### ER0.2 Vary by prey density medium turn rate, low varience
- Prey density = 10, 20, 40, 80, 160
 - Angle turn = 60
 - Angle varience = low

#### ER0.3 Vary by prey density high turn rate, low varience
- Prey density = 10, 20, 40, 80, 160
 - Angle varience = low

### ER1: Random Search in Single Patch with No Replacement
Repeat the above where prey do not get replaced. This represents the drop in capture as the resource gets depeleted in a patch. So a single patch in a heterogeneous environment

### ER3: Random Search in Multiple Patches

Variables:
- Patch Size
- Distance between patches (number of patches)
- Patch density (number prey per patch)
- Angle of turn
- Varience of turn

### EA1: Simple Area Restricted Search









