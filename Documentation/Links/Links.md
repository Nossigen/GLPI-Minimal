# Links

---

## Utilisateurs

root = /user/

### Matériel

#### Liste

/user/<id>/objets/list

#### Plus d'informations

/user/<id>/objets/<id_objet>/informations

/user/<id>/objets/<id_objet>/documentation

### Tickets

#### Liste

/user/<id>/tickets/
/user/<id>/tickets/list

/user/<id>/tickets/resolved/
/user/<id>/tickets/resolved/list

#### Gestion

/user/<id>/tickets/new

/user/<id>/tickets/<id>/respond

/user/<id>/tickets/<id>/delete

---

## Admin

root = /admin

### Utilisateurs

#### Liste d´utilisateurs

/admin/manager/user/
/admin/manage/user/list/

/admin/manage/user/list/job/<id>
/admin/manage/user/list/role/<id>

#### Utilisateur specifique

/admin/manage/user/<id>

#### Liste travail

/admin/manager/job/
/admin/manager/job/list

#### Edition

/admin/manage/job/new -> create

/admin/manage/job/<id>/edit -> edit/delete

### Matériel

#### Liste materiel

/admin/manage/object/list
/admin/manage/object/list/<id_type>
/admin/manage/object/list/accessory

#### Edition

/admin/manage/object/new
/admin/manage/object/<id>/edit

/admin/manage/object_type/new
/admin/manage/object_type/<id>/edit

### Fournisseurs

#### Liste

/admin/manage/vendor/
/admin/manage/vendor/list

#### Edition

/admin/manage/vendor/new
/admin/manage/vendor/<id>/edit

#### Commande

/admin/manage/command/new
/admin/manage/command/<id>/change_status