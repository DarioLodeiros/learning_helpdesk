from odoo.tests import common

class TestHelpdeskTicket(common.SavepointCase):
    
    @classmethod
    def setUpClass(self):
        super(TestHelpdeskTicket, self).setUpClass()
        
        helpdesk_ticket = self.env['helpdesk.ticket']
        user_admin = self.env.ref('base.admin')
        user_demo = self.env.ref('base.admin')

        tickets = self.env['res.users']
        self.ticket_test = tickets.create({
            'name': 'Test 1',
            'description': 'Ticket test',
        })


    def test_helpdesk_ticket_number(self):
        self.assertNotEquals(self.ticket.number, '/',
                             'Helpdesk Ticket: A ticket should have '
                             'a number.')
