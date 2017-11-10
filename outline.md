---
title: 'Working Paper 19: Model and Measurement of Specific Fuel Consumption on Diesel Microgrids in Lake Sentani, Indonesia'
author: Daniel Soto
figureTitle: Figure
figPrefix: Figure
tblPrefix: Table
---

# Abstract

- topic: energy access, cost of electricity
- problem being addressed: marginal cost of diesel
- gap: little direct measurement?  nothing in indonesia?
- approach: accurate energy monitoring and fuel refill logs
- result: we observe reasonable to unacceptable SFC
- key impact: we should revisit load factor and least cost assumptions going forward

# Introduction

- Electrification of the remaining 1.2 billion people without access requires close attention to operating costs.
    - Areas beyond the grid require decentralized solutions that can be more costly both to install and to maintain.
    - Indonesia is executing a large electrification expansion to achieve universal access [@ADB_AUEAII]
    - Indonesia has made progress on percentage of households with electricity access over the last decades [@ADB_AUEAII]
    - The archipelago however presents challenges and there are wide differences in the electrification rate [@no_cite_yet]
    - Diesel electricity generation with internal-combustion engines is an important source of decentralized energy.
    - Geospatial least cost studies and Indonesian planning documents show continuing diesel use as a significant part of the mix [@ADB_AUEAII; @IEEFA; @RUPTL]
    - Least cost assumptions are sensitive to operating costs [@ADB_AUEAII]
    - To support this effort we must observe the costs and compare to expectations.
    - Observations of marginal cost can inform future allocations in Indonesia and beyond.
    - If the fuel costs are significantly greater than assumptions, the assumptions should be revisited.

- This work adds to previous work that has shown problems with diesel generation by directly modelling and measuring the fuel used per unit of electricity delivered.
    - Work in off-grid generation show that diesel grids are expensive to run and do not operate at all hours.
    - Grids in Haiti show oversized grids infrequently operated [@Schnitzer_Thesis]
    - A diesel microgrid in Nicaragua runs at well below the generator rating [@Casillas_EP]
    - In the case of photovoltaic (PV) electricity, oversizing leads to higher costs [@Louie_ESD]
    - Evidence shows that tariffs are below operating costs in Haiti and that few if any grids are operating since they are not economically viable [@Schnitzer_Thesis]
    - All this evidence strongly suggests that the operating costs for diesel be verified.

- This study provides estimates and observations of the fuel costs for diesel consumption in three Indonesian microgrids
    - This work presents a model and estimate of fuel consumption under low loads and observes the fuel use per unit of energy delivered.
    - We find that the generators are providing power well below their intended operating points
    - The model estimates that a new generator operating at these low power operating points would have operating costs at 0.60 USD per kWh or above
    - Our observations show that the observed specific fuel consumption (SFC) with an installed generator on one grid is as high as 2 USD per kWh delivered, suggesting significant efficiency degradation.

- These results suggest diesel microgrids may not all be performing to expectations.
    - When the generator is run at low loads marginal cost and carbon emissions rise
    - Areas with high marginal costs should be identified and mitigated
    - Right-sized generators or alternate technologies should be considered for areas with high marginal costs
    - Indonesia overall diesel plant electricity production flattening out [@ESDM].
    - The remaining off-grid diesel market should be investigated for efficiency.

# Methods

## Data Collection Context

- We measured the energy and power delivered to 3 villages with diesel microgrids
    - These villages are in the Lake Sentani region of Indonesia
    - These recordings were compiled from late April to July 2015
    - The main supply to each of these villages was fitted with a logging electrical power meter
    - The power meter records the power, voltage, and current.
    - The data is recorded at one-minute intervals.
    - The meter measurements are transmitted to a database over a communication network
    - Accumulated energy is reported in units of kilowatt-hours
    - The apparent power is reported in units of volt-amps

## Data Coverage

- We report the interval of time that is covered by data
    - Since the communication network wasn't fully robust, some gaps in the data exist
    - We receive measurements at regular intervals during grid operation
    - We receive reports when the grid ceases operation and returns
    - We sum these periods of time to report the fraction of time covered by the data record

## Missing data techniques and data integrity

- We synthesize time series data for the times when the grid isn't running
    - During power outages, we insert observations of zero power and energy consumption at the same frequency as the meter observations.
    - There remain times without a measurement or confirmed period of power off
    - We remove anomalies due to data corruption in the record

## Energy consumption analysis

- We report the daily energy use in the microgrid from the accumulated energy timeseries
    - The meter records an energy accumulator that is reported at each timestamp with 1 kWh resolution.
    - To account for gaps we insert zeros during reported downtime as described above.
    - We resample the timeseries onto a one-minute time scale
    - Take the difference between neighboring minutes
    - Samples without valid data are assigned null values that aren't included in sums or means
    - By summing these energy differences over a day, we get the energy consumption.

