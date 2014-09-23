IAFF ROGUE
==========

A GeoShape plugin for the IAFF.

Installation
------------
Download iaff_geoshape and install it directly from source:

```
git clone <address>
cd iaff_geoshape
python setup.py install
```

Project Configuration
---------------------

Once installed you can configure your project to use
iaff_geoshape with the following steps.

Add ``iaff_geoshape`` to ``INSTALLED_APPS`` in your project's
``settings`` module:

    INSTALLED_APPS = (
        'iaff_geoshape',
        # other apps
    )
