
from app import app
from models import db, UserModel, CategoryModel, ProductModel, ReviewModel,OrderModel

users=[{
  "id": 1,
  "username": "rbridson0",
  "email": "dkillich0@bravesites.com",
  "phone_number": "244-678-6901",
  "role": "member",
  "password": "qE8/LmHzx\"M1D0<Z"
}, {
  "id": 2,
  "username": "bmatchett1",
  "email": "afellgett1@theglobeandmail.com",
  "phone_number": "409-932-4362",
  "role": "member",
  "password": "mL4_Oq!k@2"
}, {
  "id": 3,
  "username": "bnuttey2",
  "email": "rbulter2@google.de",
  "phone_number": "673-861-2497",
  "role": "member",
  "password": "lP4!Tj>GahbKoz~}"
}, {
  "id": 4,
  "username": "sgiacopetti3",
  "email": "acoslitt3@oracle.com",
  "phone_number": "257-619-9308",
  "role": "member",
  "password": "oN3>Sd_!oM`M97ri"
}, {
  "id": 5,
  "username": "cabrami4",
  "email": "hmatz4@mlb.com",
  "phone_number": "942-904-6178",
  "role": "member",
  "password": "qO8(59FfGW)"

}, {
  "id": 6,
  "username": "mcastaner5",
  "email": "gdogerty5@adobe.com",
  "phone_number": "212-373-9841",
  "role": "member",
  "password": "kT8+p01+"
}, {
  "id": 7,
  "username": "tandreassen6",
  "email": "mbradder6@google.com.au",
  "phone_number": "597-166-0352",
  "role": "member",
  "password": "mR4$a)EsC3"
}, {
  "id": 8,
  "username": "arollason7",
  "email": "scheley7@theguardian.com",
  "phone_number": "922-383-2230",
  "role": "member",
  "password": "aL4}M0g56#|!=<e>"
  
}, {
  "id": 9,
  "username": "sludgrove8",
  "email": "pgopsall8@npr.org",
  "phone_number": "762-805-9069",
  "role": "member",
  "password": "sJ5~LULFGDl_6'"

}, {
  "id": 10,
  "username": "olebell9",
  "email": "rraymond9@trellian.com",
  "phone_number": "658-562-3424",
  "role": "member",
  "password": "jL8'0iJlAQ/>s"
}]

products=[{
  "id": 1,
  "user_id": 1,
  "title": "Reilly Inc",
  "description": "Switchable content-based hub",
  "price": 83,
  "category_id": 1
}, {
  "id": 2,
  "user_id": 2,
  "title": "Glover, Schmitt and O'Reilly",
  "description": "Centralized full-range model",
  "price": 44,
  "category_id": 2
}, {
  "id": 3,
  "user_id": 3,
  "title": "Rosenbaum-Wintheiser",
  "description": "Multi-channelled encompassing frame",
  "price": 63,
  "category_id": 3
}, {
  "id": 4,
  "user_id": 4,
  "title": "Ernser, Murray and Rohan",
  "description": "Customer-focused grid-enabled synergy",
  "price": 42,
  "category_id": 4
}, {
  "id": 5,
  "user_id": 5,
  "title": "Satterfield, Gutkowski and Spinka",
  "description": "Managed encompassing groupware",
  "price": 68,
  "category_id": 5
}, {
  "id": 6,
  "user_id": 6,
  "title": "Dibbert-Braun",
  "description": "Reactive responsive architecture",
  "price": 91,
  "category_id": 6
}, {
  "id": 7,
  "user_id": 7,
  "title": "Schuster-Wiza",
  "description": "Inverse tangible model",
  "price": 83,
  "category_id": 7
}, {
  "id": 8,
  "user_id": 8,
  "title": "Zboncak-Leuschke",
  "description": "Persevering optimal forecast",
  "price": 83,
  "category_id": 8
}, {
  "id": 9,
  "user_id": 9,
  "title": "Dickinson, Trantow and Brown",
  "description": "Up-sized asynchronous collaboration",
  "price": 30,
  "category_id": 9
}, {
  "id": 10,
  "user_id": 10,
  "title": "Gleason LLC",
  "description": "Reactive contextually-based encryption",
  "price": 31,
  "category_id": 10
}]

