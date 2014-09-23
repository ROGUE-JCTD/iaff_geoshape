IAFF GeoSHAPE
=============

A django plugin to add additional functionality to the IAFF's GeoShape instance.

Installation
------------
Download iaff_geoshape and install it directly from source:

```
git clone https://github.com/ROGUE-JCTD/iaff_geoshape.git
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
