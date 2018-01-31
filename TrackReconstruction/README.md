# Vision

Fish track reconstruction is becoming a more desired processing technique necessary to explore behavioral characteristics of organisms.  As split-beam transducer and echosounder packages become available as moored systems, large volume high resolution datasets are becoming increasingly available for analysis.  To investigate long-term temporal trends in animal movement, open-source methods for path reconstruction will increase the availability of such analyses.

# Objectives
- Create readability and data structure for the import and management of reconstructed fish paths (linked single target detections).
- Produce an open-source toolkit that can be integrated with concurrently developed python-based acoustic data processing suites.
- Allow for varying levels of input data to provide availability for alternative "target" recordings (such as optical datasets with 3-diemnsional locations, tag data, etc.)

## Data Description
Large volume datasets are available to use for development at two levels of processing:
1. `.raw` EK60/EK80 data (Kongsberg Maritime AS)
2. Single target detections

Preliminary objectives are based on the use of acoustic single target detections.  Development of methods focused on target detections will allow for flexibility and future applications in 3-dimensional optical data sets and animal tag recordings.  Direct input of unprocessed data will require integration with open-source methods for target detection.

### Initial Dataset
- Track Reconstruction:
  - Data was collected with stationary WBAT placement on a fixed dock, with a calibration sphere at ~6m distance moved horizontally through the insonified volume in intervals of 8 - 10 cm.
- In situ fish track observations for validation:
  - Portions of a dataset collected in the Chukchi Sea (2017-Present WBAT/EK80 NE Chukchi Sea, AK, 24 months, 2h duty-cycle)

### Available Data
- 2015 Shelikof, AK 3-mooring Array (3 months, 3h duty-cycle)
- 2016 Shumagins, AK 3-mooring Arra (5 months, 3h duty-cycle)
- OOI RSN EK60

# Success Criteria
- We are able to parse fish track data.

# Communication Strategies
- Github
- Reporting of methods and findings of application within fisheries acoustics community

# Deliverable Schedule
March 1st, 2018: Framework for reading single target detections in python
May 1st, 2018: Redevelopment of Tracker3D methods in python (basic trajectory reconstruction, spline trajectory)
September 1st, 2018: Single target detection implementation in python

# Minimum Products
1.  Porting of common practice single-target detection algorithms to Python
2. Python toolkit for acoustic fish track reconstruction
3. Python toolkit for multi-sourced track reconstruction

# StakeHolders
- Users of high-resolution acoustic datasets with varying temporal resolution (moored systems, buoys, node-based systems, stationary vessel observations).
- Behavioral ecologists working with 3-dimensional data recordings of animal movement.
