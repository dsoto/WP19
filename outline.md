---
title: Sentani Microgrid Marginal Cost Working Paper
author: Daniel Soto
---

# Key Questions

- What are the observed costs of electrical energy on these microgrids?
- How reliable is the electricity on these microgrids?

# Contributions

- estimations of specific fuel consumption for electricity generation on diesel microgrids

# Possible Titles

- Microgrid Marginal Electricity cost in Lake Sentani, Indonesia
- Measurements of Microgrid Consumption in Lake Sentani, Indonesia
- Microgrid Energy Consumption, Uptime and Load Factor in Lake Sentani, Indonesia

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

<!-- TODO: should this go before or after the energy and power methods? -->
<!-- TODO: what do we do to ensure correct data? -->

- We synthesize time series data for the times when the grid isn't running
    - During power outages, we insert observations of zero power and energy consumption at the same frequency as the meter observations.
    - There remain times without a measurement or confirmed period of power off
    - We remove anomalies due to data corruption in the record

## Energy consumption analysis

<!-- TODO: what is the right level of detail to report here? -->

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

- We construct a typical daily load profile from an average of the apparent power observations.
    - We plot the mean load by averaging the valid observations for each minute in over all the observation period.
    - These mean power are then plotted with the time of day as the independent variable.

<!-- TODO: determine how to plot quartiles on load profile -->

- We construct a load duration curve to show the percentage of time that the grid is supplying a given power level.
    - We sort the time series in descending order
    - We normalize the independent variable onto to a scale of zero to one so that the plot represents the time the grid is running.
    - It is essentially a cumulative distribution function with the axes reversed

## State of the art fuel estimation

- We estimate the best possible cost per kWh of generation on the microgrids assuming the datasheets for high quality genset performance and the observed loads.
    - Generators become less efficient in fuel use per energy delivered as the load is decreased
    - We find specification sheets for a generators of similar size from a leading manufacturer
    - Specification sheets report fuel use at 25%, 50%, 75%, and 100% of the full load.
    - We assume a linear relationship between fuel use and generator load.
    - We take the published curves for fuel use and extrapolate to the low loads observed on microgrids
    - We divide the fuel rate by the apparent power to get the instantaneous specific fuel consumption
    - Using these fits, we can create a time series of fuel rates from the observed load data
    - Following the method used to construct a load duration curve, we create a specific fuel consumption duration curve
    - This curve has the specific fuel consumption in liters per kVA-hour as the independent variable

## Observed fuel use

- We estimate the per kWh cost of generation in real-world conditions from the delivered energy and the reported fuel use.
    - Logs are kept of fuel input to the generator on a nightly basis.
    - We divide the mean fuel per night as reported in the written log with the mean generation per night to get the overall specific fuel consumption

<!-- TODO: how do we know the sizes of the generators? -->

# Results

- TODO: format tables with reasonable numbers of significant figures

## Data Coverage

- We have confidence in the data for 86% to 93% of the observation period for the microgrids
    - The data cover from two to three months in the villages.
    - We have direct time series measurements for 9 to 23 percent of the observation period
    - We have messages indicating the grid going off and back on that bring coverage up to 86 to 93 percent.
    - We have no robust way of the presence or absence of power in the data gaps with the data set available.


| Village   |   Duration (days) |   Percent data |   Percent known downtime |   Total Coverage |
|:----------|------------------:|---------------:|-------------------------:|-----------------:|
| atamali   |           124.065 |      0.1904    |                 0.67276  |         0.863161 |
| ayapo     |           127.433 |      0.232502  |                 0.672051 |         0.904552 |
| kensio    |           102.194 |      0.0893443 |                 0.837226 |         0.92657  |

<!-- SI_data_integrity -->

## Electricity Energy Consumption

- TODO: fix order of columns in energy table
- TODO: write section outline


