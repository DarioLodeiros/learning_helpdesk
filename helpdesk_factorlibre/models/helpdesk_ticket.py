# © 2020 Alberto Esteban
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

#Imports
from odoo import models, fields, _, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    name = fields.Char(
        string='Tittle',
        required=True,
    )
    description = fields.Html(
        string='Description',
    )
    assigned_date = fields.Datetime(
        string='Assigned Date',
        compute='_compute_assigned_date',
        store=True,
        )
    
    closed_date = fields.Datetime(string='Closed Date')
    
    priority = fields.Selection(selection=[
        ('0', _('Low')),
        ('1', _('Medium')),
        ('2', _('High')),
        ], 
        string='Priority',
    )
    ticket_number = fields.Integer(
        string='Ticket number',
    )
    user_id = fields.Many2one(
        string = "asigned to",
        comodel_name = "res.users",
        ondelete = "restrict"
    )
    user_ids = fields.Many2many(
        comodel_name='res.users',
        related='team_id.user_ids',
        string='Users',
        
    )
    partner_id = fields.Many2one(
        string = "Customer",
        comodel_name = "res.partner",
        ondelete="restrict",
    )
    partner_name = fields.Char(
        string = "Customer Name",
    )
    partner_mail = fields.Char(
        string = "Customer Mail",
    )
    
    tag_ids = fields.Many2many(
        string = "Tags",
        comodel_name = "helpdesk.ticket.tag",
    )
    
    team_id = fields.Many2one(
        'helpdesk.ticket.team',
        ondelete='restrict'
    )
    
    unattended = fields.Boolean(related='stage_id.unattended')
    
    color = fields.Integer(string='Color Index')
    
    team_ids = fields.Many2many(
        string='Team',
        comodel_name='helpdesk.ticket.team',
    )
    
    helpdesk_ticket_ids = fields.One2many(
        string='Tickets',
        comodel_name='helpdesk.ticket',
        inverse_name='user_id'
    )
    
    count_open_tickets = fields.Integer(
        string='Number of tickets',
        compute='_compute_count_tickets'
    )
    
    def _compute_count_tickets(self):
        for record in self:
            tickets = self.env.search(
                [('user_id', '=', record.id)])
            record.count_open_tickets = len(
                tickets.filtered(lambda ticket: ticket.stage_id.closed == False))
    
    @api.multi
    def assign_to_me(self):
        self.write({'user_id': self.env.user.id})
        
    
        
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for record in self:
            partner = record.partner_id
            if partner:
                record.update({
                    'partner_name': partner.name,
                    'partner_mail': partner.email,
                })
                
    @api.depends('user_id')
    def _compute_assigned_date(self):
        self.assigned_date = fields.Datetime.now()
        
        
    @api.model
    def create(self,vals):
        if vals.get("partner_id") and ("partner_name" not in vals or "partner_mail" not in vals):
            partner = self.env["res.partner"].browse(vals["partner_id"])
            vals.setdefault("partner_name", partner.name)
            vals.setdefault("partner_mail", partner.email)
            
        res = super().create(vals)
        return res
    
    @api.multi 
    @api.onchange('team_id')
    def onchange_user_id(self):
        for record in self:
            least_open_tickets_users = self.env['res.users'].search(
                [('team_id', '=', record.team_id.id)], limit=1
            )
            if record.team_id.id not in [team.id for team in record.team_ids]:
                record.update({
                    'user_id': least_open_tickets_users.id
                })
                           
    @api.multi
    @api.onchange('user_id')
    def onchange_team_id(self):
        for record in self:
            theTeam = self.env['helpdesk.ticket.team'].search(
                [('teamId', '=', record.team_id.teamId)], limit=1)
            if theTeam:
                record.update({
                    'team_id': theTeam.id
                })
    
