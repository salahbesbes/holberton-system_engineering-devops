# postmortem

## Investigating

    On Sunday, at 2:19am PDT 15/05/2021,
    we faced an URGENT AND IMPORTANT problem that led to drop everything in our hands.
    there is a rupture of the our running web server 'nginx'.
    the root cause were a fire in the building just in front of us let to rupture of the electricity of some building including ours

## Timeline

    On Sunday 2:19am PDT 15/05/2021,
    the accident is immediatly detected since
    the power is cut

## Monitoring

    our backup power generor runs as quiqly as possible, but that didnt save us from the rupture of our web server.
    our support team resart the server

## Identified

    the fire led to interruption of the power of all next buidings, but the problem of our system is that we dont have a back up for the running web server

## Corrective and preventative

    for this specific accident we just restart the 'njinx' server and to prevent that from occuring again:
        - we create a monitoring server
        - reduce the single point of failer around the web server
        - maintain and ameliorate the power supply durability