- We report on daily electricity energy consumption
    - daily energy on days of operation
    - daily energy over entire valid observation period
    - the average energy use for connected household is between 0.4 and 0.9 kWh per day
    - the cumulative distribution function shows that the electricity most days is clustered around the mean but there is a low energy tail

![](./plots/daily_energy_CDF.png)

|   operating mean (kWh) |   overall mean (kWh) |   per household operating mean (kWh) | village   |
|-----------------------:|---------------------:|-------------------------------------:|:----------|
|               15.213   |             14.9364  |                             0.380324 | atamali   |
|               90.0091  |             84.6239  |                             0.873875 | ayapo     |
|                9.12281 |              5.30612 |                             0.45614  | kensio    |

## Power Consumption

- TODO: clean up date axis on hourly_kVA.png
- TODO: create time series percentile plot for hourly profile
- TODO: create a CDF of power in the SI


- These grids run exclusively during the evening
    - We display the averaged power profile for the three microgrids
    - The average load plot shows that the grid only provides power in the evenings

![](./plots/hourly_kVA.png)

- The microgrid has a relatively even load profile
    - The CDF or load duration curve shows mostly zero load or non-operation
    - It also shows few power observations between zero and a cutoff power
    - For the purposes of generator efficiency, we focus on the periods of non-zero power output

![](./plots/power-CDF.png)

![](./plots/power-CDF-no-zeros.png)

- We report on the apparent power consumption in these microgrids
    - the table shows the mean loads during operation of the microgrids are well below the operating points of the generators
    - The most well-matched microgrid is operating at 32% of the rated load and one grid is only at 6% of the load.
    - These means do not include the periods of zero power

Table: Total and per connection apparent power

|    |   HH |   kVA factor |   max kVA |   max kVA per HH |   mean kVA |   mean kVA per HH | village   |
|---:|-----:|-------------:|----------:|-----------------:|-----------:|------------------:|:----------|
|  0 |   40 |     0.73535  |     3.884 |         0.0971   |    2.8561  |         0.0714024 | atamali   |
|  1 |  103 |     0.767282 |    17.041 |         0.165447 |   13.0753  |         0.126944  | ayapo     |
|  2 |   20 |     0.690428 |     3.253 |         0.16265  |    2.24596 |         0.112298  | kensio    |

Table: Generator Utilization

|         |     mean |   rating (kVA) |   percent genset load |
|:--------|---------:|---------------:|----------------------:|
| Atamali |  2.8561  |             25 |             0.114244  |
| Ayapo   | 13.0753  |             40 |             0.326881  |
| Kensio  |  2.24596 |             35 |             0.0641703 |

## Microgrid Marginal Cost

- I model the specific fuel consumption in liters per kWh for a hypothetical well-maintained generator operating at the manufacturers specifications at the fraction of load we observe
    - The generators range in size from 25 kVA to 40 kVA
    - Our fit to the generator specifications has a slope of 0.270 lph per kVA of load
    - The fit has a slope of 0.059 lph per kVA of rated power
    - The modeled specific fuel consumption at 100% load range from 0.287 to 0.302 liters per kVA-hour
    - The modeled specific fuel consumption at the rated load range from 0.361 to 0.681 liters per kVA-hour

- Since we have the time series observations of kVA we can model a duration curve for the specific fuel consumption.
    - TODO: report descriptive statistics on the curves

- I also report an observed specific fuel consumption based on the generator operators daily fuel logs and the observed daily energy use
    - Observations of fuel consumption are from operator reports
    - Atamali reports 30 liters per night for its 25 kVA genset to deliver 15 kWh
    - This results in a specific fuel consumption of 2 liters per kWh.
    - Ayapo reports 60 liters per night for its 40 kVA genset to deliver 85 kWh
    - This is a specific fuel consumption of 710 ml per kWh, well above predicted.
    - At 1 USD per liter for diesel, this is a marginal cost of 0.70 USD and 2 USD per kWh

