# Polyculture Crop Systems for Space Life Support via Simulation

## Research Overview

This project investigates the effects of polycultural crops on advanced life support systems using BioSim, an integrated simulation platform developed at NASA's Johnson Space Center. The research aims to explore how genetically diverse crop combinations can enhance plant nutrition, increase total yield, improve system stability, and reduce crop failure risk in spaceflight environments.

## Research Objectives

### Primary Objectives
1. **Investigate Polyculture Interactions**: Explore interactions between high Crop Readiness Level (CRL) plants in controlled space environments
2. **Optimize Life Support Systems**: Determine optimal crop combinations for nutrition, crew well-being, and oxygen/CO₂ cycling
3. **Enhance System Stability**: Identify polyculture configurations that improve overall Bioregenerative Life Support System (BLSS) resilience
4. **Validate Earth-Based Knowledge**: Test terrestrial polyculture success in spaceflight simulation environments

### Technical Objectives
1. **Simulation Framework Development**: Create Python scripts to interface with BioSim's RESTful API
2. **Parallel Simulation Execution**: Implement iterative simulations of different polyculture combinations
3. **Data Collection & Analysis**: Log simulation outputs over extended periods (500+ ticks) with customizable sensors
4. **Parameter Optimization**: Determine compatible light, water, and nutrient profiles for optimal crop output

## BioSim API Integration

### Core Endpoints

#### Simulation Management
- `GET /api/simulation` - List all active simulations
- `POST /api/simulation/start` - Start new simulation with XML configuration
- `POST /api/simulation/{simID}/tick` - Advance simulation by one tick
- `GET /api/simulation/{simID}` - Get complete simulation details
- `GET /api/simulation/{simID}/globals` - Get global simulation properties
- `GET /api/simulation/{simID}/log` - Retrieve complete run log with tick data

#### Module Control
- `GET /api/simulation/{simID}/modules/{moduleName}` - Get detailed module information
- `POST /api/simulation/{simID}/modules/{moduleName}/consumers/{type}` - Update consumer definitions
- `POST /api/simulation/{simID}/modules/{moduleName}/producers/{type}` - Update producer definitions

#### Malfunction Management
- `POST /api/simulation/{simID}/modules/{moduleName}/malfunctions` - Schedule/start malfunctions
- `GET /api/simulation/{simID}/modules/{moduleName}/malfunctions` - Get module malfunctions
- `DELETE /api/simulation/{simID}/modules/{moduleName}/malfunctions/{malfunctionID}` - Clear specific malfunction
- `DELETE /api/simulation/{simID}/modules/{moduleName}/malfunctions` - Clear all malfunctions

#### Real-time Updates
- `WS /ws/simulation/{simID}` - WebSocket connection for real-time simulation updates

### Key Data Structures

#### Biomass Production System (BiomassPS)
- **Shelves**: Array of growing areas with crop-specific data
  - `plantType`: Crop type identifier
  - `cropAreaUsed` / `cropAreaTotal`: Area utilization metrics
  - `timeTillCanopyClosure`: Growth stage timing
  - `harvestInterval`: Harvest frequency
  - `ppfNeeded`: Photosynthetic photon flux requirements
  - `molesOfCO2Inhaled`: CO₂ consumption rate

#### Environment (SimEnvironment)
- **Atmospheric Conditions**:
  - `temperature`, `temperatureInKelvin`, `relativeHumidity`
  - `lightIntensity`, `maxLumens`, `dayLength`, `hourOfDayStart`
  - `totalPressure`, `totalMoles`, `leakRate`
- **Gas Stores**:
  - `o2Moles`, `co2Moles`, `nitrogenMoles`, `otherMoles`, `vaporMoles`
- **Volume Control**: `currentVolume`, `initialVolume`, `airLockVolume`

#### Crew System (CrewGroup)
- **Individual Metrics**:
  - `O2Consumed`, `CO2Produced`, `caloriesConsumed`
  - `potableWaterConsumed`, `dirtyWaterProduced`, `greyWaterProduced`
- **Activity Management**: Current activity, schedule, intensity levels

#### Sensors & Actuators
- **Sensors**: Value monitoring with configurable alarm thresholds (WATCH, WARNING, DISTRESS, CRITICAL, SEVERE)
- **Actuators**: Flow rate control with min/max limits and output module connections

### Flow Rate Control
- **Consumer/Producer Definitions**: Configurable flow rates for resources
- **Connection Management**: Dynamic linking between modules
- **Rate Arrays**: `maxFlowRates`, `desiredFlowRates`, `actualFlowRates`, `initialFlowRates`

## Research Milestones

