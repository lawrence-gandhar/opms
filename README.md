# OPMS
**Performance Management System in Django**

**Database Engine :** PostgreSQL

### Models Overview
> User Model:

User model is extended to add department, designation, location, display_name and usertype.


> Usertype Model:

This model defines the different roles for the users. Such as agents, managers, supervisors and hr. You can assign a user to a specific usertype. For example, an agent reports to a supervisor, a supervisor to his manager and a manager to his boss. There is a field known as access, this field allows to set access for a usertype to view records of the usertypes assigned to it. 


> Location Model:

You can add multiple locations with the same name but the abbr should be unique. For example, if you added a city, and there are multiple branches across different locations in the same city. Then use postcodes / zipcodes as abbr. This will keep each location unique and easy to assign it to the related models. 


> Department Model:

A Department can be a parent department with multiple departments assigned to it. In the add user form, the department section has two dropdowns. First dropdown shows the parent department in assigned location. You may also find departments that are not assigned to any locations. It means that the department is available for all locations. On the parent department select, the second dropdown is populated with the departments assigned to the selected parent department.


