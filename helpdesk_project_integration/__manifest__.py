{
    'name': 'Helpdesk Integration with Project',
    'version': '11.0',
    'author': 'César Castañón',
    'license': 'AGPL-3',
    'description': """
Module to integrate Project inside Helpdesk.
    """,
    'depends': ['project', 'helpdesk_factorlibre'],
    'data': [
        'views/inherit_view_project_kanban.xml'
    ],
    'installable': True
}
