# Introduction

The electrification of the remaining 1.2 billion people without access requires a close attention to costs.
Indonesia is executing a large electrification expansion to achieve universal access [@ADB_AUEAII].
Indonesia has made significant progress reducing the number of households without electricity access over the last decades.
A significant fraction of the remaining households are beyond the reach of centralized grids and will require decentralized solutions.
Indonesian planning documents based on least-cost studies show diesel generators as a significant part of the new electricity supply [@ADB_AUEAII; @IEEFA; @RUPTL].
To ensure the delivery of electricity at the lowest price, the operating costs should be compared to assumptions over time.
If these operating costs are significantly different from the assumptions, the electrification plan should be revisited.

Previous work has shown problems with diesel generation but there are few examples of direct modeling and measurement of the fuel used per unit of electricity delivered (specific fuel consumption or SFC).
Grids in Haiti show problems with loads below the capacity of the generator that lead to infrequent operation over limited hours.
These problems make sustainable financial operation of the microgrids very difficult and many have fallen into disuse.
[@Schnitzer_Thesis].
A diesel microgrid in Nicaragua also runs at well below the generator rating [@Casillas_EP].
In the case of photovoltaic (PV) electricity, having components that provide more energy than is being used leads to higher costs [@Louie_ESD, @Lee].
Diesel generators that can deliver more power than is required by the customers can lead to higher fuel costs and generator degradation over time [@Hove_Tazvinga].

This study provides modeled and observed costs for diesel consumption in three microgrids in the Lake Sentani region of Indonesia.
We find that the generators are providing power well below their intended operating points.
Using a model based on the manufacturer specifications for several generators, we estimate that these generators would use 0.6 liters per kWh of electricity or above.
This is about twice the value for a well-maintained generator operating according to its specifications.
The observed fuel use reached as high as 1.9 liters per kWh suggesting serious fuel inefficiency likely due to issues of generator maintenance.

These results suggest that diesel micro-grids operating outside of centralized grid areas may not be performing to the expectations of the electricity planners.
Areas that are struggling with high costs of electricity delivery can estimate the SFC of their generators to check for degradation or insufficient loads.
These micro-grids could be retrofitted with diesel generators that are a better match to the load or with alternative electricity generation technologies.
Improving these operating costs could improve the financial viability on these existing grids and inform future electricity planning.

# Methods

We model and estimate the fuel use per unit of electrical energy delivered (specific fuel consumption or SFC) for three village microgrids.
Power and energy data from data logging meters are collected, cleaned, and analyzed to extract the energy and power delivered.
We create a model of generator fuel consumption as a function of the rated power and delivered power based on the specification sheets of nine comparable generators.
The observed power during operation and rated energy size is used to infer the SFC for each of the three microgrids.
To estimate the actual observed SFC we take the ratio of the reported fuel use per day by the operator and the measured energy use per day.

We measured the energy and power delivered to three villages with diesel microgrids using data logging meters.
The recordings were compiled from late April to July 2015 as part of the work of a private microgrid provider in the area.
The meters were placed at the main output of the generator and measured the energy delivered to the village distribution system.
The data logger measured power in volt-amps and accumulated energy in kilowatt-hours at one-minute intervals.
These measurements were transmitted over a communication network to a database for storage.

We assemble a time series record from our record of data.
There are three possibilities in the data recording process.
One, the meter and generator were properly functioning and data was stored on one-minute intervals.
Two, the meter is properly functioning and the generator was dormant and a data point for the shutdown and startup of the generator was stored.
Third, the meter or communication networks were not functioning properly and no data is in the record.
We account for each of these possibilities as we assemble the time series of generator data.

We model the cost per kWh of generation on these microgrids using a linear fit of manufacturer generator specification data from nine specification sheets from three manufacturers.
All specification sheets report the fuel use in liters per kWh as a function of the power delivered by the generator (load).
All specification sheets report on SFC while delivering power at 50%, 75%, and 100% of the rated load while some also include a 25% data point.
We assume a linear relationship between the SFC and the delivered power as well as the SFC and the rated power for the generator.
These data are used to create a linear regression model of fuel use.
The rated power for each of the three generators and the observed average power of operation for each microgrid is fed into this linear model to predict the SFC for each generator.

We also estimate the per kWh cost of generation in real-world conditions on these grids from the delivered energy and the reported fuel use.
Operators keep logs of the approximate fuel use per day for the microgrids.
The ratio of this approximate fuel use per day and the energy delivered per day gives the observed specific fuel consumption.


