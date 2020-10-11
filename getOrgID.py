#!/usr/bin/env python3

import click
import os
import meraki
import logging

"""
Optional: export env vars to access Meraki dashboard

    export APIKEY=myApiKey
"""


@click.command(help="List Organization ID accessible via API KEY")
@click.option(
    "--apikey",
    required=True,
    prompt=True,
    help="API Key",
    default=os.environ.get("APIKEY", ""),
)
def main(apikey):

    m = meraki.DashboardAPI(
        api_key=apikey, print_console=False, output_log=False, suppress_logging=True
    )
    try:
        orgs = m.organizations.getOrganizations()
        for org in orgs:
            click.echo(f"ORG ID: {org.get('id'):20}ORG NAME: {org.get('name')}")
    except:
        click.echo(click.style(f"\n❌ ❌ ❌ ERROR READING ORGS - Verify API KEY is valid ❌ ❌ ❌\n", fg="red",))

main()
