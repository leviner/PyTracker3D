# Vision

Fish track reconstruction from single target detections is expanding as a common processing technique to explore basic behavioral characteristics of organisms.  As split-beam transducer and echosounder packages become available as moored systems, large volume high resolution datasets are becoming increasingly available for analysis.  To investigate long-term temporal trends in track characteristics, computer-assisted classification of fish behavior in acoustically observed fish tracks becomes a greater necessity.

We are working with EK80 multifrequency split-beam systems deployed as upward facing echosounders on the seabed for periods of 3 to 24 months.  These high volume datasets pair with oceanographic environmental observations of an equivalent time series.  Grouping and identification of behavior will allow for association of common track traits with changes in environmental conditions.

# Objectives
- Develop framework for machine learning assisted grouping of fish tracks based on predetermined track and target characteristics.
- Create readability and data structure for the import and management of reconstructed fish paths (linked single target detections).
- Produce an open-source toolkit that can be integrated with concurrently developed python-based acoustic data processing suites.

## Data Description
Large volume datasets are available to use for development.  Original data is available in the form of Simrad (Kongsberg Maritime AS) `.raw` files.  Post-processed data is in the format of reconstructed fish paths.

Preliminary objectives are based on the use of reconstructed fish paths, where additional processing for classification requires a subset of criteria derived from those tracks (i.e., speed, angle, neighbor distances).  Development of methods for input of target detections will allow for flexibility and future applications in 3-dimensional optical data sets and animal tag recordings.

### Initial Dataset
- Track Reconstruction:
  - Data was collected with stationary WBAT placement on a fixed dock, with a calibration sphere at ~6m distance moved horizontally through the insonified volume in intervals of 8 - 10 cm.
- Fish Behavior Classification
  - 2017-Present WBAT NE Chukchi Sea, AK (24 months, 2h duty-cycle)

### Available Data
- 2015 Shelikof, AK 3-mooring Array (3 months, 3h duty-cycle)
- 2016 Shumagins, AK 3-mooring Array (5 months, 3h duty-cycle)
- OOI RSN EK60

# Success Criteria
Success criteria will be based on increased resolution of track identification, from single track metrics to behavior identification.

- Identification of standard track metrics by priority/simplicity:
  1. Vertical location
  2. Swim speed
  3. Swim angle
  4. Neighbor distances
  5. Neighbor orientation
- Clustering by track metrics
- Identification of clustered behaviors

# Communication Strategies
- Github
- Reporting of methods and findings of application within fisheries acoustics community

# Deliverable Schedule
By Academic Quarter
- Summer 2018
  - Track import tool is available
  - Track metric tool is available
- Fall 2018
  -  Metric classification tool is available
- Winter 2019
  - Training set of expected components is constructed from 2015 and 2017 instrument deployments

# Minimum Products
The development of python-based tools for:
1. Extraction of track metrics from reconstructed paths (i.e., speed, swim angle, neighbor distances, etc.)
2. Component clustering of reconstructed fish tracks based on track metrics
3. Live estimation of behavior from split-beam data streams

# StakeHolders
- Users of high-resolution acoustic datasets with varying temporal resolution (moored systems, buoys, node-based systems, stationary vessel observations).
- Behavioral ecologists working with 3-dimensional data recordings of animal movement.
