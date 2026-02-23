from models.user import Users
from models.company import Company
from database.session import db
from security.security import hash_password

session = db.get_session()

admin_user = Users(
    login = "admin",
    password = hash_password("admin"),
    user_type = "internal"
)

external_user = Users(
    login = "external",
    password = hash_password("external"),
    user_type = "external"
)

bemol = Company(
    service_type = "pj",
    name="Bemol",
    responsible="admin",
    identity="19829293891",
    social_name="Benchimol",
    profile="Agente de carga",
    direct_invoicing=True,
    path_file="temp_files/ST.png",
    status="PENDING"
)

super_terminais = Company(
    service_type = "pj",
    name="super_terminais",
    responsible="admin",
    identity="123812393891",
    social_name="super_terminais",
    profile="Despachante beneficiário",
    direct_invoicing=True,
    path_file="temp_files/ST.png",
    status="APPROVED"
)

apple = Company(
    service_type = "pj",
    name="apple",
    responsible="admin",
    identity="123145623498",
    social_name="apple",
    profile="Transportadora",
    direct_invoicing=True,
    path_file="temp_files/ST.png",
    status="PENDING"
)

[session.add(rows) for rows in [admin_user, external_user, \
                                              bemol, super_terminais, apple]]
session.commit()