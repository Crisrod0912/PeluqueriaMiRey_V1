# 💈 Peluquería Mi Rey

A family business of **three hairdressers** has decided to acquire their services for the implementation of a system that will allow them to provide a better service to their clients.

🕗 **Working hours:**  
From **8:00 a.m. to 6:00 p.m.**

👥 **Capacity:**  
During this time, the hair salon can serve **3 clients simultaneously** for each reservation or appointment slot.

✂️ **Service duration:**
- Men's haircut: **30 minutes**
- Women's haircut: **1 hour**

💲 **Pricing policy:**
- Children's haircut: **50% of the adult price**
- Senior citizens: **50% of the adult price**

## 🧩 Features

### 🔐 Login
- Basic system access for managing reservations, billing, and reports.

### 📅 Reservations Module
- Requests:
  - Number of people
  - Age category of each person (child, adult, senior citizen)
  - Preferred reservation time (selecting available times)
- Generates:
  - Reservation number
  - Assigned staff member
  - Selected time slot
- Validates capacity:
  - If the number of people exceeds the salon capacity, the system will notify that no space is available and request another time.

### 🧾 Billing Module
- Requests:
  - Client name
  - Identification number
  - Reservation number
- Generates an invoice that includes:
  - Company information
  - Client billing details
  - Reservation details
  - Price per person
  - Total amount to be paid

### 📊 Reports Module
Reports are generated using data obtained from **flat files** created by the reservations and billing modules.

📌 Available reports:
- 👥 **Number of people served per day**
  - Grouped by staff member
  - Grouped by condition (woman, man, child, adult, senior citizen)
- 💰 **Daily income**
  - Divided by adults, children, and senior citizens
- 🔥 **Peak hours**
  - Time slots with the highest number of clients
- 💤 **Lowest demand hours**
  - Time slots with the lowest number of clients

### 🚪 Exit
- Safely exits the system.

---

## 🛠️ Technologies Used

- 🐍 **Programming language:** Python  
- 🌱 **Version Control:** Git  

---

## ⚙️ Installation

### 📋 Prerequisites

- 🐍 [Python](https://www.python.org/) (recommended: Python 3.10 or higher)
- 💻 [Visual Studio Code](https://code.visualstudio.com/)

---

### 🔧 Setup

Follow these steps to correctly configure and run the project:

1. 📥 **Clone the repository**

   ```bash
   git clone https://github.com/Crisrod0912/PeluqueriaMiRey_V1.git
   ```
    
3. 📂 **Open the project folder in VS Code**

   ```bash
   cd PeluqueriaMiRey_V1
   ```

5. ▶️ **Run the project**

- Click on "Run Python File".

> [!NOTE]
> **Project Owner / Developer** 👨🏻‍💻  
>- Cristopher Rodríguez Fernández 
***