## Power Consumption Analysis

- We report the power used on the grids from the apparent power timeseries
    - The meter provides the apparent power in kVA averaged over an interval at each time step.
    - These data are reported as a mean power for each time of day and as a load duration curve
    - We construct a cumulative distribution function of the observed apparent power to show the percentage of time that the grid is supplying a given power level.

## Modeled fuel estimation

- We model the cost per kWh of generation on these microgrids assuming the generators perform according to the datasheets for the observed loads.
    - We use nice specification sheets for generators of similar size from three manufacturers.
    - All specification sheets report fuel use in liters per kWh while delivering power equal to 50%, 75%, and 100% of the rated load.
    - Some sheets also specify fuel use at 25% of the full load.
    - We assume a linear relationship between fuel use and generator load as well as fuel use and the rated generator size.
    - I create a dataset of the expected fuel consumption for several generators as a function of the delivered load and maximum power output.
    - I perform a regression on this data set to create a linear model of fuel use as a function of delivered load and maximum power output.
    - This model is used to extrapolate the fuel use for loads below the specified range.
    - We divide the fuel rate by the apparent power to get the instantaneous specific fuel consumption

## Observed fuel use

- We estimate the per kWh cost of generation in real-world conditions from the delivered energy and the reported fuel use.
    - Logs are kept of fuel input to the generator on a nightly basis.
    - We divide the mean fuel per night as reported in the written log with the mean generation per night to get the overall specific fuel consumption

# Results


## Data Coverage

- We have direct or indirect data for 86% to 93% of the observation period on these microgrids
    - The data cover from two to three months in the villages. (@tbl:data_coverage)
    - We have direct time series measurements for 9 to 23 percent of the observation period
    - We have messages indicating the grid going off and back on that bring coverage up to 86 to 93 percent.

