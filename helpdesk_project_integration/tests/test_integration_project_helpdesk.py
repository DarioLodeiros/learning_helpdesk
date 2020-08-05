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
    def setUpClass(self):
        super(TestHelpdeskTicket, self).setUpClass()
        
        Ticket = env['helpdesk.ticket']
        Project = env["project.project"]
        
        self.ticket1 = Ticket.create({
            'name': 'Test 1',
            'description': 'Ticket test1',
        })
        
        self.ticket2 = Ticket.create({
            'name': 'Test 2',
            'description': 'Ticket test2',
        })
        
        self.project1 = Project.create({
            "name": "Test Helpdesk-Project 1",
        })
    
        self.project2 = Project.create({
            "name": "Test Helpdesk-Project 2",
        })
      
        self.ticket1.write({
            'project_id': self.project1.id,
        })
        self.ticket2.write({
            'project_id': self.project2.id,
        })
        
    def test_helpdesk_ticket_project(self):
        self.assertNotEquals(self.ticket.project_id, 'False',
                             'Helpdesk Ticket: A ticket should have '
                             'a project.')
        
    def test_open_ticket_count(self):
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


