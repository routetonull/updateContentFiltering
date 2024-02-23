# Meraki Content filtering URL blocking manager

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/routetonull/updateContentFiltering)

Command-line utility to manage Content filtering URL blocking on [Meraki](https://meraki.cisco.com/) dashboard.

Copyright (c) 2024, Gian Paolo Boarina

## Installation

Clone the repository

    git clone https://github.com/routetonull/updateContentFiltering.git

Create a new virtualenv and activate it

    cd updateContentFiltering
    python3 -m venv venv
    source venv/bin/activate

Install the module

    pip3 install .

Get the API KEY from Meraki dashboard, instructions **[HERE](https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API)**.


Set *env var* for API KEY. This is not mandatory but makes things easier.

    export APIKEY=myApiKey
    
Get the Organization ID using this script (included in the repository)

    getOrgID --apikey $APIKEY

Set *env var* for the Organization. This is not mandatory but makes things easier.

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

Option **--filternetwork** filters networks that in include a string in the name

    updateContentFiltering --apikey $APIKEY --orgid $ORGID --action remove --intent block --dry --filternetwork EMEA-IT ifconfig.it 
