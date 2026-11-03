from math import atan2, degrees
import arcpy

# Set the workspace where your data is located
arcpy.env.workspace = r"<WORKSPACE_GDB>"

# Replace "line_feature" with the name of your line feature class
line_feature = "MoreheadFriendly"

# Walk the vertices of a line feature, returning bearing, running station
# distance, and coordinates at each vertex along the centerline.
def calculate_bearing_distance_station(line_fc):

    bearing_distance_station = []

    with arcpy.da.SearchCursor(line_fc, ["SHAPE@"]) as cursor:
        for row in cursor:
            # Iterate through each part of the line
            for part in row[0]:
                # Initialize station distance
                station_distance = 0
                # Iterate through each vertex in the part
                for i in range(1, len(part)):
                    # Get coordinates of current and previous vertex
                    x1, y1 = part[i-1].X, part[i-1].Y
                    x2, y2 = part[i].X, part[i].Y

                    # Calculate distance between current and previous vertex
                    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

                    # Calculate bearing (azimuth from north)
                    dx = x2 - x1
                    dy = y2 - y1
                    bearing = degrees(atan2(dx, dy))

                    # Update running station distance
                    station_distance += distance

                    # Append bearing, station distance, and coordinates to the list
                    bearing_distance_station.append((bearing, station_distance, (x1, y1)))

    return bearing_distance_station


# Call the function to calculate bearing, distance, and station coordinates
result = calculate_bearing_distance_station(line_feature)

# Print the results
for bearing, distance, coordinates in result:
    print("Bearing: {}, Station: {}, Coordinates: {}".format(bearing, distance, coordinates))
