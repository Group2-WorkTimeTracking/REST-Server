# Work time tracking API

## URIs

##### `worktime-tracking.herokuapp.com/login`

* Submit a **POST** request to this URI to authenticate through the API. If the request is successful, the server will return an account object, *including the userkey that is required for every other API paths*.

### Employer URIs (for the web client)

##### `worktime-tracking.herokuapp.com/account`

* Submit a **GET** request to this URI to get account details. This will return an account object.
* Submit a **PUT** request to this URI to modify account details. In the body of the request, include an account object. If the request is successful, the server will return an account object.

##### `worktime-tracking.herokuapp.com/employee`

* Submit a **GET** request to this URI to get the list of employee. This will return an array of account object.
* Submit a **POST** request to this URI to create a new employee. In the body of the request, include an account object. If the request is successful, the server will return an account object.

##### `worktime-tracking.herokuapp.com/employee/{employee-id}`

Here `{employee-id}` is the ID of the employee.
* Submit a **GET** request to this URI to get employee details. This will return an account object.
* Submit a **PUT** request to this URI to modify employee details. In the body of the request, include an account object. If the request is successful, the server will return an account object.
* Submit a **DELETE** request to this URI to delete an employee. If the request is successful, the server will return an HTTP `204` (`No Content`) status.

##### `worktime-tracking.herokuapp.com/location`

* Submit a **GET** request to this URI to get the list of workplace. This will return an array of location object.
* Submit a **POST** request to this URI to create a new workplace. In the body of the request, include a location object. If the request is successful, the server will return a location object.

##### `worktime-tracking.herokuapp.com/location/{location-id}`

Here `{location-id}` is the ID of the work place.
* Submit a **GET** request to this URI to get a work place. This will return a location object.
* Submit a **PUT** request to this URI to modify a work place. In the body of the request, include a location object. If the request is successful, the server will return a location object.
* Submit a **DELETE** request to this URI to delete a location. If the request is successful, the server will return an HTTP `204` (`No Content`) status.

##### `worktime-tracking.herokuapp.com/employee/{employee-id}/location`

Here `{employee-id}` is the ID of the employee.
* Submit a **GET** request to this URI to get the employee workplace. This will return a location object.
* Submit a **PUT** request to this URI to modify employee workplace. In the body of the request, include a location object. If the request is successful, the server will return a location object.

##### `worktime-tracking.herokuapp.com/employee/{employee-id}/logs`

Here `{employee-id}` is the ID of the employee.
* Submit a **GET** request to this URI to get the day-per-day work time of the employee for the current month. This will return a logs object.

##### `worktime-tracking.herokuapp.com/employee/{employee-id}/logs/{month-id}`

Here `{employee-id}` is the ID of the employee and {month-id} is the ID of the month.
* Submit a **GET** request to this URI to get the day-per-day work time of the employee for a month. This will return a logs object.

### Employee URIs (for the mobile application)

##### `worktime-tracking.herokuapp.com/account`

* Submit a **GET** request to this URI to get account details. This will return an account object.
* Submit a **PUT** request to this URI to modify account details. In the body of the request, include an account object. If the request is successful, the server will return an account object.

##### `worktime-tracking.herokuapp.com/account/location`

* Submit a **GET** request to this URI to get the employee workplace. This will return a location object.

##### `worktime-tracking.herokuapp.com/work/start`

* Submit a **POST** request to this URI to start counting work time. In the body of the request, include a start timetag object. If the request is successful, the server will return a timetag object.

##### `worktime-tracking.herokuapp.com/work/finish`

* Submit a **POST** request to this URI to stop counting work time. In the body of the request, include the stop timetag object. If the request is successful, the server will return a timetag object.

##### `worktime-tracking.herokuapp.com/work/note`

* Submit a **POST** request to this URI to make a note. In the body of the request, include a note object. If the request is successful, the server will return a note object.

##### `worktime-tracking.herokuapp.com/account/logs`

* Submit a **GET** request to this URI to get the day-per-day work time of the employee for the current month. This will return a logs object.

##### `worktime-tracking.herokuapp.com/account/logs/{month}`

Here `{month-id}` is the month on the ISO 8601 format (`2017-01`).
* Submit a **GET** request to this URI to get the day-per-day work time of the employee for a month. This will return a logs object.

## JSON Objects

##### Account

```json
{...}
```

##### Location

```json
{
    "place-name": "OAMK, Kotkantie campus",
    "coordinate": {"latitude": 64.99958,
                   "longitude": 25.51078},
    "size": 0.00220
}
```

##### Logs

```json
{
    "month": "2016-12",
    "total-working-hours": 142.1,
    "daily-work": [
        {
            "day": "2016-12-01",
            "working-hours": 7.9,
            "note": ""
        },
        {
            "day": "2016-12-02",
            "working-hours": 8.3,
            "note": ""
        },
        {
            "day": "2016-12-05",
            "working-hours": 0.0,
            "note": "I have a meeting in Helsinki."
        },
            ...
    ]
}
```

##### Timetag

```json
{
    "type": "start",
    "timestamp": 1485096644, // POSIX time
    "user-id": 42
}
```

##### Note

```json
{
    "message": "I won’t be present because of a meeting in Helsinki.",
    "day-of-effectiveness": "2017-01-22",
    "user-id": 42
}
```
