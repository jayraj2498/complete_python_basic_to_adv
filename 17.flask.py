

from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route and a function to handle the route
@app.route('/')
def hello_world():
    
    return ''' <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Your Bootstrap App</title>

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for your website -->
    <!-- Add your custom styles here -->

</head>
<body>

    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="#">Your Logo/Brand</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Services</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="container mt-4">
        <h1>Welcome to Your Bootstrap App!</h1>
        <p>This is a basic Bootstrap starter template. Customize it to fit your needs.</p>
    </div>

    <!-- Bootstrap JS (optional) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

    <!-- Your custom scripts (if any) -->
    <!-- Add your custom scripts here -->

</body>
</html>
  '''

# Run the app if this script is the main program
if __name__ == '__main__':
    app.run(debug=True)

























    
    
# from flask import Flask

# # Create a Flask web application
# app = Flask(__name__)

# # Define a route and a function to handle the route
# @app.route('/')
# def hello_world():
    
#     return ''' <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#     <title>Your Colorful Bootstrap App</title>

#     <!-- Bootstrap CSS -->
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

#     <!-- Custom styles for your website -->
#     <style>
#         body {
#             background-color: #f8f9fa;
#         }

#         .navbar {
#             background-color: #007bff; /* Change this to the color you prefer */
#         }

#         .navbar-dark .navbar-brand {
#             color: #fff;
#         }

#         .navbar-dark .navbar-toggler-icon {
#             background-color: #fff;
#         }

#         .nav-link {
#             color: #fff !important;
#         }

#         .jumbotron {
#             background-color: #28a745; /* Change this to the color you prefer */
#             color: #fff;
#         }

#         .container {
#             background-color: #ffffff;
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
#             margin-top: 20px;
#         }
#     </style>

# </head>
# <body>

#     <!-- Navigation Bar -->
#     <nav class="navbar navbar-expand-lg navbar-dark">
#         <div class="container">
#             <a class="navbar-brand" href="#">Your Logo/Brand</a>
#             <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
#                 <span class="navbar-toggler-icon"></span>
#             </button>
#             <div class="collapse navbar-collapse" id="navbarNav">
#                 <ul class="navbar-nav ml-auto">
#                     <li class="nav-item">
#                         <a class="nav-link" href="#">Home</a>
#                     </li>
#                     <li class="nav-item">
#                         <a class="nav-link" href="#">About</a>
#                     </li>
#                     <li class="nav-item">
#                         <a class="nav-link" href="#">Services</a>
#                     </li>
#                     <li class="nav-item">
#                         <a class="nav-link" href="#">Contact</a>
#                     </li>
#                 </ul>
#             </div>
#         </div>
#     </nav>

#     <!-- Jumbotron -->
#     <div class="jumbotron">
#         <div class="container">
#             <h1 class="display-4">Welcome to Your Colorful Bootstrap App!</h1>
#             <p class="lead">This is a basic Bootstrap starter template with some added colors. Customize it to fit your needs.</p>
#         </div>
#     </div>

#     <!-- Main Content -->
#     <div class="container">
#         <h2>Additional Features</h2>
#         <p>Add more content and features here...</p>
#         <button type="button" class="btn btn-primary">Primary Button</button>
#         <button type="button" class="btn btn-success">Success Button</button>
#         <button type="button" class="btn btn-danger">Danger Button</button>
#     </div>

#     <!-- Bootstrap JS (optional) -->
#     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

# </body>
# </html>
#   '''

# # Run the app if this script is the main program
# if __name__ == '__main__':
#     app.run(debug=True)
