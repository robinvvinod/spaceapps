# Submitted to NASA Covid-19 SpaceAppsChallenge

## CovidView: Is it safe? Covid-19 hotspot prediction

### Summary
CovidView works by identifying the correlation of multiple metrics related to human factors, to predict future Covid-19 hotspots. We translate this information to provide an early warning system that allows preventative and preparatory action to be taken, before there are a large number of cases.
How We Addressed This Challenge

Our challenge was to determine how human factors can influence and affect Covid-19 hotspots. Our project considers a number of factors that are related to, or could influence, human activity.

By using the available US Covid-19 related data, we are able to pinpoint which county (or counties) out of the 3000+ that are likely to become hotspots a week in advance. We determined how Covid-19 cases are affected by certain factors such as mobility, population density of each county and the availability and efficiency of testing.

The idea is to make a functioning website that will allow users to identify the risk level of an outbreak in their county. It is also possible to check the status of surrounding counties. Our prototype can be accessed at: https://robinvvinod.github.io/spaceapps/website/homepage.html

#### Notable features

    Early warning system for at-risk areas
    Check risk level for similar areas
    1 week advance prediction - Indicated level of risk from low to high
    Updated daily

#### Notable outcomes

    Enables early planning to prevent hotspot or reduce impact
    Reduction in new Covid-19 confirmed cases
    Prevention of overwhelmed healthcare system

## How We Developed This Project

### Our inspiration 

It goes without saying that everyone has been directly affected by Covid-19, and it has caused more than 6,000,000 cases and more than 360,000 deaths worldwide. These numbers are still increasing everyday. Our team, Nerd Immunity, chose to tackle this challenge as we wanted to do our part to help fight this pandemic and felt like this could make the most immediate impact.

Many countries are easing their lockdown measures, and we want to propose a method that makes lockdowns and coming out them more effective to prevent a second wave. This can guide and inform policy makers and members of the public.
Our approach 

We decided to choose the United States to train our model. This is due the expanse of the country, the depth, range and availability of data, the fact that it is a high-profile country, and there are large numbers of clusters and cases.

Data was obtained from multiple sources to provide factors for prediction of cases. This required data cleaning and rearrangement into a format comparable across factors. Since FIPS code is unique to a county, it was used as an index to unite factors for one county. However, certain data such as symptoms was only available at state level, requiring discretion to be used in application to counties.

### Data acquisition

#### Mobility data

Apple mobility data quantified mobility using GPS and Apple Maps data from portable devices such as smartphones and smartwatches. This was downloaded in CSV format from their website (referenced) with values normalized to 100 at 26th January. There was considerable noise including weekend effects and this was removed using a 7 day moving average.

#### County demographics

This was downloaded in CSV format from the US Census Bureau (referenced). This included population, population density, median age and gender ratio. We correlated these against cases and found only population and population density correlated significantly and so only used these for regression.

#### Covid-19 infection stats

We obtained cases, deaths and tests dating from 22nd January from the NASA source (SEDAC, referenced) as required. We identified its source which is the Center For Systems Science and Engineering at John Hopkins University (referenced) which updates daily with confirmed case numbers, fatalities and hospitalization admissions daily. Data wrangling was performed on case data, including interpolation of missing values on May 12th/13th. Calculation of 14 day moving average was investigated but not ultimately used in order to preserve useful temporal information. 

#### Covid symptoms

Covid symptoms were investigated using Google Health Trends (referenced) data showing Google searches for Covid symptoms.  We initially downloaded the smoothed data but found this removed useful temporal information and later used the raw data. These were only available at state level and were therefore used for all counties inside each state.

#### Nitrogen dioxide measurements

Nitrogen dioxide can be used as an indicator for human activity because it is emitted by transport and industry (Reductions in Nitrogen Dioxide Associated with Decreased Fossil Fuel Use Resulting from COVID-19 Mitigation). However, upon further analysis this was found to be a poorer indicator than mobility and symptoms, due to difficulties in minimizing day-to-day effects and the general lack of geographical resolution.


### Analysis

#### Clustering

We expressed county cases and fatalities on a per capita basis by normalizing with respect to each county's population, to indicate relative severity of infection between counties. We  then performed hierarchical clustering which dynamically groups counties without assuming a fixed number of groups. We eventually chose 10 clusters because it separated outlying counties with high impact (eg. New York County, NY,  Trousdale County, TN) from those with lower impact. We then ordered the clusters by mean cases per capita. This ordering was used to produce a colorbar to visualize clusters as a choropleth  on page 1 of the website. This was also available for other factors such as mobility. The clustering allowed the website to identify counties with similar trends to the queried county, which were displayed in the bar on the lower half of page 1.

#### Correlations

To identify relationships for use in prediction, we carried out initial exploratory correlations between timeseries of factors and cases. For example, we found significant positive correlation between mobility and cases in virtually all counties after testing reached a steady state on 8th April. This was supported by a paper we found in our literature survey, demonstrating a linear relationship between viral reproduction rate R and mobility. However, further correlations were limited by differing time delays between timeseries. For example, symptoms and cases had a time delay of unknown duration, as was the case for mobility. We therefore experimented with predictions using linear regression methods, by varying time delays and/or smoothing between variables.

#### Case prediction using regression

We compared regression methods on mobility against daily cases. We chose Gaussian Process Regression over Support Vector Regression  and Decision Tree Regression (overfitting) as the daily cases  tend to a Gaussian distribution.  We used the first 80% of the timeseries for training and the final 20% for testing. We predicted cases from both mobility and symptoms and found better prediction was achieved using both. However, the choice of how much moving average and/or timeshift to apply to mobility/symptoms/ dailycases was still a problem to optimize. We opted against moving average of daily cases due to removal of useful temporal information. 

