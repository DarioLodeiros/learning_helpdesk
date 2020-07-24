# -*- coding: utf-8 -*-
# © 2020 Nacho Morales
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, fields, _, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    
    helpdesk_ticket_ids = fields.One2many(
        string='Tickets',
        comodel_name='helpdesk.ticket',
        inverse_name='partner_id',
    )
    
    count_tickets = fields.Integer(
        string='Number of tickets',
        compute='_compute_count_tickets'
    )
    
    @api.multi
    def _compute_count_tickets(self):
        for record in self:
            #REVIEW: use "record.count_tickets = len(record.helpdesk_ticket_ids)" to efficient code
            tickets = self.env['helpdesk.ticket'].search([
                ('partner_id', '=', record.id)
                ])
            record.count_tickets = len(tickets)
            
   
    
    
    