# GIS Automation

Production ArcPy scripts from years building and running an enterprise GIS for a
county sanitary and storm sewer system (Buffalo, NY). These are working tools
that ran against a live system of record, not demos.

Author: Steven Russell, GISP - https://russelljr.com

## Scripts

### `update_layers.py`
Pulls feature classes from the enterprise geodatabase (ArcSDE on SQL Server) and
regenerates the local shapefiles and layer files that field and office staff
worked from. Built in ModelBuilder, exported to Python, then extended. Ran on a
schedule so the working data stayed in sync with the authoritative SDE database.

Deployed as four district-specific variants, one per sewer maintenance district.

### `morehead.py`
Walks the vertices of a rail corridor centerline and returns the bearing
(azimuth from north), running station distance, and coordinates at each
point along the line. Rebuilt from scratch after the prior GIS staffer's
version left with him - a clean replacement for a tool the team relied on.

Written for ArcGIS Pro (`arcpy`, Python 3).
## Notes

- Written for ArcGIS Desktop (`arcpy`, Python 2.x) - the production environment of the era.
- Database connection details live in ArcGIS `.sde` connection files, never in the scripts.
- Internal server paths and connection names have been replaced with
  `<OUTPUT_PATH>` / `<OUTPUT_GDB>` placeholders.

## License

MIT - see [LICENSE](LICENSE).