The final regression used mobility MA period of 7 (effectively a time delay of 3) with time delay of 4 for a combined shift of 7 days. The symptoms data had a delay of 12 days. This delay was obtained from our literature survey which found a paper reporting delay of 10-12 days between online symptoms reporting and cases ("Using internet search data to predict daily case number").

#### Website development

A demonstration website was developed with 3 pages showing 3 areas of interest: Risk Assessment, Predictions and Personal Risk. The Risk Assessment page shows the cumulative cases and risk level of a queried county, with cumulative cases shown from similar counties identified by clustering. The Predictions page shows predictions for the next 7 days in a queried county and a map showing counties clustered by number of predicted cases. The Personal Risk page shows predicted risk for a person of queried age and pre-existing conditions in a queried county on a queried day.


### Discussion

NB: Due to transparency of PNG images, axes may be difficult to read on a black background. 

NB: Due to transparency of PNG images, e relatively constant with minor variations (Prediction of New York county test data). This is due to symptoms data lacking the higher geographical resolution of county level. Were this rectified, we expect this would be ameliorated. However, there were regions where predictions matched daily case trend particularly well (Prediction of Orleans county test data). It should also be noted that inaccuracies in daily case prediction are exacerbated by the small scale at which the graph is plotted.  It is well understood that the prediction accuracy is limited by the quality of the training data, which differs extensively between times and counties due to differences in type, quantity and reporting of testing. The model assumes a Gaussian distribution in daily cases  but we have seen examples where there are such deviations in testing that this assumption is violated (Prediction of Erie county test data). Finally, in prediction of Orleans County training data  large unpredictable spikes did not cause the predicted curve to deviate from the trend line, suggesting a natural fit had been achieved without overfitting.


The website is available to test here: https://robinvvinod.github.io/spaceapps/website/homepage.html

### What we used

Languages used: Python, R, HTML

Libraries used: pandas, numpy, sklearn, statsmodels, scipy, matplotlib

Development tools used: Folium, Google Colab, Jupyter Notebook, Figma, Adobe XD, Excel

### Future work

Now that testing has been standardized in response to the first wave, we believe there will be improvement in model performance should there be a second wave. We could consider other indicators such as weather data, or county infrastructure and public attractions  to aid in prediction of future cases. There are also delays in obtaining mobility and symptoms data whose resolution would improve prediction, as would countywide reporting of symptoms. Now proof of concept has been demonstrated in the US, we expect our approach is transferable to other nations. 

## Project Demo
https://github.com/robinvvinod/spaceapps/blob/master/Nerd_Immunity_slides_200531.pptx

## Project Code
https://github.com/robinvvinod/spaceapps

## Resources

Equivalent work looking into economic impacts and a "mobility budget"

https://institute.global/policy/smart-exit-covid-19-early-warning-model


Mobility trends on Covid models

https://www.ejgm.co.uk/download/the-study-of-the-effects-of-mobility-trends-on-the-statistical-models-of-the-covid-19-virus-8212.pdf


New York times map of Minnesota cases

https://www.nytimes.com/interactive/2020/us/minnesota-coronavirus-cases.html


Mobility trends on Covid upsurge

https://www.prnewswire.com/news-releases/spireon-driving-data-demonstrates-strong-relationship-between-increases-in-mobility-and-upsurge-in-covid-19-cases-301045898.html


Korea's use of hotspot mapping to resolve Covid-19 visualisation 

https://www.unescap.org/blog/outpacing-covid-19-key-innovations-prompt-early-warning-early-actions


Use of internet search history to predict daily case number

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7176069/


Our model can be paired with alternative approaches such as sampling sewage

https://www.sciencemag.org/news/2020/04/coronavirus-found-paris-sewage-points-early-warning-system


Data sources

Facebook covid survey data

https://covid-survey.dataforgood.fb.com/#3/35/-75


Google Health Trend data used in model

https://github.com/cmu-delphi/delphi-epidata/blob/master/docs/api/covidcast_signals.md


Covid-19 infection data by county

https://www.kaggle.com/jieyingwu/covid19-us-countylevel-summaries?select=healthcare_visits.csv


Controlling human mobility influence on Covid infection

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7146642/


NASA SEDAC data

https://earthdata.nasa.gov/learn/articles/sedac-covid-19-viewer


Mobility data from Apple

https://www.apple.com/covid19/mobility


Reductions in Nitrogen Dioxide Associated with Decreased Fossil Fuel Use Resulting from COVID-19 Mitigation

https://svs.gsfc.nasa.gov/4810


Environmental data relevant to Covid-19

https://climate.gov/maps-data/primer/what-environmental-data-are-relevant-study-infectious-diseases-covid-19


New York Times Covid-19 data

https://data.humdata.org/dataset/nyt-covid-19-data


COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University

https://github.com/CSSEGISandData/COVID-19


Giovanni data

https://giovanni.gsfc.nasa.gov/giovanni/#service=TmAvMp&starttime=2020-05-01T00:00:00Z&endtime=2020-05-26T23:59:59Z&shape=tl_2014_us_state/shp_13&&data=OMNO2d_003_ColumnAmountNO2TropCloudScreened


Map of Covid infection

https://www.unacast.com/covid19/social-distancing-scoreboard


Seasonal temperature data

https://earthdata.nasa.gov/learn/pathfinders/covid-19/seasonality


Effects of latitude on Covid

https://www.cebm.net/covid-19/effect-of-latitude-on-covid-19/


US census data on counties

https://www.census.gov/data/tables/time-series/demo/popest/2010s-counties-total.html


Polygon map of US

https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us_counties_20m_topo.json


World json data

https://github.com/codeforamerica/click_that_hood/tree/master/public/data