|    |   observed SFC |   observed_daily_fuel |   operating mean (kWh) | village   |
|---:|---------------:|----------------------:|-----------------------:|:----------|
|  0 |       1.972    |                    30 |               15.213   | atamali   |
|  1 |       0.666599 |                    60 |               90.0091  | ayapo     |
|  2 |     nan        |                   nan |                9.12281 | kensio    |

- data sheet fuel consumption per hour
- TODO: should this be output as a percent penalty over expected in the specific fuel consumption table?
- TODO: Report median costs and 95th percentile costs?
- TODO: describe the data sheets


|         |   genset rating kVA |   expected fuel rate at 100% (lph) |   mean load (kVA) |   expected fuel rate at mean load (lph) |
|:--------|--------------------:|-----------------------------------:|------------------:|----------------------------------------:|
| atamali |                  25 |                            7.16545 |           3.05753 |                                 1.24064 |
| ayapo   |                  40 |                           12.105   |          14.3235  |                                 5.17199 |
| kensio  |                  35 |                           10.4585  |           2.45143 |                                 1.66989 |



|         |   expected specific fuel consumption at 100% load (lpkVA) |   expected specific fuel consumption at mean load (lpkVA) |   genset rating kVA |
|:--------|----------------------------------------------------------:|----------------------------------------------------------:|--------------------:|
| atamali |                                                  0.286618 |                                                  0.405766 |                  25 |
| ayapo   |                                                  0.302626 |                                                  0.361084 |                  40 |
| kensio  |                                                  0.298815 |                                                  0.681192 |                  35 |


- The figure shows the ideal specific fuel consumption.
    - It assumes the fuel consumption matches the data sheet
    - In practice, we expect wear and tear to reduce the efficiency of the generator.



![](./plots/specific_fuel_consumption_duration.png)


# Discussion

- observed fuel costs are well above modeled fuel costs suggesting generator maintenance issues
- observed fuel costs are well above tariff collection requiring subsidy
- operating at low load increases engine maintenance requirements and worsens fuel costs
- it is likely uneconomical to run these generators continuously but unnecessarily high marginal costs worsen the problem
- these observed fuel costs are likely higher than those in least-cost models




- at $400 per kW, $1 per liter, and 300 ml/kWh, fuel cost exceeds capital cost after about 1000 hours, making generator replacement feasible (confirm)
- an efficient diesel generator has comparable cost and carbon intensity compared to existing fossil sources
- diesel cost and carbon intensity can match or greatly exceed coal and NG averages
- while PV costs rise on a capital basis, diesel costs rise on a marginal basis
- marginal costs are often more difficult because operation and maintenance isn't well handled

- We report two electricity consumption averages.
    - We report an average for energy delivered on days or nights with full access.
    - We report another average for actual energy delivered each day.
    - The first average gives the potential energy consumption for the system when it is fully operational without technical or operational constraints.
    - The second average is the actual electricity delivered.
    - The difference between these two provides a measure of latent demand.


Operation of the generators at an inefficient operating point wastes diesel fuel and drives up operating costs.

- Operating a diesel generator at a power load well below its designed operating point leads to inefficient operation.
    - This inefficiency increases fuel cost per unit of energy generated.
    - Ayapo retains a reasonable fuel rate close to the designed operation of the generator.
    - Atamali and Kensio with average loads at 11 and 6 percent of the design have theoretical specific fuel consumptions (SFC) of 460 ml per kVA-hour and 970 ml per kVA-hour.
    - This operation could increase wear and tear on the generator, increasing maintenance costs and downtime.

- The operating costs are well above the tariffs
    - Customers pay 5 cents or less per kWh and many meters don't function
    - The observed marginal costs due to fuel well exceed this

- This is far above the our ideal fuel consumption estimate for Atamali.
- Tariffs in the area are below 5 cents per kWh so the electricity is almost completely subsidized

# Conclusion


