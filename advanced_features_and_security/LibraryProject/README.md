Django library project.

Permissions and Group Configuration
Groups:
    - Viewers: Access to can_view. Can only see the book list.
    - Editors: Access to can_view, can_createm and can_edit. Can only add and modify entries but cannot remove them.
    - Admins: Full access including can_delete

Logic:> Permisssions are enforced at the view level using Django's @permission_required decorator. If a user lacks the permission, a '403 Forbidden' error is rais (raise_exception=True)