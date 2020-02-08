#! /usr/bin/env python3

import django

if __name__ == "__main__":
    django.setup()

from django.db import transaction

from base.helpers.exceptions import DryRunException
from organization.models.club import Club

CLUBS = [
    ('ATL','Atlanta United FC',1),
    ('CHI','Chicago Fire',1),
    ('CIN','FC Cincinnati',1),
    ('CLB','Columbus Crew SC',1),
    ('COL','Colorado Rapids',1),
    ('DAL','FC Dallas',1),
    ('DC','D.C. United',1),
    ('HOU','Houston Dynamo',1),
    ('LAFC','Los Angeles FC',1),
    ('LAG','Los Angeles Galaxy',1),
    ('MIN','Minnesota United FC',1),
    ('MTL','Montreal Impact',1),
    ('NE','New England Revolution',1),
    ('NYC','New York City FC',1),
    ('NYRB','New York Red Bulls',1),
    ('ORL','Orlando City SC',1),
    ('PHI','Philadelphia Union',1),
    ('POR','Portland Timbers',1),
    ('RSL','Real Salt Lake',1),
    ('SEA','Seattle Sounders FC',1),
    ('SJ','San Jose Earthquakes',1),
    ('SKC','Sporting Kansas City',1),
    ('TOR','Toronto FC',1),
    ('VAN','Vancouver Whitecaps FC',1)
]


def main(args):
    for club in CLUBS:
        created_club = Club.objects.create(
            club_id=club[0],
            name=club[1],
            is_active=True if club[2] == 1 else False
        )
        print(created_club.id)
        


if __name__ == '__main__':
    
    import argparse

    parser = argparse.ArgumentParser(
        description="A script to backfill MLS clubs based on Jay's SQL dump."
    )

    parser.add_argument('--commit', required=False, action='store_true')

    args = parser.parse_args()

    with transaction.atomic():
        main(args)
        if not args.commit:
            raise DryRunException()
