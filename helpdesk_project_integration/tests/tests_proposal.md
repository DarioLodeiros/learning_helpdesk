# Setup:

create new ticket assigned to a project x

# Test 1: Check relational fields between project_id and helpdesk_ticket

assert new ticket id is in project x ticket ids.

# Test 2: Check ticket count by project:

var a = call func -> number of tickets on project x

update new_ticket: change from project x to project y

var b = call func -> number of tickets on project x

assert var a - 1 = var b

# Test 3: Check open tickets count by project:

var a = call func -> number of tickets not closed on project x

close new_ticket

var b = call func -> number of tickets not closed on project x

assert var a - 1 = var b
