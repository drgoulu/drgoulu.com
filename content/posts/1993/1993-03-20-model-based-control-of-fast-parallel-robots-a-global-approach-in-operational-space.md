---
title: "Model-Based Control of Fast Parallel Robots : a Global Approach in Operational Space"
date: 1993-03-20
categories: 
  - "non-classe"
tags: 
  - "mecanique"
---

ma thèse de doctorat est désormais directement consultable en ligne : [Thèse no 1228, EPFL Lausanne](https://library.epfl.ch/theses/?nr=1228)

<!--more-->

#### Abstract

A global approach to the problem of model-based control of fast parallel robots is proposed in this work. Fundamental differences between the well-known serial arms and parallel manipulators are first explained. A formalism inspired form Denavit-Hartenberg's makes it possible to parameterise any parallel manipulator by handling it as two tree robots connected through six standard links.

Then, it is shown that kinematics and dynamics modelling is greatly simplified when the robot's state is represented both by the variables associated to the actuated joints and the variables specifying the end effector's position in operational space. The inverse dynamics model of any parallel manipulator ran then be put under a standard form called 1n the two spaces".

A Newton-Euler based algorithm is proposed for the real-time computation of the model in the two spaces Its complexity is shown not to be much larger than for serial arms. Through Lagrangian mechanics, the model in the two spaces allows analysis of the robot's dynamics properties, such as passivity. These properties are shown to be equivalent to those of serial arms, except that parallel robots offer good performances only in a restricted workspace in which their Jacobian matrix remains bounded.

Various control strategies for the trajectory-tracking problem for fast robots are then examined. The advantages of model-based approaches combined with robust feedback laws in operational space are described. It is shown that a control loop in operational space requires less computations than in joint space for a parallel robot. Moreover, such a scheme can be very efficiently be implemented on a multiprocessor control unit that exploits the intrinsically parallel and pipeline structure of the required algorithms.

Finally, the proposed approach is applied to the Delta parallel manipulator. A systematic approach leads to the kinematics and dynamics models of this robot, which are expressed under a very compact form. The analysis of the Delta's Jacobian matrix as well as some simulation results reveal the advantages and weak points of this manipulator. The implementation of a model-based control law for the Delta on a control unit with four Transputers is described. Some results obtained on a Delta with a crank belt reduction are presented and discussed.
