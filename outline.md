---
title: 'Working Paper 19: Model and Measurement of Specific Fuel Consumption on Diesel Microgrids in Lake Sentani, Indonesia'
author: Daniel Soto
figureTitle: Figure
figPrefix: Figure
tblPrefix: Table
---

# Abstract

# Introduction

<!-- p1: main issue: quantifying observed diesel marginal cost  -->

- this paper establishes the observed marginal cost of diesel generation in a remote area
    - least cost assumptions that drive energy allocations are dependent on operating conditions
    - we observe operating conditions that are likely to cause high operating costs
    - we measure operating costs that are well above assumptions and recovery tariffs

<!-- p2: context, motivation, need: keeping indonesia on track -->

- indonesia is executing a large electrification expansion to achieve universal access (ADB paper)
    - Indonesia has made progress on percent with electricity access over the last decades (ADB?)
    - we want to simultaneously expand access, lower cost and lower carbon intensity
    - the archipelago however presents challenges and there are wide differences in the electrification rate
    - This assumption would be threatened by oversized generators.
    - Observations of marginal cost can inform future allocations in Indonesia and beyond.
    <!-- is diesel the dominant technology in Indonesia?  (ADB)  -->
    <!-- at what time were these grids installed? -->

<!-- p3: lit search shows this study fills a data and analysis gap -->

- least cost electrification needs data to support its assumptions
    - these establish a range of diesel operating costs to use in future least-cost studies
    - geospatial least cost studies show continuing diesel use as a significant part of the mix (ADB_AUEAII)
    - least cost assumptions are sensitive to operating costs (ADB_AUEAII)
    - A diesel microgrid in Nicaragua runs at well below the generator rating (Casillas_EP)
    - Indonesia diesel plant electricity production flattening out (ESDM)
    - In the case of PV, oversizing leads to higher costs (Louie_ESD, Lee)
    - Grids in Haiti show oversized grids infrequently operated (Schnitzer_Thesis)
    - evidence shows that tariffs are below operating costs in Haiti and that few if any grids are operating (Schnitzer_Thesis)
    - This study adds to the literature by gathering minute-resolution load data

<!-- p4: results -->

- this study provides estimates and observations of the fuel costs for diesel consumption in three indonesian microgrids
    - this work makes two contributions
    - first, an observation of the specific fuel consumption in three microgrids
    - second, a modeled estimate of the specific fuel consumptions for well-maintained generators
    - we find that the generators are providing power well below their intended operating points
    - we estimate that a new generator operating at these low power operating points would have operating costs at 0.60 USD or above
    - we find that the observed specific fuel consumption with an installed generator on one grid is as high as 2 USD per kVA-hour delivered, suggesting significant efficiency degradation

<!-- p5: conclusions -->

- These results suggest diesel microgrids may not be performing to expectations
    - when the generator is run at low loads marginal cost and carbon emissions rise
    - areas with high marginal costs should be identified and mitigated
    - right-sized generators or alternate technologies should be considered for areas with high marginal costs

# Methods

## Data Collection Context

<!-- where and how was the data collected? -->

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
    - We use 9 specification sheets for a generators of similar size from a leading manufacturer
    - These are available in supplemental table {label}
    - All specification sheets report fuel use at 50%, 75%, and 100% of the full load.
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

- TODO: format tables with reasonable numbers of significant figures GT
- TODO: fix order of columns in energy table
- TODO: capitalize village names

## Data Coverage

- We have confidence in the data for 86% to 93% of the observation period for the microgrids
    - The data cover from two to three months in the villages. (@tbl:data_coverage)
    - We have direct time series measurements for 9 to 23 percent of the observation period
    - We have messages indicating the grid going off and back on that bring coverage up to 86 to 93 percent.

TODO: report as percent or change column name to fraction

