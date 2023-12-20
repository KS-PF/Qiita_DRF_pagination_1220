#add
INSTALLED_APPS = [
    'rest_framework',
    'paginationproject.apps.PaginationprojectConfig',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3
}
