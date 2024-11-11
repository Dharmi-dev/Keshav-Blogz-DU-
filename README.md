# 🚀 Keshav blogz (DU) Project

A modern, feature-rich blog application built with Django, featuring a responsive design with Tailwind CSS and dynamic animations. 



## ✨ Features

- 📱 Responsive design using Tailwind CSS
- 🎨 Modern UI with animations and transitions
- 💬 Comment system
- 📝 Rich text content
- 🔍 SEO-friendly URLs
- 🌈 Dynamic shapes and visual effects

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10+
- pip (Python package manager)
- Git

## 🚀 Getting Started

### 1. Clone the Repository
```bash
https://github.com/4darsh-Dev/Keshav-Diaries-Blog.git
cd Keshav-Diaries-Blog
```

### 2. Set Up Virtual Environment

#### For Unix/macOS:
```bash
# Create virtual environment
python3 -m venv myenv

# Activate virtual environment
source myenv/bin/activate
```

#### For Windows:
```bash
# Create virtual environment
python -m venv myenv

# Activate virtual environment
myenv\Scripts\activate
```

### 3. Install Dependencies
```bash
# Update pip
pip install --upgrade pip

# Install required packages
pip install django
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Create .env file
cp .env.example .env

# Edit .env file with your settings
nano .env
```

### 5. Database Setup
```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser 🎉


## 🔧 Common Commands

```bash
# Create a new app
python manage.py startapp appname

# Make migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver

# Run tests
python manage.py test
```

## 💻 Development

### Adding New Posts
1. Log in to the admin panel at `/admin`
2. Navigate to "Posts" section
3. Click "Add Post"
4. Fill in the required fields
5. Click "Save"

### Customizing Templates
- Base template: `templates/base.html`
- Home page: `templates/home.html`
- Post detail: `templates/post_detail.html`

## 🎨 Customization

### Tailwind CSS
The project uses Tailwind CSS for styling. To customize:
1. Edit the `tailwind.config.js` file
2. Add custom styles in `static/css/custom.css`
3. Run `npm run build` to compile changes

### Adding New Features
1. Create new models in `blog/models.py`
2. Create corresponding views in `blog/views.py`
3. Add URL patterns in `blog/urls.py`
4. Create templates in `blog/templates/`

## 📝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

For support, email your-email@example.com or create an issue in the repository.

## 🌟 Acknowledgments

- Django Documentation
- Tailwind CSS
- Bootstrap
- Font Awesome for icons
- All contributors who help improve the project

---
Made with ❤️ by [Dharmesh Tanwar]
