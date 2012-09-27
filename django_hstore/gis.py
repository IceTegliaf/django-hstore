from django.contrib.gis.db.models.sql.query import GeoQuery
from django.db.models.sql.query import Query
from django_hstore.query import HStoreQuerySet

from django.contrib.gis.db.models.query import GeoQuerySet
from django.contrib.gis.db import models as geo_models


class HStoreGeoQuery(GeoQuery, Query):
    pass


class HStoreGeoQuerySet(HStoreQuerySet, GeoQuerySet):
    def __init__(self, model=None, query=None, using=None):
        query = query or HStoreGeoQuery(model)
        super(HStoreGeoQuerySet, self).__init__(model=model, query=query, using=using)



class HStoreGeoManager(geo_models.GeoManager, HStoreManager):
    """
    Object manager combining Geodjango and hstore.
    """
    def get_query_set(self):
        return HStoreGeoQuerySet(self.model, using=self._db)