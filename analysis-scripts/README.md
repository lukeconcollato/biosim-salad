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

### Phase 1: Foundation & Setup (Weeks 1-2)

#### 1.1 BioSim Connection Infrastructure
- [ ] **Script: `biosim_client.py`**
  - Implement REST API client with authentication handling
  - Create connection pooling and retry logic
  - Add comprehensive error handling and logging
  - Functions: `connect()`, `authenticate()`, `health_check()`, `get_server_info()`

- [ ] **Script: `config_manager.py`**
  - Parse and validate BioSim XML configuration files
  - Create configuration templates for different crop combinations
  - Implement parameter validation and constraint checking
  - Functions: `load_config()`, `validate_config()`, `generate_template()`

- [ ] **Script: `websocket_monitor.py`**
  - Establish WebSocket connection for real-time simulation updates
  - Implement event handling for simulation state changes
  - Create data streaming and buffering mechanisms
  - Functions: `connect_websocket()`, `stream_updates()`, `handle_events()`

#### 1.2 Basic Simulation Control
- [ ] **Script: `simulation_controller.py`**
  - Start, stop, pause, and resume simulations
  - Implement tick advancement and state management
  - Create simulation lifecycle management
  - Functions: `start_simulation()`, `advance_tick()`, `get_simulation_state()`, `stop_simulation()`

- [ ] **Script: `module_manager.py`**
  - Interface with BioSim modules (BiomassPS, Environment, CrewGroup)
  - Implement module configuration and parameter updates
  - Create module health monitoring
  - Functions: `get_module_info()`, `update_module_config()`, `monitor_module_health()`

### Phase 2: Polyculture Simulation Framework (Weeks 3-4)

#### 2.1 Crop Combination Generation
- [ ] **Script: `polyculture_generator.py`**
  - Generate all possible crop combinations from 9 available crops
  - Implement weighted selection based on CRL and nutritional value
  - Create area allocation algorithms for optimal space utilization
  - Functions: `generate_combinations()`, `calculate_optimal_ratios()`, `allocate_growing_areas()`

- [ ] **Script: `xml_generator.py`**
  - Dynamically generate BioSim XML configurations for each polyculture
  - Implement parameter optimization for light, water, and nutrient profiles
  - Create validation and testing for generated configurations
  - Functions: `generate_crop_xml()`, `optimize_parameters()`, `validate_xml()`

#### 2.2 Parallel Simulation Execution
- [ ] **Script: `simulation_runner.py`**
  - Execute multiple simulations in parallel with unique IDs
  - Implement resource management and load balancing
  - Create simulation queue and priority management
  - Functions: `run_parallel_simulations()`, `manage_simulation_queue()`, `balance_resources()`

- [ ] **Script: `stress_testing.py`**
  - Implement environmental stress testing via malfunction API
  - Create failure scenario generation (power outages, equipment failures)
  - Test system resilience and recovery capabilities
  - Functions: `generate_failure_scenarios()`, `inject_malfunctions()`, `test_recovery()`

#### 2.3 Dynamic System Management
- [ ] **Script: `area_allocator.py`**
  - Dynamically adjust crop area allocation based on performance
  - Implement real-time optimization during simulation
  - Create adaptive growing area management
  - Functions: `optimize_area_allocation()`, `adjust_crop_ratios()`, `monitor_space_utilization()`

### Phase 3: Data Collection & Analysis (Weeks 5-7)

#### 3.1 Long-Duration Simulation Execution
- [ ] **Script: `long_run_manager.py`**
  - Execute simulations for 500+ ticks with monitoring
  - Implement checkpoint and recovery mechanisms
  - Create progress tracking and status reporting
  - Functions: `run_long_simulation()`, `create_checkpoint()`, `resume_from_checkpoint()`

- [ ] **Script: `data_collector.py`**
  - Collect comprehensive sensor data across all crop combinations
  - Implement real-time data streaming and storage
  - Create data validation and quality assurance
  - Functions: `collect_sensor_data()`, `stream_data()`, `validate_data_quality()`

#### 3.2 Biomass and Resource Analysis
- [ ] **Script: `biomass_analyzer.py`**
  - Analyze crop performance metrics (yield, growth rate, efficiency)
  - Calculate oxygen generation and CO₂ consumption rates
  - Implement comparative analysis across polyculture combinations
  - Functions: `analyze_crop_performance()`, `calculate_oxygen_production()`, `compare_polycultures()`

