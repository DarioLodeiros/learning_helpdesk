# Test project_id on helpdesk_ticket

### Arrange:
new_ticket = {ticket with project_id = a}
ticket.write(new_ticket)

project_ticket_id = search project_id in project where ticket_id = new_ticket.project_id

###Assert
project_ticket_id = new_ticket.project_id

# Test ticket counter button:

## Onchange method:

###Arrange
new_ticket = {ticket with project_id = a}
ticket.write(new_ticket)

tickets_a_count = (ticket_count_field where project_id = a)
tickets_b_count = (ticket_count_field where project_id = b)

new_ticket update: new_ticket.project_id = b

call: new_ticket onchange method

###Assert
tickets_a_count -1 = (ticket_count_field where project_id = a)
tickets_b_count +1 = (ticket_count_field where project_id = b)


# Test Smartbuttons on projects form view:

###Arrange:
open_tickets_count_field = project.project_id.open_tickets_count
tickets_count_field = project.project_id.all_tickets_count
open_tickets_by_project = helpdesk_ticket.search(where project.project_id = helpdesk_project_id and ticket is not closed)
tickets_by_project = helpdesk_ticket.search(where project.project_id = helpdesk_project_id)

###Assert
ticket_count_field = len(tickets_by_project)
open_tickets_count_field = len(open_tickets_count_field)

