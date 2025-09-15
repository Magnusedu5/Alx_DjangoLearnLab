

# 📖 API Documentation

## 🔐 Authentication

All endpoints require **JWT / Session Authentication** (depending on your setup).
Add the token in headers:

```
Authorization: Bearer <your_token>
```

---

## 👤 Accounts API

### 1. Follow a User

**Endpoint:**

```
POST /api/accounts/follow/{user_id}/
```

**Description:**
Follow another user.

**Permissions:**

* Must be authenticated.
* Cannot follow yourself.

**Request Example:**

```
POST /api/accounts/follow/5/
```

**Response (200):**

```json
{
  "detail": "You are now following alice."
}
```

**Error (400):**

```json
{
  "detail": "You cannot follow yourself."
}
```

---

### 2. Unfollow a User

**Endpoint:**

```
POST /api/accounts/unfollow/{user_id}/
```

**Description:**
Unfollow a user.

**Permissions:**

* Must be authenticated.
* Cannot unfollow yourself.

**Request Example:**

```
POST /api/accounts/unfollow/5/
```

**Response (200):**

```json
{
  "detail": "You have unfollowed alice."
}
```

---

### 3. List Following

**Endpoint:**

```
GET /api/accounts/following/
```

**Description:**
Get a list of users the current user is following.

**Permissions:**

* Must be authenticated.

**Response Example:**

```json
[
  {
    "id": 5,
    "username": "alice"
  },
  {
    "id": 8,
    "username": "bob"
  }
]
```

---

### 4. List Followers

**Endpoint:**

```
GET /api/accounts/followers/
```

**Description:**
Get a list of users who follow the current user.

**Permissions:**

* Must be authenticated.

**Response Example:**

```json
[
  {
    "id": 12,
    "username": "charlie"
  }
]
```

---

## 📰 Posts API

### 5. Feed

**Endpoint:**

```
GET /api/posts/feed/
```

**Description:**
Fetch posts from users the current user follows, ordered by most recent first.

**Permissions:**

* Must be authenticated.

**Response Example:**

```json
[
  {
    "id": 21,
    "author": 5,
    "author_username": "alice",
    "content": "Excited to start a new project!",
    "created_at": "2025-09-15T10:30:00Z"
  },
  {
    "id": 19,
    "author": 8,
    "author_username": "bob",
    "content": "Django REST framework makes APIs easy 😍",
    "created_at": "2025-09-14T19:20:00Z"
  }
]