categories=[{
  "id": 1,
  "name": "Domainer"
}, {
  "id": 2,
  "name": "Bigtax"
}, {
  "id": 3,
  "name": "Redhold"
}, {
  "id": 4,
  "name": "Konklux"
}, {
  "id": 5,
  "name": "Regrant"
}, {
  "id": 6,
  "name": "Greenlam"
}, {
  "id": 7,
  "name": "Y-Solowarm"
}, {
  "id": 8,
  "name": "Vagram"
}, {
  "id": 9,
  "name": "Temp"
}, {
  "id": 10,
  "name": "Wrapsafe"
}]


reviews=[{
  "id": 1,
  "user_id": 1,
  "product_id": 1,
  "text": "Tracheal reconstruction",
  "rating": 1
}, {
  "id": 2,
  "user_id": 2,
  "product_id": 2,
  "text": "Adrenal lesion excision",
  "rating": 2
}, {
  "id": 3,
  "user_id": 3,
  "product_id": 3,
  "text": "Lengthen 1 extraoc musc",
  "rating": 3
}, {
  "id": 4,
  "user_id": 4,
  "product_id": 4,
  "text": "Arterial bld gas measure",
  "rating": 4
}, {
  "id": 5,
  "user_id": 5,
  "product_id": 5,
  "text": "Coron vess aneurysm rep",
  "rating": 5
}, {
  "id": 6,
  "user_id": 6,
  "product_id": 6,
  "text": "Scan of other sites",
  "rating": 6
}, {
  "id": 7,
  "user_id": 7,
  "product_id": 7,
  "text": "Breast implant removal",
  "rating": 7
}, {
  "id": 8,
  "user_id": 8,
  "product_id": 8,
  "text": "Brain meninge repair NEC",
  "rating": 8
}, {
  "id": 9,
  "user_id": 9,
  "product_id": 9,
  "text": "Other suture of tendon",
  "rating": 9
}, {
  "id": 10,
  "user_id": 10,
  "product_id": 10,
  "text": "Ovarian operation NEC",
  "rating": 10
}]
orders=[{
  "id": 1,
  "user_id": 1,
  "product_id": 1,
  "total_price": 67,
  "status": "on-route"
}, {
  "id": 2,
  "user_id": 2,
  "product_id": 2,
  "total_price": 82,
  "status": "on-route"
}, {
  "id": 3,
  "user_id": 3,
  "product_id": 3,
  "total_price": 49,
  "status": "pending"
}, {
  "id": 4,
  "user_id": 4,
  "product_id": 4,
  "total_price": 52,
  "status": "deliverd"
}, {
  "id": 5,
  "user_id": 5,
  "product_id": 5,
  "total_price": 2,
  "status": "pending"
}, {
  "id": 6,
  "user_id": 6,
  "product_id": 6,
  "total_price": 20,
  "status": "deliverd"
}, {
  "id": 7,
  "user_id": 7,
  "product_id": 7,
  "total_price": 34,
  "status": "pending"
}, {
  "id": 8,
  "user_id": 8,
  "product_id": 8,
  "total_price": 57,
  "status": "pending"
}, {
  "id": 9,
  "user_id": 9,
  "product_id": 9,
  "total_price": 27,
  "status": "deliverd"
}, {
  "id": 10,
  "user_id": 10,
  "product_id": 10,
  "total_price": 37,
  "status": "pending"
}]


with app.app_context():
    # db.session.add_all([UserModel(**user) for user in users])
    # db.session.add_all([ProductModel(**product) for product in products])
    # db.session.add_all([CategoryModel(**category) for category in categories])
    # db.session.add_all([ReviewModel(**review) for review in reviews])
    db.session.add_all([OrderModel(**order) for order in orders])
    db.session.commit()