# Work time tracking API

## URIs

#### `/login`

* Submit a **POST** request to this URI to authenticate through the API. If the request is successful, the server will return an account object, *including the userkey that is required for every other API paths*.

### Employer URIs (for the web client)

#### `/account`

* Submit a **GET** request to this URI to get account details. This will return an account object.
* Submit a **PUT** request to this URI to modify account details. In the body of the request, include an account object. If the request is successful, the server will return an account object.

#### `/employee`

* Submit a **GET** request to this URI to get the list of employee. This will return an array of account object.
* Submit a **POST** request to this URI to create a new employee. In the body of the request, include an account object. If the request is successful, the server will return an account object.

#### `/employee/{employee-id}`

Here `{employee-id}` is the ID of the employee.
* Submit a **GET** request to this URI to get employee details. This will return an account object.
* Submit a **PUT** request to this URI to modify employee details. In the body of the request, include an account object. If the request is successful, the server will return an account object.
* Submit a **DELETE** request to this URI to delete an employee. If the request is successful, the server will return an HTTP `204` (`No Content`) status.

#### `/location`

* Submit a **GET** request to this URI to get the list of workplace. This will return an array of location object.
* Submit a **POST** request to this URI to create a new workplace. In the body of the request, include a location object. If the request is successful, the server will return a location object.

#### `/location/{location-id}`

Here `{location-id}` is the ID of the work place.
* Submit a **GET** request to this URI to get a work place. This will return a location object.
* Submit a **PUT** request to this URI to modify a work place. In the body of the request, include a location object. If the request is successful, the server will return a location object.
* Submit a **DELETE** request to this URI to delete a location. If the request is successful, the server will return an HTTP `204` (`No Content`) status.

#### `/employee/{employee-id}/location`

Here `{employee-id}` is the ID of the employee.
* Submit a **GET** request to this URI to get the employee workplace. This will return a location object.
* Submit a **PUT** request to this URI to modify employee workplace. In the body of the request, include a location object. If the request is successful, the server will return a location object.

#### `/employee/{employee-id}/logs`

Here `{employee-id}` is the ID of the employee.
* Submit a **GET** request to this URI to get the day-per-day work time of the employee for the current month. This will return a logs object.

#### `/employee/{employee-id}/logs/{month}`

Here `{employee-id}` is the ID of the employee and `{month}` is the month on the ISO 8601 format (e.g. `2017-01`).
* Submit a **GET** request to this URI to get the day-per-day work time of the employee for a month. This will return a logs object.

### Employee URIs (for the mobile application)

#### `/account`

* Submit a **GET** request to this URI to get account details. This will return an account object.
* Submit a **PUT** request to this URI to modify account details. In the body of the request, include an account object. If the request is successful, the server will return an account object.

#### `/account/location`

* Submit a **GET** request to this URI to get the employee workplace. This will return a location object.

#### `/work/start`

* Submit a **POST** request to this URI to start counting work time. In the body of the request, include a start timetag object. If the request is successful, the server will return a timetag object.

#### `/work/finish`

* Submit a **POST** request to this URI to stop counting work time. In the body of the request, include the stop timetag object. If the request is successful, the server will return a timetag object.

#### `/work/note`

* Submit a **POST** request to this URI to make a note. In the body of the request, include a note object. If the request is successful, the server will return a note object.

#### `/account/logs`

* Submit a **GET** request to this URI to get the day-per-day work time of the employee for the current month. This will return a logs object.

#### `/account/logs/{month}`

Here `{month-id}` is the month on the ISO 8601 format (`2017-01`).
* Submit a **GET** request to this URI to get the day-per-day work time of the employee for a month. This will return a logs object.

## JSON Objects

#### Account

```json
{
    "realName": "J. Random User",
    "login": "jrandom",
    "role": "employer",
    "key": "b613679a0814d9ec772f95d778c35fc5ff1697c493715653c6c712144292c5ad"
}
```

#### Location

```json
{
    "placeName": "OAMK, Kotkantie campus",
    "coordinate": {"latitude": 64.99958,
                   "longitude": 25.51078},
    "size": 0.00220
}
```

#### Logs

```json
{
    "month": "2016-12",
    "totalWorkingHours": 142.1,
    "dailyWork": [
        {
            "day": "2016-12-01",
            "workingHours": 7.9,
            "note": ""
        },
        {
            "day": "2016-12-02",
            "workingHours": 8.3,
            "note": ""
        },
        {
            "day": "2016-12-05",
            "workingHours": 0.0,
            "note": "I have a meeting in Helsinki."
        }
    ]
}
```

#### Timetag

```json
{
    "type": "start",
    "timestamp": 1485096644,
    "userId": 42
}
```

#### Note

```json
{
    "message": "I won’t be present because of a meeting in Helsinki.",
    "dayOfEffectiveness": "2017-01-22",
    "userId": 42
}
```
