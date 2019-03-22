# GNS3 Lab1 - Junos and Arista

## Short description
This lab simulate 1 compagny with 2 hub site and 4 branches. 1 vEOS switch is simultating the internet to connect hub and branches. There is a direct link between the 2 DC.
The focus of this lab is the Juniper SRXs. Arista is use to simulate the other parts of the networks (no previous experience with Arista). 

This document explain the view of what will look like the LAB at the end of this cours.
The goal of the first exercise will be explain in the Exercices section

## Topology
### DC
The core network for each DC is simulating by vEOS device call C1-DCX-R3. The core network has two main path toward internet or other site:
Path1: 
C1-DCX-R3 <-> C1-DCX-FW01 <-> C1-DCX-R1 <-> Internet-1
C1-DCX-R3 <-> C1-DCX-FW01 <-> C1-DCX-R1 <-> Internet-2
Path2:
C1-DCX-R3 <-> C1-DCX-FW02 <-> C1-DCX-R2 <-> MPLS-1

At the moment nothing else is connected to the vEOS that is simulating the core network.

### Branches
There is 4 branches. Each branch has it's own vSRX but share one vEOS for the Branch router connecting to Internet and one shared vEOS for the Router behind the vSRX simulating the Branch network.

Branch connection from the local network to the Internet:
C1-BR-R2 <-> C1-BR01-FW01 <-> C1-BR-R1 <-> MPLS or internet or both.
