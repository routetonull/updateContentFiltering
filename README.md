# Meraki Content filtering URL blocking manager

Command-line utility to manage Content filtering URL blocking on [Meraki](https://meraki.cisco.com/) dashboard.

**WARNING: The changes are applied to all the networks of the organization.**

Copyright (c) 2020, Gian Paolo Boarina

## Installation

Clone the repository

    git clone https://github.com/routetonull/updateContentFiltering.git

Install [virtualenv](https://virtualenv.pypa.io/en/latest/).

Create a new virtualenv and activate it

    virtualenv venv
    source venv/bin/activate

Install the module

    pip3 install --editable .

Get API KEY from Meraki dashboard, instructions **[HERE](https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API)**.

Get organization ID using this script (included in the repository)

    ./getOrgID.py --apikey myApiKey

Set *env vars* for API KEY and organization ID. This is not mandatory but makes thing easier.

    export APIKEY=myApiKey
    export ORGID=myOrgID

To leave virtualenv run

    deactivate

## Usage

Add pattern to block list

    updateContentFiltering --apikey $APIKEY --orgid $ORGID --action add --intent block ifconfig.it

Multiple patterns can be added with a comma-separated list

    updateContentFiltering --apikey $APIKEY --orgid $ORGID --action add --intent block ifconfig.it,ifconfig.me,badsite.com

Remove pattern from block list

    updateContentFiltering --apikey $APIKEY --orgid $ORGID --action remove --intent block ifconfig.it

Use flag **--dry** for dry run (no changes applied)

    updateContentFiltering --apikey $APIKEY --orgid $ORGID --action remove --intent block --dry ifconfig.it
