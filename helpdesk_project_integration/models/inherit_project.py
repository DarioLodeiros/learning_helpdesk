from odoo import models, fields, api


class Project(models.Model):
    _inherit = "project.project"

    @api.depends('ticket_ids')
    def _compute_tickets_count(self):
        for project in self:
            project.tickets_count = len(
                [ticket for ticket in project.ticket_ids
                 if ticket.stage != 'Cancelled'])

    @api.depends('ticket_ids')
    def _compute_open_tickets_count(self):
        for project in self:
            project.open_tickets_count = len(
                [ticket for ticket in project.ticket_ids
                 if ticket.closed is False])

    ticket_ids = fields.One2many(
        comodel_name='helpdesk.ticket',
        inverse_name='project_id',
        string='Ticket IDs')

    tickets_count = fields.Integer(
        compute='_compute_tickets_count',
        string="Tickets")

    open_tickets_count = fields.Integer(
        compute='_compute_open_tickets_count',
        string='Open Tickets'
    )
