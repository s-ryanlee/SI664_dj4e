import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # name,description,justification,year,longitude,latitude,area_hectares,category,state,region,iso

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        i, created = Iso.objects.get_or_create(name=row[10])
        r, created = Region.objects.get_or_create(name=row[9])

        try:
            y = int(row[3])
            lat = float(row[4])
            long = float(row[5])
            area = float(row[6])
        except:
            y = None
            lat = None
            long = None
            area = None

        site = Site(
            name=row[0], year=y, latitude=lat, longitude=long,
            description=row[1], justification=row[2], area_hectares=area,
            category=c, region=r, iso=i, state=s
            )

        site.save()
