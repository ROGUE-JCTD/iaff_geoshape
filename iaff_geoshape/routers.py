
class IAFFGeoRouter(object):
    """
    A router to control all database operations on Geospatial models in the
    IAFF ROGUE application.
    """

    APP_LABEL = 'iaff_geoshape'
    DATABASE = 'geonode_imports'

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == self.APP_LABEL:
            return self.DATABASE
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label == self.APP_LABEL:
            return self.DATABASE
        return None

    def allow_syncdb(self, db, model):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if db == self.DATABASE:
            return model._meta.app_label == self.APP_LABEL
        elif model._meta.app_label == self.APP_LABEL:
            return False
        return None
