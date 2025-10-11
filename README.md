# 📄 DocsApp - Documentation Management System

A Django web application for managing documents, orders, and related processes in an enterprise environment. This pet project was developed as a 3-month internship project and covers the full documentation lifecycle from creation and editing to Excel report generation.

## ✨ Features

### 📋 Document & Order Management
- Create, edit, and delete documents and orders
- Associate with workshops, document types, and employees

### 👥 Employee Management
- Track employees who have/haven't familiarized themselves with documents
- Monitor employee status (on vacation, active, etc.)

### 🔄 Process & Action Management
- Add processes to documents and orders
- Monitor action completion and deadlines

### 📊 Reporting System
- Reports on employees who haven't familiarized with documents
- Reports on incomplete processes
- Reports on outdated documents
- Individual employee reports
- Complete workshop reports
- **Excel (.xlsx) export** for all reports

## 🛠️ Tech Stack

- **Python 3.x**
- **Django 4.x**
- **OpenPyXL** - Excel report generation
- **Pandas** - data analysis

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/autozavod-docs.git
cd autozavod-docs


 Implementation Details
Class-based views for clear and maintainable code

Session management for workshop selection

Dynamic Excel report generation using OpenPyXL

AJAX integration for employee familiarization tracking (no page reload)