Table: Data Coverage {#tbl:data_coverage}

{% include './tables/data_coverage.md' %}

<!-- [table label: data_coverage](./tables/data_coverage.md) -->

## Microgrid Uptime

- Our data show the total duration of operation each day (@fig:uptime_CDF)
    - The figure shows that two grids don't operate at on 15% of the days and another on 35% of the days.
    - The Atamali provides between 5 and 7 hours 75% of the observed days
    - The Ayapo grid provides between 4 and 7 hours on about 75% of the observed days
    - The Kensio microgrid, however, shows very few days with more than 5 hours of service.
    - These data are consistent with the evening-only operation and also show some days with less service.

![Cumulative distribution function of Uptime](./plots/uptime_CDF.png){#fig:uptime_CDF}

## Electricity Energy Consumption

- We report on the daily electricity energy consumption for days the grid is operating
    - we define operation as a day where there is any non-zero energy reported
    - on operating days @tbl:daily_operating_energy shows that total energy delivered is 9, 15, and 90 kWh per day.
    - the average energy use on days of operation per connected household is between 0.4 and 0.9 kWh per day
    - the cumulative distribution function (@fig:daily_energy_CDF} shows that the electricity most days is clustered around the mean but there is a low energy tail
    - these daily energy totals were used to calculate the observed specific fuel consumption

![Daily Energy Cumulative Distribution Function](./plots/daily_energy_CDF.png){#fig:daily_energy_CDF}

Table: Mean Energy Delivered During Grid Operation {#tbl:daily_operating_energy}

{% include './tables/daily_operating_energy.md' %}

<!-- [table label: daily_operating_energy](./tables/daily_operating_energy.md) -->


## Power Consumption

- TODO: decide on whether the power CDF should include zeros

- We report on the apparent power consumption in these microgrids during these times of operation
    - The @tbl:genset_utilization shows the mean loads during operation of the microgrids are well below the operating points of the generators
    - The most well-matched microgrid is operating at 32% of the rated load and one grid is only at 6% of the generators rated load.
    - These means do not include the periods of zero power since the generators don't run during these periods and fuel isn't consumed

![Power Cumulative Distribution Function](./plots/power-CDF.png){#fig:power-CDF}

![Power Cumulative Distribution Function](./plots/power-CDF-no-zeros.png){#fig:power-CDF-no-zeros.png}

Table: Generator Utilization {#tbl:genset_utilization}

{% include './tables/genset_utilization.md' %}

<!-- [table label: genset_utilization](./tables/genset_utilization.md) -->


## Microgrid Marginal Cost

- I model the specific fuel consumption in liters per kWh for a hypothetical well-maintained generator operating at the manufacturers specifications at the fraction of load we observe
    - The generators range in size from 25 kVA to 40 kVA
    - Our fit to the generator specifications has a slope of 0.270 lph per kVA of load
    - The fit has a slope of 0.059 lph per kVA of rated power
    - Figure {which label?} shows the modeled specific fuel consumption.
    - In practice, we expect wear and tear to reduce the efficiency of the generator.

- Since we have the time series observations of kVA we can model a duration curve for the specific fuel consumption.
    - report CDFs of specific fuel
    - The modeled specific fuel consumption at 100% load range from 0.287 to 0.302 liters per kVA-hour
    - The modeled specific fuel consumption at the rated load range from 0.361 to 0.681 liters per kVA-hour

Table: Modeled Specific Fuel Consumption {#tbl:modeled_SFC}

{% include './tables/modeled_SFC.md' %}

<!-- [table label: modeled_SFC](./tables/modeled_SFC.md) -->

- I also report an observed specific fuel consumption based on the generator operators daily fuel logs and the observed daily energy use
    - Observations of fuel consumption are from operator reports
    - Atamali reports 30 liters per night for its 25 kVA genset to deliver 15 kWh
    - This results in a specific fuel consumption of 2 liters per kWh.
    - Ayapo reports 60 liters per night for its 40 kVA genset to deliver 85 kWh
    - This is a specific fuel consumption of 710 ml per kWh, well above predicted.
    - At 1 USD per liter for diesel, this is a marginal cost of 0.70 USD and 2 USD per kWh

Table: Observed Specific Fuel Consumption {#tbl:observed_SFC}

{% include './tables/observed_SFC.md' %}

<!-- [table label: observed_SFC](./tables/observed_SFC.md) -->

<!-- ![](./plots/specific_fuel_consumption_duration.png) -->

# Discussion

## Inefficient Operation Leads to Poorer Service

- Operating a diesel generator at a power load well below its designed operating point leads to inefficient operation.
    - operating at low load increases engine maintenance requirements and worsens fuel costs (cite diesel lit or schnitzer)
    - This inefficiency increases fuel cost per unit of energy generated.
    - This operation could increase wear and tear on the generator, increasing maintenance costs and downtime.
    - These drive up operating costs through increased fuel consumption.
    - To conserve fuel, many microgrids are only operated in the evenings. (cite Schnitzer?, casillas)
    - Our observations adhere to this prediction of higher SFC
    - The observed fuel costs are well above modeled fuel costs suggesting generator maintenance issues
    - These SFC costs also restrict generator operation to evenings
    - it is likely uneconomical to run these generators continuously but unnecessarily high marginal costs worsen the problem
    - The village nominally has been electrified but has an expensive and intermittent electricity service.

## Insufficient Cost Recovery

- Observed fuel costs are well above tariff collection requiring subsidy
    - Customers pay 5 cents or less per kWh and many meters don't function
    - The electricity is almost completely subsidized
    - The operating costs are well above the tariffs
    - This subsidized operation is found in other grids (cite)

## Least Cost Model Assumptions

- These observed fuel costs are likely higher than those in least-cost models for electricity planning
    - If the observed costs are above another option, least-cost planning hasn't been achieved
    - The $2 per kVA is likely above the levelized cost for solar PV with battery storage
    - Using the Lazard LCOE and LCOS studies we can create a composite estimate of 1.03 -- 1.70 USD per kWh for PV and storage. {cite Lazard_LCOE, Lazard_LCOS}
    - While this is a high LCOE it is below the observed fuel cost for one of the villages and invites us to reconsider the least cost assumptions.

## Capital vs Operating Costs

- diesel generators are attractive because they are affordable to purchase and install
    - Diesel is the least cost option from a capital perspective
    - if the cost of maintenance and operation isn't priced, they will be installed in cases where they are not the least cost option (jaramillo?)

## Carbon Impact

- High specific fuel consumption means high carbon intensity of electricity
    - under ideal conditions an efficient diesel generator has comparable cost and carbon intensity compared to existing fossil sources
    - diesel cost and carbon intensity can match or greatly exceed coal and NG averages
    - TODO: calculate the carbon intensity for each generator and compare to coal and others

## Potential Improvements

- These problems of high marginal costs and insufficient tariff recovery suggest that other approaches could provide better service at a lower cost.
    - Revisiting the least cost assumptions in actual operation may lead to different generation allocation decisions

- Matching generators to loads could improve SFC and operating costs
    - A smaller generator operating at 75% load would provide X improvement
    - Running the generator at this 75% load could slow degradation and SFC increases
    - at $400 per kW, $1 per liter, and 300 ml/kWh, fuel cost exceeds capital cost after about 1000 hours, making generator replacement feasible (confirm)

- Replacing diesel generation with PV and battery storage could improve levelized cost
    - It is plausible that PV systems with storage can deliver electricity for less than the $2 per kWh that we observe
    - While the levelized cost of a battery and PV system may be lower, the capital investment is much higher.
    - while PV costs rise on a capital basis, diesel costs rise on a marginal basis
    - To move to a least cost option from a total cost perspective may require new ways to access capital.

