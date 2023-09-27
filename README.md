# OpenPLZ API Data

Data export of all German streets (including postal codes, localities and regional keys) from the [OpenStreetMap project](https://www.openstreetmap.org/).

## Sources  

This dataset is an extract from the regional OpenStreetMap file for Germany [germany-latest.osm.pbf](https://download.geofabrik.de/europe/germany.html). The following algorithm is used:

1. Read in all postal code areas (OSM relations), municipality areas (OSM relations) and streets (OSM ways) together with their geometric information.

2. Include only ways which have one of the the following properties:

    Name      | Value
    --------- | -----
    `place`   | `square`
	`leisure` | `park`
	`highway` | `primary`
	`highway` | `secondary`
	`highway` | `tertiary`
	`highway` | `residential`
	`highway` | `living_street`
	`highway` | `road`
	`highway` | `unclassified`
	`highway` | `footway`
	`highway` | `pedestrian`
	`highway` | `track` (but only for `tracktype=grade1`)
	`highway` | `service` (but only for `service=alley`)

3. For each OSM Street, determine the geometric centre and in which municipality and postcode area it is located.

4. Create a new street object (name, postal code, locality, regional key) from the combination of the three data objects (OSM street, OSM municipality area, OSM postal code area).

5. Shorten all street names with `strasse` or `Strasse` to `str.` or `Str.`.

6. Ignore all streets with names matching the following regular expression: `^(\\?|\\+|-|_|\\(.*\\))$`.

7. Export all street objects to CSV.

## Data quality

The data in the OpenStreetMap project is not perfect, but surprisingly well maintained for Germany.  

+ A total of 120 municipality regional keys from the official [GV100AD (Gemeindeleitdatei)](https://www.destatis.de/EN/Themes/Countries-Regions/Regional-Statistics/OnlineListMunicipalities/_inhalt.html) are not represented. This is largely due to the fact that these are areas without buildings and proper roads.

+ Streets and their postal codes or their municipality keys are determined on the basis of geometrical comparisons. This procedure is not 100% perfect.

+ Street names, postal codes and municipality keys are subject to constant change. The OpenStreetMap project as a community project tries as best as possible to update its data regularly. Current changes in streets and postal codes are documented quarterly by Deutsche Post (see [Deutsche Post Direkt](https://www.deutschepost.de/de/d/deutsche-post-direkt/datafactory/download_postleitdaten.html)), current changes in municipality assignment in the [Gemeindeleitdatei](https://www.destatis.de/EN/Themes/Countries-Regions/Regional-Statistics/OnlineListMunicipalities/_inhalt.html) of the Federal Statistical Office (Destatis).

## Can I help?

Yes, that would be much appreciated. The best way to help is to post a response via the Issue Tracker and/or submit a Pull Request.
