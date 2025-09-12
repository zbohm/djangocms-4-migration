from cms.models import PageUrl
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Fix page id duplicities."

    def handle(self, *args, **options):
        data = []
        self.stdout.write("Delete duplicates urls.")
        self.stdout.write("Lang Pid  Slug:                     Path:                     Page:")
        for pur in PageUrl.objects.all().order_by("page_id"):
            key = (pur.language, pur.page_id)
            if key in data:
                self.stdout.write(f" - {pur.language} {pur.page_id:>2}  {pur.slug:<24}  {pur.path:<24}  {pur}")
                pur.delete()
            data.append(key)
