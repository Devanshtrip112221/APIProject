#  Product CRUD API (Django CBV)

This project is a simple REST-like API built using **Django Class-Based Views (CBV)** and **Django REST Framework utilities**. It allows users to perform CRUD (Create, Read, Update, Delete) operations on Product data.

---

##  Features

* Create a new product
* Retrieve all products or a single product by ID
* Update existing product details
* Delete a product
* JSON-based request and response handling

---

##  Tech Stack

* Python
* Django
* Django REST Framework (Parser & Renderer)
* SQLite (Default Database)

---

## 📁 Project Structure

```
Home/
│── models.py
│── serializers.py
│── views.py
```

---

##  Product Model

The `Product` model contains the following fields:

* `product_name` (CharField)
* `product_image` (ImageField)
* `price` (DecimalField)
* `available_qty` (IntegerField)
* `general_info` (TextField)
* `created_at` (DateTimeField)
* `updated_at` (DateTimeField)

---

##  API Endpoints

### Base URL:

```
http://127.0.0.1:8000/product/
```

---

###  1. Get All Products

* **Method:** GET
* **Request Body:** Not required

**Response:**

```json
[
  {
    "id": 1,
    "product_name": "Sample Product",
    "price": "100.00",
    "available_qty": 10
  }
]
```

---

###  2. Get Single Product

* **Method:** GET

**Request Body:**

```json
{
  "id": 1
}
```

---

###  3. Create Product

* **Method:** POST

**Request Body:**

```json
{
  "product_name": "New Product",
  "price": "200.00",
  "available_qty": 5,
  "general_info": "Sample info"
}
```

---

###  4. Update Product

* **Method:** PUT

**Request Body:**

```json
{
  "id": 1,
  "price": "250.00"
}
```

---

###  5. Delete Product

* **Method:** DELETE

**Request Body:**

```json
{
  "id": 1
}
```

---



##  Important Notes

* CSRF is disabled for testing purposes using `csrf_exempt`.
* `JSONParser` and `JSONRenderer` are used instead of full DRF views.
* Image upload requires proper **MEDIA settings** in Django.

---

##  Future Improvements

* Add authentication (JWT or Token-based)
* Add pagination
* Add filtering and search
* Use Django REST Framework `APIView` or `ViewSets`
* Add proper validation and error handling

---

##  Author

**Devansh Tripathi**

