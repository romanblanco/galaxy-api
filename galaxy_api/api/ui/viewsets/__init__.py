from .namespace import NamespaceViewSet, MyNamespaceViewSet
from .collection import CollectionViewSet, CollectionVersionViewSet, CollectionImportViewSet
from .tags import TagsViewSet
from .group import GroupViewSet
from .current_user import CurrentUserViewSet

__all__ = (
    'NamespaceViewSet',
    'MyNamespaceViewSet',
    'CollectionViewSet',
    'CollectionVersionViewSet',
    'CollectionImportViewSet',
    'TagsViewSet',
    'CurrentUserViewSet',
    'GroupViewSet',
)
