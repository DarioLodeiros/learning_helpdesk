#Ticket in a project
'''
from odoo.tests import common

@classmethod
class TestHelpdeskTicketProject(common)
    def ticket_in_proyect(self):
        super(TestHelpdeskTicketProject, self).setUpClass()
        
        Ticket = env['helpdesk.ticket']
        Project = env["project.project"]
        
        #ticket belongs to a project
        -we create the new ticket
        self.ticket = Ticket.create({
            'name': 'Test',
            'description': 'Ticket test',
        })
        
        -assign the new ticket to a project
        
        self.project = Project.create({
            'name': 'Test Helpdesk-Project',
        })
        self.ticket.write({
            'project_id': self.project.id,
        })
        
        -button ticket count +1
        self.project.write({
            'ticket_count': self.ticket_count+1
        })
        -check the count of the button is right
    
    def test_helpdesk_ticket_project(self):
        self.assertNotEquals(self.ticket.project_id, 'False',
                             'Helpdesk Ticket: A ticket should have '
                             'a project.')
                             
    def test_helpdesk_ticket_counts(self):
        self.assertequal(self.project_id.ticket_count,
                         1,
                         'Helpdesk Ticket: Project assigned '
                         'one ticket')

        self.helpdesk_ticket.write({
            'stage_id': self.stage_closed.id,
        })

        self.assertequal(self.project_id.ticket_count,
                         1,
                         'Helpdesk Ticket: Project assigned '
                         'one ticket')
'''