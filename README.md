# Bartonbus :busstop: 

_A Python wrapper around Trent Barton's live bus times_

[![Build Status](https://travis-ci.org/alxwrd/bartonbus.svg?branch=master)](https://travis-ci.org/alxwrd/bartonbus)
[![Downloads](https://img.shields.io/badge/dynamic/json.svg?url=https://pypistats.org/api/packages/bartonbus/recent?mirrors=false&label=downloads&query=$.data.last_month&suffix=/month)](https://pypistats.org/packages/bartonbus)

> I never got around to building this :grimacing:

## Example

```python
>>> import bartonbus

>>> service = bartonbus.lookup_service("Red Arrow")

>>> service.directions
[<Direction('Derby > Nottingham', service='Red Arrow')>, ...]

>>> service.stops
[<Stop('Derby Bus Station (bay 5)')>, <Stop('Morledge (stop C8)')>, ...]

>>> service.stops[0].arrivals
[<Arrival('2018-11-14T12:59:16.7059878+00:00', service='Red Arrow'), ...]

>>> next_bus = service.stops[0].arrivals[0]
>>> next_bus.eta
'9 minutes from now'
```
