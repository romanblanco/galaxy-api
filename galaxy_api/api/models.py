from django.db import models
from django.db import transaction
from django.urls import reverse

from galaxy_api.auth import models as auth_models


__all__ = ("Namespace", "NamespaceLink")


class Namespace(models.Model):
    """
    A model representing Ansible content namespace.

    Fields:
        name: Namespace name. Must be lower case containing only alphanumeric
            characters and underscores.
        company: Optional namespace owner company name.
        email: Optional namespace contact email.
        avatar_url: Optional namespace logo URL.
        description: Namespace brief description.
        resources: Namespace resources page in markdown format.

    Relations:
        owners: Reference to namespace owners.
        links: Back reference to related links.

    """

    # Fields

    name = models.CharField(max_length=64, unique=True)
    company = models.CharField(max_length=64, blank=True)
    email = models.CharField(max_length=256, blank=True)
    avatar_url = models.CharField(max_length=256, blank=True)
    description = models.CharField(max_length=256, blank=True)
    resources = models.TextField(blank=True)
    groups = models.CharField(max_length=256, default="")

    def __str__(self):
        return self.name

    @transaction.atomic
    def set_links(self, links):
        """Replace namespace related links with new ones."""
        self.links.all().delete()
        self.links.bulk_create(
            NamespaceLink(name=link["name"], url=link["url"], namespace=self)
            for link in links
        )


class NamespaceLink(models.Model):
    """
    A model representing a Namespace link.

    Fields:
        name: Link name (e.g. Homepage, Documentation, etc.).
        url: Link URL.

    Relations:
        namespace: Reference to a parent namespace.
    """

    # Fields
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=256)

    # References
    namespace = models.ForeignKey(
        Namespace, on_delete=models.CASCADE, related_name="links"
    )

    def __str__(self):
        return self.name


class CollectionImport(models.Model):
    """
    A model representing a mapping between pulp task id and task parameters.

    Fields:
        task_id: Task UUID.
        created_at: Task creation date time.
        name: Collection name.
        version: Collection version.

    Relations:
        namespace: Reference to a namespace.
    """
    task_id = models.UUIDField(primary_key=True)

    created_at = models.DateTimeField()

    namespace = models.ForeignKey(Namespace, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, editable=False)
    version = models.CharField(max_length=32, editable=False)

    class Meta:
        ordering = ['-task_id']

    def get_absolute_url(self):
        return reverse('api:v3:collection-imports', args=[str(self.task_id)])
