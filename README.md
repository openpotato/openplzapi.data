# OpenPLZ API Data

This repository contains:

+ Data export of all German streets (including postal codes, localities and regional keys) from the [OpenStreetMap project](https://www.openstreetmap.org/).

+ List of communes (municipalities) in Liechtenstein.

## Sources  

### Germany

#### Data processing

This dataset is an extract from the regional OpenStreetMap file for Germany [germany-latest.osm.pbf](https://download.geofabrik.de/europe/germany.html). The following algorithm is used:

1. Read in all postal code areas (OSM relations), municipality areas (OSM relations), borough areas (OSM relations), suburb areas (OSM relations) and streets (OSM ways) together with their geometric information.

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
	
	and have NOT any of the following properties:
	
    Name      | Value
    --------- | -----
    `access`  | `private`
    `access`  | `forestry`
    `access`  | `military`

3. For each OSM Street, determine the geometric centre and in which municipality and postcode area it is located. Where available, the borough area and/or suburb area should also be taken into account.

4. Create a new street object (name, postal code, locality, regional key, borough, suburb) from the combination of 5 data objects (OSM street, OSM municipality area, OSM postal code area, borough OSM areas, suburb OSM area).

5. Shorten all street names with `strasse` or `Strasse` to `str.` or `Str.`.

6. Ignore all streets with names matching the following regular expression: `^(\?|\+|-|_|\d*|\(.*\))$`.

7. Export all street objects to CSV (file `streets.csv`).

#### Data post-processing

Despite filtering the data, the resulting CSV file `streets.csv` contains streets that are unusable or even incorrect. For example:

+ Small footways (often with strange names) that cannot be distinguished from usable ways.

+ Streets that do not match the postal code area 100% and therefore appear twice with different postal codes and municipal assignments (yes, this is not always wrong).

To solve this problem, we have introduced an additional csv file called `streets.ignore.csv`. This file is used to automatically create (via GitHub Action) a third csv file called `streets.updated.csv` by removing all streets from `streets-csv` that are contained in `streets.ignore.csv`. The `streets.ignore.csv` file is maintained manually.

#### Data quality

The data in the OpenStreetMap project is not perfect, but surprisingly well maintained for Germany.  

+ A total of 121 municipality regional keys from the official [GV100AD (Gemeindeleitdatei)](https://www.destatis.de/EN/Themes/Countries-Regions/Regional-Statistics/OnlineListMunicipalities/_inhalt.html) are not represented. This is largely due to the fact that these are areas without buildings and proper roads.

+ Streets and their postal codes or their municipality keys are determined on the basis of geometrical comparisons. This procedure is not 100% perfect.

+ Street names, postal codes and municipality keys are subject to constant change. The OpenStreetMap project as a community project tries as best as possible to update its data regularly. Current changes in streets and postal codes are documented quarterly by Deutsche Post (see [Deutsche Post Direkt](https://www.deutschepost.de/de/d/deutsche-post-direkt/datafactory/download_postleitdaten.html)), current changes in municipality assignment in the [Gemeindeleitdatei](https://www.destatis.de/EN/Themes/Countries-Regions/Regional-Statistics/OnlineListMunicipalities/_inhalt.html) of the Federal Statistical Office (Destatis).

### Liechtenstein

Since there is no official list of municipalities in Liechtenstein that is machine-readable, we have created our own list as a CSV file based on [information from Wikipedia](https://w.wiki/BEPn).

## Can I help?

Yes, that would be much appreciated. The best way to help is to post a response via the Issue Tracker and/or submit a Pull Request.
