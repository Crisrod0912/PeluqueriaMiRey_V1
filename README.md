# 💈 Peluquería Mi Rey

A family business of **three hairdressers** has decided to acquire their services for the implementation of a system that will allow them to provide a better service.

The working hours are from 8 am to 6 pm, during this time the hair salon can serve 3 clients simultaneously for each reservation or appointment slot.

The men's haircut requires a 30-minute appointment for its execution, the women's haircut requires 1 hour.

Prices vary according to age; a child's haircut will cost half the price of an adult's, and the same applies to senior citizens.

## 🧩 Features

- 🔐 **Login**.
- 📅 **Reservations Module**: This module will ask the customer for the number of people, the age of each person (child or senior citizen), and their preferred reservation time (selecting available times). A reservation number will then be generated. If the number of people making the reservation exceeds the venue's capacity, the system will indicate that there is no space available at the chosen time and that they must select another time. The reservation must also include the selected time, the name of the person who will be assisting them, and a reservation number.
- 🧾 **Billing Module**: It will request the client's name and identification number, as well as the reservation number. With this number and the conditions defined in the reservation, it will create an invoice that must contain the company's information, the details of the client being billed, the reservation details (number of people, condition of each person, schedule and the amount to be paid for each person and for the total invoice).
- 📊 **Reports Module**: It will generate the following reports, for which you must obtain the information from the flat files that were recorded for both reservations and billing.
  - 👥 **Number of people served on the day**: divided by the staff who serve them, their condition (woman-man, child-adult-elderly adult).
  - 💰 **Amount of money generated per day**: divided by (adults- children and senior citizens).
  - 🔥 **Peak hours**: You must indicate the hours and the number of people served during a given period.
  - 💤 **Lowest hours**: You must indicate the hours and the number of people served during a given period.
- 🚪 **Go out**.

## 🛠️ Technologies Used

- 🐍 **Programming language**: Python
- 🌱 **Version Control**: Git

## ⚙️ Installation

### 📋 Prerequisites

- 🐍 [Python IDLE](https://www.python.org/) (recommended: Python 3.14 or higher)
- 💻 [Visual Studio Code](https://code.visualstudio.com/)

### 🔧 Setup

Follow these steps to correctly configure and run the project:

1. 📥 **Clone the repository**

   ```bash
   git clone https://github.com/Crisrod0912/PeluqueriaMiRey_V1.git
   ```

2. 📂 **Open the project folder in VS Code**

   ```bash
   cd PeluqueriaMiRey_V1
   ```

3. ▶️ **Run the project**

- Click on "Run Python File".

> [!NOTE]
> **Project Owner / Developer** 👨🏻‍💻  
>- Cristopher Rodríguez Fernández 
***
