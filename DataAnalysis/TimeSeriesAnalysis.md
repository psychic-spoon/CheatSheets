## Time Series Analysis
> Time series analysis accounts for the fact that data points taken over time may have an internal structure, such as autocorrelation, trend, seasonal or periodic variation.


#### [Time Series Components](https://www.linkedin.com/pulse/everything-time-series-analysis-components-data-saranya-anandh/)

**Seasonal**: Seasonality is a component of a time series in which the data experiences regular and 
		  predictable changes that recur in regular calendar intervals such as months or fiscal year.


**Cycle**: Some time series may show tendency to repeat itself over a longer period of time.
		That is, there could be combination of trend and seasonal data that repeats over a longer period of time.

**Trend**: Trend is the long-term movement in a time series without time or irregular effects and is a reflection
		 of the underlying level. The trend can be increasing or decreasing as well as linear or nonlinear.

![](https://media.licdn.com/mpr/mpr/shrinknp_800_800/AAEAAQAAAAAAAAf9AAAAJGJiZjUxMDEzLTU3MzItNDIzNy04ODllLTE5MjYwYWMwYWYyNQ.png)

#### Overall Steps
- Plot data to see the presence of different components of time series
- Model Trend and Seasonality
- After removing trend seasonality, model the remaining data as autoregressive part and  noise part
- Use an additive or multiplicative model for forecasting using the components identified
- Compute residuals by comparing forecast with actuals
- Confirm that residuals is actually noise




#### [Stationary Time Series](https://people.duke.edu/~rnau/411diff.htm)
Stationary time series is one whose mean and variance is constant over time. 

- A stationarized series is relatively easy to predict: you simply predict that its statistical properties will be the same in the future as they have been in the past!
	
- The predictions for the stationarized series can then be "untransformed," by
	 reversing whatever mathematical transformations were previously used, to 
	 obtain predictions for the original series.

- _Most business and economic time series are far from stationary when expressed
	 in their original units of measurement, and even after deflation or seasonal 
	 adjustment they will typically still exhibit trends, cycles, random-walking,
	  and other non-stationary behavior._


The main reason why using ordinary least squares regression is frowned upon in modeling 
time series data is that the error terms are correlated with each other.

[Fitting time series regression models](http://people.duke.edu/~rnau/411l696.htm)

:+1: This looks great

**Resources** 
- [Time Series Duke University](https://people.duke.edu/~rnau/411home.htm) 
- [Using dplyr](https://blog.exploratory.io/introducing-time-series-analysis-with-dplyr-60683587cf8a) 
- [Time Series Components](https://www.linkedin.com/pulse/everything-time-series-analysis-components-data-saranya-anandh/)

About