- [ ] **Script: `resource_optimizer.py`**
  - Analyze water, power, and nutrient consumption patterns
  - Identify optimal resource allocation strategies
  - Calculate efficiency metrics and waste reduction
  - Functions: `analyze_resource_usage()`, `optimize_consumption()`, `calculate_efficiency()`

#### 3.3 Crew and System Monitoring
- [ ] **Script: `crew_monitor.py`**
  - Monitor crew resource consumption and well-being metrics
  - Track nutritional intake and health indicators
  - Analyze crew productivity and satisfaction levels
  - Functions: `monitor_crew_health()`, `track_nutrition()`, `analyze_productivity()`

- [ ] **Script: `system_stability_analyzer.py`**
  - Monitor overall system stability and resilience
  - Track system performance under various conditions
  - Identify potential failure points and bottlenecks
  - Functions: `monitor_system_stability()`, `identify_bottlenecks()`, `assess_resilience()`

### Phase 4: Optimization & Validation (Weeks 8-10)

#### 4.1 Results Analysis and Optimization
- [ ] **Script: `results_analyzer.py`**
  - Comprehensive analysis of all simulation results
  - Statistical analysis and significance testing
  - Generate performance rankings and recommendations
  - Functions: `analyze_all_results()`, `perform_statistical_tests()`, `generate_rankings()`

- [ ] **Script: `optimization_engine.py`**
  - Refine crop ratios based on simulation results
  - Implement machine learning for parameter optimization
  - Create iterative improvement algorithms
  - Functions: `optimize_crop_ratios()`, `ml_parameter_optimization()`, `iterative_improvement()`

#### 4.2 Resilience and Failure Testing
- [ ] **Script: `resilience_tester.py`**
  - Test system resilience under various failure conditions
  - Implement comprehensive stress testing scenarios
  - Analyze recovery time and system robustness
  - Functions: `test_system_resilience()`, `run_stress_tests()`, `analyze_recovery()`

- [ ] **Script: `failure_analysis.py`**
  - Analyze failure modes and their impact on polyculture systems
  - Identify critical failure points and mitigation strategies
  - Generate failure prevention recommendations
  - Functions: `analyze_failure_modes()`, `identify_critical_points()`, `generate_mitigation_strategies()`

#### 4.3 Validation and Reporting
- [ ] **Script: `terrestrial_validator.py`**
  - Validate results against known terrestrial polyculture data
  - Compare space simulation results with Earth-based studies
  - Identify discrepancies and potential causes
  - Functions: `validate_against_terrestrial_data()`, `compare_results()`, `identify_discrepancies()`

- [ ] **Script: `report_generator.py`**
  - Generate comprehensive research reports and recommendations
  - Create visualizations and data summaries
  - Produce mission planning recommendations
  - Functions: `generate_research_report()`, `create_visualizations()`, `produce_recommendations()`

### Phase 5: Advanced Analysis and Publication (Weeks 11-12)

#### 5.1 Advanced Statistical Analysis
- [ ] **Script: `statistical_analyzer.py`**
  - Perform advanced statistical analysis (ANOVA, regression, correlation)
  - Implement time series analysis for long-duration simulations
  - Create predictive models for polyculture performance
  - Functions: `advanced_statistical_analysis()`, `time_series_analysis()`, `create_predictive_models()`

- [ ] **Script: `visualization_engine.py`**
  - Create comprehensive data visualizations and dashboards
  - Generate publication-ready figures and charts
  - Implement interactive visualization tools
  - Functions: `create_dashboards()`, `generate_publication_figures()`, `build_interactive_tools()`

#### 5.2 Documentation and Reproducibility
- [ ] **Script: `experiment_recorder.py`**
  - Record all experimental parameters and configurations
  - Create reproducible experiment documentation
  - Generate metadata for all simulations
  - Functions: `record_experiment_parameters()`, `create_reproducible_docs()`, `generate_metadata()`

- [ ] **Script: `data_publisher.py`**
  - Prepare data for publication and sharing
  - Create standardized data formats
  - Generate data dictionaries and documentation
  - Functions: `prepare_publication_data()`, `standardize_formats()`, `create_data_dictionaries()`

## Script Dependencies and Workflow

### Core Dependencies
```
biosim_client.py (foundation)
├── config_manager.py
├── websocket_monitor.py
└── simulation_controller.py
    ├── module_manager.py
    └── simulation_runner.py
        ├── polyculture_generator.py
        ├── xml_generator.py
        └── area_allocator.py
```

