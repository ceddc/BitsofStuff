# Paris building construction visualization (200k+)

[You can check the app here](/ConstructionParis.html)

This weekend the 4.5 version of the ArcGIS API for JavaScript have been released, and it's great.

Especially this new beta function to render featurelayers in WebGL.

Esri blog post : [FeatureLayer rendering: taking advantage of WebGL in 2D](https://blogs.esri.com/esri/arcgis/2017/09/29/featurelayer-taking-advantage-of-webgl-2d/)

Sooo, there is a nice demo about New York building construction, and it's really sweet.

The source code is here : <https://developers.arcgis.com/javascript/latest/sample-code/visualization-vv-color-animate/index.html>

But New york is a bit far away from where I live though, so why not use Paris? With a lot of historical buildings going way earlier than 1800?

There is the source code for the app, so all you need to do to make a nice Paris map is just to find some building data.


There is a great opendata website from l'Atelier parisien d'urbanisme
<http://opendata.apur.org/> and a dataset with many information about Paris buildings : <http://opendata.apur.org/datasets/002f14c0cf28435296a341d9921adf99_0>

Because this is still a beta feature, there are some limitation for WebGL featurelayers
> support is limited to layers created from feature services hosted on ArcGIS Online. Non-hosted enterprise feature services and client-side feature collections will be supported in a future release.

And the apur dataset is coming from an ArcGIS Server :-(

So with just a free account on <https://developers.arcgis.com/> (you get 50 credits, enough to play and host 200mb+ of data), you can upload the data on your own account and then use it in your app.

<https://www.arcgis.com/home/item.html?id=739c3c3d463f4ff2b594c683364d3874>


Then replace some variables and enjoy.


Want to learn more about this dataviz?
Learn ArcGIS : <http://learn.arcgis.com/en/>
ArcGIS API for JavaScript : <https://developers.arcgis.com/javascript/>
