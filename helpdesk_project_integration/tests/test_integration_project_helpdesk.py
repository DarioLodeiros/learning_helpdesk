# Test ticket associated to a project
'''
def count_ticket_in_project(self):
    -Create the new ticket
    -assign the new ticket to a project
    -button project_ticket_count +1
    -check the count button is right
'''

#Test project_id on helpdesk_ticket
'''
    -Check project_ticket_id = new_ticket_project_id
'''

#Test when the project change, ticket reset
'''
    def test_helpdesk_ticket_project_task(self):
        -Create method onchange
        -Check project_id change
        -If project_id change remove ticket_id 
'''

from odoo.tests import common

@classmethod
class TestHelpdeskTicketProject(common.SavepointCase):
    def setUpClass(cls):
        super(TestHelpdeskTicket, cls).setUpClass()
        
        Ticket = env['helpdesk.ticket']
        Project = env["project.project"]
        
        cls.ticket1 = Ticket.create({
            'name': 'Test 1',
            'description': 'Ticket test1',
        })
        
        cls.ticket2 = Ticket.create({
            'name': 'Test 2',
            'description': 'Ticket test2',
        })
        
        cls.project1 = Project.create({
            "name": "Test Helpdesk-Project 1",
        })
    
        cls.project2 = Project.create({
            "name": "Test Helpdesk-Project 2",
        })
      
        cls.ticket1.write({
            'project_id': cls.project1.id,
        })
        cls.ticket2.write({
            'project_id': cls.project2.id,
        })
        
    def test_helpdesk_ticket_project(self):
        self.assertNotEquals(self.ticket.project, '/',
                             'Helpdesk Ticket: A ticket should have '
                             'a project.')
        
    def test_helpdesk_ticket_counts(self):
        self.assertequal(self.project_id.ticket_count,
                         1,
                         'Helpdesk Ticket: Project assigned '
                         'one ticket')
        
        self.assertequal(self.project_id.ticket_count,
                         2,
                         'Helpdesk Ticket: Project assigned '
                         'two tickets')
        
        self.helpdesk_ticket1.write({
            'stage_id': self.stage_closed.id,
        })
        
        self.assertequal(self.project_id.ticket_count,
                         1,
                         'Helpdesk Ticket: Project assigned '
                         'one ticket')