### Data Flow Pipeline
```
1. Configuration → polyculture_generator.py → xml_generator.py
2. XML Config → simulation_runner.py → long_run_manager.py
3. Simulation → data_collector.py → experiment_recorder.py
4. Raw Data → biomass_analyzer.py, resource_optimizer.py, crew_monitor.py
5. Analysis → results_analyzer.py → optimization_engine.py
6. Results → report_generator.py → visualization_engine.py
```

### Critical Script Interactions
- **`biosim_client.py`** provides the foundation for all API interactions
- **`polyculture_generator.py`** creates crop combinations that feed into **`xml_generator.py`**
- **`simulation_runner.py`** orchestrates parallel execution using **`long_run_manager.py`**
- **`data_collector.py`** streams data to multiple analysis scripts simultaneously
- **`results_analyzer.py`** aggregates outputs from all analysis scripts
- **`optimization_engine.py`** uses results to refine parameters for iterative improvement

### Parallel Execution Strategy
- **Phase 1-2**: Sequential development of core infrastructure
- **Phase 3**: Parallel execution of multiple polyculture simulations
- **Phase 4**: Parallel analysis of different data streams
- **Phase 5**: Parallel generation of reports and visualizations

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
│   ├── environmental_params.json # Environmental stress test parameters
│   └── templates/              # Configuration templates
│       ├── base_simulation.xml # Base simulation template
│       ├── crop_configs/       # Individual crop configurations
│       └── stress_scenarios/   # Failure scenario templates
├── src/                         # Python source code
│   ├── core/                   # Core infrastructure scripts
│   │   ├── biosim_client.py    # BioSim REST API client
│   │   ├── config_manager.py   # Configuration management
│   │   ├── websocket_monitor.py # Real-time monitoring
│   │   └── simulation_controller.py # Basic simulation control
│   ├── simulation/             # Simulation execution scripts
│   │   ├── simulation_runner.py # Parallel simulation execution
│   │   ├── long_run_manager.py # Long-duration simulation management
│   │   ├── module_manager.py   # BioSim module interface
│   │   └── stress_testing.py   # Environmental stress testing
│   ├── polyculture/            # Polyculture-specific scripts
│   │   ├── polyculture_generator.py # Crop combination algorithms
│   │   ├── xml_generator.py    # XML configuration builder
│   │   └── area_allocator.py   # Dynamic area allocation
│   ├── data/                   # Data collection and management
│   │   ├── data_collector.py   # Data logging and collection
│   │   ├── experiment_recorder.py # Experiment documentation
│   │   └── data_publisher.py   # Data preparation for publication
│   ├── analysis/               # Data analysis tools
│   │   ├── biomass_analyzer.py # Crop performance analysis
│   │   ├── resource_optimizer.py # Resource usage optimization
│   │   ├── crew_monitor.py     # Crew health and nutrition monitoring
│   │   ├── system_stability_analyzer.py # System stability analysis
│   │   ├── results_analyzer.py # Comprehensive results analysis
│   │   ├── optimization_engine.py # Parameter optimization
│   │   ├── resilience_tester.py # System resilience testing
│   │   ├── failure_analysis.py # Failure mode analysis
│   │   ├── terrestrial_validator.py # Validation against Earth data
│   │   ├── statistical_analyzer.py # Advanced statistical analysis
│   │   └── report_generator.py # Report generation
│   └── visualization/          # Visualization tools
│       ├── visualization_engine.py # Data visualization
│       └── dashboard_builder.py # Interactive dashboards
├── data/                        # Simulation output data
│   ├── raw/                    # Raw API responses
│   │   ├── simulations/        # Individual simulation data
│   │   ├── sensors/            # Sensor readings
│   │   └── logs/               # Simulation logs
│   ├── processed/              # Cleaned and structured data
│   │   ├── biomass/            # Crop performance data
│   │   ├── resources/          # Resource consumption data
│   │   ├── crew/               # Crew health data
│   │   └── system/             # System stability data
│   └── metadata/               # Data dictionaries and documentation
├── results/                     # Analysis results and visualizations
│   ├── reports/                # Generated research reports
│   ├── figures/                # Publication-ready figures
│   ├── dashboards/             # Interactive dashboards
│   └── recommendations/        # Mission planning recommendations
├── tests/                       # Unit tests and validation
│   ├── unit/                   # Unit tests for individual scripts
│   ├── integration/            # Integration tests
│   └── validation/             # Data validation tests
└── docs/                        # Additional documentation
    ├── api_reference.md         # API usage documentation
    ├── troubleshooting.md      # Common issues and solutions
    └── examples/               # Usage examples and tutorials
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