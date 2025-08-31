# alx_travel_app_0x03

This repository contains the **Milestone 5: Setting Up Background Jobs for Email Notifications** project for the **ALX Backend ProDev Program**.  
The project focuses on integrating **Celery with RabbitMQ** into the Django-based `alx_travel_app` to enable **asynchronous background job processing**, specifically for sending booking confirmation emails without blocking the main request-response cycle.

---

## 📌 Project Overview

Modern booking platforms like Booking.com and Airbnb rely on seamless background processes to handle tasks such as **confirmation emails**, **invoice generation**, and **report creation**.  
This milestone ensures that our travel application can send **booking confirmation emails** using **Celery workers** with **RabbitMQ** as the message broker.  

By implementing asynchronous task execution, the app remains responsive while offloading heavy tasks to background workers.

---

## 🎯 Learning Objectives

By completing this project, you will:

- Understand how to integrate **Celery with RabbitMQ** in a Django application.  
- Learn to configure asynchronous task processing for improved performance.  
- Implement an **email notification feature** triggered by user actions.  
- Gain experience with **Django’s email backend** for automated communications.  

---

## ✅ Learning Outcomes

After completing this milestone, you will be able to:

- Configure and run **Celery with RabbitMQ** as a message broker.  
- Create and manage **shared tasks** in Django using Celery.  
- Trigger Celery tasks from **Django views or viewsets**.  
- Test and verify **asynchronous operations** such as sending emails.  

---

## 🔑 Key Concepts

- **Asynchronous Task Processing** → Running time-consuming tasks in the background.  
- **Message Broker (RabbitMQ)** → Middleware that passes task messages between Django and Celery.  
- **Celery Configuration** → Adding `celery.py` and integrating it into `settings.py`.  
- **Shared Tasks** → Functions decorated with `@shared_task` executed by Celery workers.  
- **Email Backend in Django** → Configuring SMTP for sending emails automatically.  

---

## 🛠 Tools and Libraries

- **Django** – Backend web framework.  
- **Celery** – Distributed task queue for background execution.  
- **RabbitMQ** – Message broker for communication.  
- **SMTP Email Backend** – For sending booking confirmation emails.  

---

## 📂 Repository Structure

```bash
alx_travel_app_0x03/
│
├── alx_travel_app/
│   ├── __init__.py
│   ├── settings.py        # Django settings with Celery & email config
│   ├── celery.py          # Celery app configuration
│   └── urls.py
│
├── listings/
│   ├── tasks.py           # Celery tasks (send booking email)
│   ├── views.py           # Django views triggering Celery tasks
│   └── models.py
│
├── README.md              # Project documentation
└── requirements.txt       # Dependencies