Table: Data Coverage {#tbl:data_coverage}

{% include './tables/data_coverage.md' %}

## Electricity Energy Consumption

- We report on the daily electricity energy consumption for days the grid is operating
    - We define operation as a day where there is any non-zero energy reported
    - On operating days @tbl:daily_operating_energy shows that total energy delivered is 9, 15, and 90 kWh per day.
    - The average energy use on days of operation per connected household is between 0.4 and 0.9 kWh per day
    - The cumulative distribution function (CDF) in @fig:daily_energy_CDF shows that the electricity most days is clustered around the mean but there is a low energy tail for two villages
    - These daily energy totals were used to calculate the observed specific fuel consumption

![Daily Energy Cumulative Distribution Function](./plots/daily_energy_CDF.png){#fig:daily_energy_CDF}

Table: Mean Energy Delivered During Grid Operation {#tbl:daily_operating_energy}

{% include './tables/daily_operating_energy.md' %}


## Power Consumption

- We report on the apparent power consumption in these microgrids during these times of operation
    - The @tbl:genset_utilization shows the mean loads during operation of the microgrids are well below the operating points of the generators
    - The most well-matched microgrid is operating at 32% of the rated load and one grid is only at 6% of the generators rated load.
    - These means do not include the periods of zero power since the generators don't run during these periods and fuel isn't consumed

![Power Cumulative Distribution Function](./plots/power-CDF.png){#fig:power-CDF}

<!-- ![Power Cumulative Distribution Function](./plots/power&#45;CDF&#45;no&#45;zeros.png){#fig:power&#45;CDF&#45;no&#45;zeros.png} -->

Table: Generator Utilization {#tbl:genset_utilization}

{% include './tables/genset_utilization.md' %}

## Microgrid Marginal Cost

- I model the specific fuel consumption in liters per kWh for a hypothetical well-maintained generator operating at the manufacturers specifications at the fraction of load we observe
    - The generators range in size from 25 kVA to 40 kVA
    - Our fit to the generator specifications has a slope of 0.270 lph per kVA of load
    - The fit has a slope of 0.059 lph per kVA of rated power
    - Table @tbl:modeled_SFC shows the modeled specific fuel consumption.
    - In practice, we expect wear and tear to reduce the efficiency of the generator and increase the SFC.

- Since we have the time series observations of kVA we can model a duration curve for the specific fuel consumption.
    - The modeled specific fuel consumption at 100% load range from 0.287 to 0.302 liters per kVA-hour
    - The modeled specific fuel consumption at the rated load range from 0.361 to 0.681 liters per kVA-hour

Table: Modeled Specific Fuel Consumption {#tbl:modeled_SFC}

{% include './tables/modeled_SFC.md' %}

- I also report an observed specific fuel consumption based on the generator operators daily fuel logs and the observed daily energy use
    - Atamali reports 30 liters per night for its 25 kVA genset to deliver 15 kWh
    - This results in a specific fuel consumption of 2 liters per kWh.
    - Ayapo reports 60 liters per night for its 40 kVA genset to deliver 85 kWh
    - This is a specific fuel consumption of 710 ml per kWh, well above predicted.
    - At 1 USD per liter for diesel, this is a marginal cost of 0.70 and 2 USD per kWh

Table: Observed Specific Fuel Consumption {#tbl:observed_SFC}

{% include './tables/observed_SFC.md' %}

# Discussion

## Diesel and Least Cost Assumptions

- Diesel generators are attractive because they are affordable to purchase and install
    - Diesel costs the least to purchase and install per kW among any generation source [@Lazard_LCOE]
    - Because of fuel cost they end up on the high end of levelized cost [@Lazard_LCOE]
    - If the true, observed cost of maintenance and operation isn't priced, they will be installed in cases where they are not the least cost option
    - These results show marginal cost above assumptions.

- Operating a diesel generator at a power load well below its designed operating point leads to inefficient operation.
    - Operating at low load increases engine maintenance requirements and worsens fuel costs [@Schnitzer_Thesis]
    - This inefficiency increases fuel cost per unit of energy generated.
    - This operation could increase wear and tear on the generator, increasing maintenance costs and downtime.
    - These drive up operating costs through increased fuel consumption.
    - To conserve fuel, many microgrids are only operated in the evenings. [@Schnitzer_Thesis,  @Casillas_EP ?]
    - Our observations adhere to this prediction of higher SFC
    - The observed fuel costs are well above modeled fuel costs suggesting generator maintenance issues
    - These SFC costs also restrict generator operation to evenings

- These observed fuel costs are likely higher than the cost assumptions in least-cost models for electricity planning
    - If the observed costs are above another option, least-cost planning hasn't been achieved
    - The $2 per kVA is likely above the levelized cost for solar PV with battery storage
    - Using the Lazard levelized cost of energy (LCOE) and levelized cost of storage LCOS studies we can create a composite estimate of 1.22 -- 1.56 USD per kWh for PV and storage. [@Lazard_LCOE @Lazard_LCOS]
    - While this is a high LCOE it is below the observed fuel cost for one of the villages and invites us to reconsider the least cost assumptions.

## Inefficient Operation and Level of Service

- The observed fuel costs are well above the tariffs charged on the grids requiring subsidy
    - Customers pay 5 cents or less per kWh and many meters don't function (personal communication)
    - This suggests electricity is almost completely subsidized similar to other grids [@Schnitzer_Thesis]
    - While there is insufficient cost recovery even if running efficiently, degraded generators exacerbate this problem.

- Our data show the grids operating only for a portion of the day
    - Figure (@fig:uptime_CDF) shows that two grids don't operate at on 15% of the days and another on 35% of the days.
    - The Atamali provides between 5 and 7 hours 75% of the observed days
    - The Ayapo grid provides between 4 and 7 hours on about 75% of the observed days
    - The Kensio microgrid, however, shows very few days with more than 5 hours of service.
    - These data are consistent with the evening-only operation and also show some days with less service.
    - It is likely uneconomical to run these generators continuously but unnecessarily high marginal costs worsen the problem
    - The village nominally has been electrified but has an expensive and intermittent electricity service.

![Cumulative distribution function of Uptime](./plots/uptime_CDF.png){#fig:uptime_CDF}

## Potential Improvements

- These problems of high marginal costs and insufficient tariff recovery suggest that other approaches could provide better service at a lower cost.
    - Revisiting the least cost assumptions in actual operation may lead to different generation allocation decisions

- Matching generators to loads could improve SFC and operating costs
    - A smaller generator operating at or above 75% of the rated load will bring the SFC within the range of assumptions.
    - Running the generator at this better matched load could slow degradation and SFC increases due to the incomplete combustion (wet stacking) observed at low loads.  [@Hove_Tazvinga]
    - The low initial cost and high fuel cost allow this replacement to pay back quickly.

- Replacing diesel generation with PV and battery storage could improve levelized cost
    - It is plausible that PV systems with storage can deliver electricity for less than the $2 per kWh that we observe
    - While the levelized cost of a battery and PV system may be lower, the capital investment is much higher.
    - While PV costs rise on a capital basis, diesel costs rise on a marginal basis
    - To move to a least cost option from a total cost perspective may require new ways to access capital.

# Bibliography
