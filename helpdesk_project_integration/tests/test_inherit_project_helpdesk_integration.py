from odoo.tests import common


class TestProjectIntegration(common.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super(TestProjectIntegration, cls).setUpClass()
        project = cls.env['project']
        helpdesk_ticket = cls.env['helpdesk.ticket']
        cls.project_1 = project.create({
            'name': 'Project Test 1',
            'sequence': 1
        })
        cls.project_2 = project.create({
            'name': 'Project Test 2',
            'sequence': 2
        })
        cls.ticket = helpdesk_ticket.create({
            'name': 'Test 1',
            'description': 'Ticket test',
            'project_id': cls.project_1.id
        })
        tickets_on_project_id_1 = self.project.search(
            ['id', '=', cls.project_1.id]).ticket_ids

        tickets_on_project_id_2 = self.project.search(
            ['id', '=', cls.project_2.id]).ticket_ids

    def test_helpdesk_ticket_project_id(self):
        """
        Check relational fields between project_id and helpdesk_ticket
        """

        self.assertIn(self.ticket.project_id,
                      self.tickets_on_project_id_1,
                      f"ticket id {self.ticket.id} not in project\
                      {self.project_1.name}")

    def test_helpdesk_ticket_count_by_project(self):
        """
        Check ticket count by project
        """
        tickets_on_project_id_1 = self.tickets_on_project_id_1

        tickets_on_project_id_2 = self.tickets_on_project_id_2

        self.ticket.write({
            'project_id': self.project_2.id
        })

        self.assertEqual(len(self.tickets_on_project_1) - 1,
                         len(tickets_on_project_id_1),
                         f"Number of ticket on {self.project_1} is not correct")

        self.assertEqual(len(self.tickets_on_project_2) + 1,
                         len(tickets_on_project_id_2),
                         f"Number of ticket on {self.project_2} is not correct")

    def test_helpdesk_ticket_count_open_by_project(self):

        tickets_on_project_id_1 = self.tickets_on_project_id_1.filtered

        tickets_on_project_id_2 = self.tickets_on_project_id_2.filtered
