from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.db.models.loading import get_model
from optparse import make_option


class Command(BaseCommand):
    help = 'Update geospatial data..'
    args = '<serice name>'
    option_list = BaseCommand.option_list + (
        make_option('-s', '--service',
                    dest='service',
                    default='PowerOutage',
                    help='The service to update.'),
    )

    def handle(self, *args, **options):
        service = options.get('service')
        model = get_model('iaff_geoshape', service)
        model.update_data()
        self.stdout.write('Successfully updated the {0} service, there are now: {1} '
                          'features in this service.'.format(service, model.objects.count()))