### Phase 1: Foundation & Setup
- [ ] Establish BioSim connection and authentication
- [ ] Create basic simulation control scripts using REST API
- [ ] Implement XML configuration parsing for crop parameters
- [ ] Set up WebSocket connection for real-time monitoring

### Phase 2: Polyculture Simulation Framework
- [ ] Develop crop combination generation algorithms
- [ ] Create parallel simulation execution system
- [ ] Implement environmental stress testing via malfunction API
- [ ] Build dynamic crop area allocation system

### Phase 3: Data Collection & Analysis
- [ ] Execute long-duration simulations (500+ ticks)
- [ ] Collect comprehensive sensor data across all crop combinations
- [ ] Analyze biomass production, oxygen generation, and system stability
- [ ] Monitor crew resource consumption and well-being metrics

### Phase 4: Optimization & Validation
- [ ] Refine crop ratios based on simulation results
- [ ] Test system resilience under various failure conditions
- [ ] Validate results against known terrestrial polyculture data
- [ ] Generate recommendations for space mission planning

## Technical Requirements

### BioSim Integration
- **Java-based simulation platform** with RESTful API (Javalin framework)
- **XML Configuration**: Crop selection, area allocation, environmental parameters
- **Nine crop types** with unique properties and growth characteristics
- **Controllable stochastic intensity** and system malfunctions
- **Real-time WebSocket updates** for live monitoring

### Python Scripts Development
- **RESTful API communication** with BioSim server
- **Parallel simulation execution** with unique simulation IDs
- **Customizable sensor logging** with alarm threshold monitoring
- **Data collection and storage** in structured format
- **Analysis and visualization tools** for polyculture performance

### Key Parameters to Study
- **Crop Selection & Ratios**: Dynamic allocation via consumer/producer definitions
- **Crop Area Allocation**: Shelf-based growing area management
- **Resource Consumption**: Water, power, and CO₂ flow rates
- **Environmental Conditions**: Light intensity, temperature, humidity control
- **System Resilience**: Malfunction testing and recovery analysis

## Expected Outcomes

1. **Optimal Polyculture Configurations**: Identify the best crop combinations for space missions
2. **System Resilience Data**: Understand how polycultures respond to environmental stresses
3. **Resource Optimization**: Determine efficient resource usage patterns
4. **Mission Planning Support**: Provide data-driven recommendations for crew nutrition and life support

## File Structure

```
analysis-scripts/
├── README.md                    # This file
├── config/                      # Configuration files
│   ├── crop_combinations.xml   # XML templates for different polycultures
│   └── environmental_params.json # Environmental stress test parameters
├── src/                         # Python source code
│   ├── biosim_client.py        # BioSim REST API client
│   ├── simulation_runner.py    # Simulation execution engine
│   ├── data_collector.py       # Data logging and collection
│   ├── polyculture_generator.py # Crop combination algorithms
│   ├── xml_generator.py        # XML configuration builder
│   └── analysis/               # Data analysis tools
│       ├── biomass_analyzer.py # Crop performance analysis
│       ├── resource_optimizer.py # Resource usage optimization
│       └── visualization.py    # Results visualization
├── data/                        # Simulation output data
│   ├── raw/                    # Raw API responses
│   └── processed/              # Cleaned and structured data
├── results/                     # Analysis results and visualizations
└── tests/                       # Unit tests and validation
```

## Getting Started

1. **Review BioSim API**: Understand the REST endpoints and data structures
2. **Set up Python environment** with required dependencies (requests, websockets, xml.etree)
3. **Configure BioSim connection** parameters and authentication
4. **Begin with Phase 1 milestones**: Basic API integration and simulation control
5. **Iterate through phases** based on findings and API capabilities

## API Usage Examples

### Starting a Simulation
```python
# POST /api/simulation/start
xml_config = generate_crop_configuration(crop_types, areas, parameters)
response = requests.post(f"{biosim_url}/api/simulation/start", data=xml_config)
sim_id = response.json()["simId"]
```

### Monitoring Biomass Production
```python
# GET /api/simulation/{simID}/modules/BiomassPS
response = requests.get(f"{biosim_url}/api/simulation/{sim_id}/modules/BiomassPS")
biomass_data = response.json()
crop_performance = analyze_shelves(biomass_data["properties"]["shelves"])
```

### Real-time Updates via WebSocket
```python
# WS /ws/simulation/{simID}
websocket.connect(f"{biosim_url}/ws/simulation/{sim_id}")
# Receive real-time updates for live monitoring
```

## Contributing

This research project follows an iterative approach. Each phase builds upon the previous one, with continuous refinement based on simulation results and analysis findings. The BioSim API provides comprehensive control over all aspects of the life support system, enabling detailed investigation of polyculture interactions and system optimization. 