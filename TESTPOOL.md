## Login

### 4.1 Valid email/phone and password or valid google authentication:

4.1.1 Valid input for email/phone and matching password:
- Input:
Identifier: "+905540244745", Password: "1234$cdA6578"
- Output:
Status:
"Success"

4.1.2 Valid Google Authentication:
- Input:
"Google-Authentication": "Valid"
- Output:
Status: "Success"

---
### 4.2. Invalid email/phone or password:

4.2.1 Email input does not match:
- Input:
Identifier: "erengazi@gmail.com", Password: "1231234321"
- Output:
Status: "Failed"

4.2.2 Phone input does not match:
- Input:
Identifier: "5333333333, Password: "1231234321"
- Output:
Status: "Failed"

4.2.3 Password does not match with entered email/phone:
- Input:
Identifier: "sahandmoslemi@gmail.com", Password: “1231234321”
- Output:
Status: "Failed"

---
### 4.3. Empty email/phone or password:

4.3.1 Email/phone field is empty:
- Input:
Identifier: “”, Password: “1231234321”
- Output:
Status: "Failed"

4.3.2 Password field is empty:
- Input:
Identifier: "sahandmoslemi@gmail.com", Password: “”
- Output:
Status: "Failed"

---
### 4.4. Wrong format for username:

4.4.1 Email input format is not valid:
- Input:
Identifier: "sahandmoslemi-gmail.com", Password: “12345678”
- Output:
Status: "Failed"

4.4.2 Phone input format is not valid:
- Input:
Identifier: "53a1234567", Password: "12345678"
- Output:
Status: "Failed"

---
### 4.5. Google authentication invalid:

4.5.1 Authentication Fails:
- Input:
"Google-Authentication": "Invalid"
- Output:
Status: "Failed"



