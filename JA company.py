# JA Company Program - EcoPins Website
# Student Project - Made with Python

print("Creating EcoPins Website...")
print("This website was made by a student")
print("Using Python programming")


STUDENT_NAME = "Avin P. Langroodi"


TEAM_MEMBERS = [
    {"name": "Avin P. Langroodi", "role": "VP information technology"},
    {"name": "Sajal Aryal", "role": "VP internal"},
    {"name": "Alden Hiltz", "role": "VP External"},
    {"name": "Manuela Roemer", "role": "VP Production"},
    {"name": "Louis Goossens", "role": "VP Marketing"},
    {"name": "Henry Hiltz", "role": "VP Sales"},
    {"name": "Dylan Davidson", "role": "VP Human Resources"},
    {"name": "Sophia Langille", "role": "VP Corporate Social Responsibility"},
    {"name": "Maggie Pyke", "role": "VP Finance"},
    {"name": "Alexander Bautista", "role": "VP Environment"},
    {"name": "Michael Aucoin", "role": "VP Health & Safety"},
    {"name": "Lily Bray", "role": "Head of Video Production & Special Events"}
]

HTML_CONTENT = """
<!DOCTYPE html>
<html>
<head>
    <title>EcoPins - JA Company</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .header {
            background: rgba(255, 255, 255, 0.95);
            padding: 30px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }
        
        .main-title {
            color: #2c3e50;
            font-size: 42px;
            margin: 0;
            font-weight: bold;
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .subtitle {
            color: #7f8c8d;
            font-size: 20px;
            margin: 15px 0;
            font-weight: 500;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .card {
            background: rgba(255, 255, 255, 0.95);
            padding: 30px;
            margin: 25px 0;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            border: none;
            transition: all 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 35px rgba(0,0,0,0.2);
        }
        
        .about-card {
            background: linear-gradient(135deg, #FFEAA7, #fab1a0);
        }
        
        .features-card {
            background: linear-gradient(135deg, #81ECEC, #74B9FF);
        }
        
        .future-card {
            background: linear-gradient(135deg, #FD79A8, #a29bfe);
        }
        
        .student-card {
            background: linear-gradient(135deg, #55EFC4, #00b894);
        }
        
        .team-card {
            background: linear-gradient(135deg, #FDCB6E, #e17055);
        }
        
        .designs-card {
            background: linear-gradient(135deg, #a29bfe, #fd79a8);
        }
        
        .quiz-card {
            background: linear-gradient(135deg, #FF9A8B, #FF6A88);
        }
        
        h2 {
            color: #2c3e50;
            font-size: 28px;
            margin-top: 0;
            text-align: center;
            padding-bottom: 15px;
            border-bottom: 3px solid rgba(255,255,255,0.5);
        }
        
        .feature-list {
            list-style: none;
            padding: 0;
        }
        
        .feature-list li {
            padding: 15px;
            margin: 10px 0;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 10px;
            font-weight: bold;
            color: #2c3e50;
            border-left: 5px solid #e17055;
        }
        
        .future-feature {
            text-align: center;
            font-size: 22px;
            color: #2c3e50;
            font-weight: bold;
            margin: 20px 0;
            padding: 20px;
            background: rgba(255, 255, 255, 0.4);
            border-radius: 12px;
            border: 2px dashed rgba(255,255,255,0.8);
        }
        
        .student-note {
            background: rgba(255, 255, 255, 0.3);
            padding: 20px;
            border-radius: 12px;
            margin: 15px 0;
            text-align: center;
            font-style: italic;
            color: #2c3e50;
            font-size: 18px;
        }
        
        .signature {
            text-align: center;
            margin-top: 40px;
            padding: 25px;
            background: linear-gradient(135deg, #dfe6e9, #b2bec3);
            border-radius: 15px;
            font-weight: bold;
            color: #2c3e50;
            box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        }
        
        .creator-name {
            font-size: 24px;
            color: #0984e3;
            margin: 10px 0;
        }
        
        .contact-info {
            margin: 15px 0;
            padding: 15px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 10px;
            display: inline-block;
        }
        
        .contact-link {
            color: #0984e3;
            text-decoration: none;
            font-weight: bold;
            margin: 0 10px;
            padding: 8px 15px;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.5);
            transition: all 0.3s ease;
        }
        
        .contact-link:hover {
            background: rgba(255, 255, 255, 0.8);
            transform: scale(1.05);
        }
        
        .email-link {
            color: #d63031;
            text-decoration: none;
            font-weight: bold;
            margin: 0 10px;
            padding: 8px 15px;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.5);
            transition: all 0.3s ease;
            border: 1px solid #d63031;
        }
        
        .email-link:hover {
            background: rgba(214, 48, 49, 0.1);
            transform: scale(1.05);
        }

        .company-email-link {
            color: #27ae60;
            text-decoration: none;
            font-weight: bold;
            margin: 0 10px;
            padding: 12px 25px;
            border-radius: 25px;
            background: linear-gradient(45deg, #27ae60, #2ecc71);
            color: white;
            transition: all 0.3s ease;
            display: inline-block;
            box-shadow: 0 4px 15px rgba(39, 174, 96, 0.3);
            border: 2px solid rgba(255,255,255,0.5);
        }
        
        .company-email-link:hover {
            background: linear-gradient(45deg, #2ecc71, #27ae60);
            transform: scale(1.1);
            box-shadow: 0 6px 20px rgba(39, 174, 96, 0.4);
        }
        
        .team-button {
            background: linear-gradient(45deg, #e17055, #fd79a8);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            margin: 15px;
            transition: all 0.3s ease;
            font-weight: bold;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        .team-button:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
        
        .animal-button {
            background: linear-gradient(45deg, #3498db, #2980b9);
            color: white;
            border: none;
            padding: 12px 25px;
            font-size: 16px;
            border-radius: 20px;
            cursor: pointer;
            margin: 10px 0;
            transition: all 0.3s ease;
            font-weight: bold;
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        }
        
        .animal-button:hover {
            transform: scale(1.05);
            background: linear-gradient(45deg, #2980b9, #3498db);
        }
        
        .members-container {
            display: none;
            margin-top: 25px;
            padding: 25px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 15px;
            border: 2px dashed rgba(255,255,255,0.6);
        }
        
        .animal-info-container {
            display: none;
            margin-top: 20px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 12px;
            border: 2px dashed rgba(255,255,255,0.6);
        }
        
        .member-card {
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            margin: 15px 0;
            border-radius: 12px;
            font-weight: bold;
            color: #2c3e50;
            animation: fadeIn 0.5s ease;
            text-align: center;
            border: 2px solid transparent;
            transition: all 0.3s ease;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .member-info {
            text-align: left;
            flex-grow: 1;
        }
        
        .member-name {
            font-size: 18px;
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        .member-role {
            font-size: 14px;
            color: #7f8c8d;
            font-style: italic;
        }
        
        .role-badge {
            display: inline-block;
            background: linear-gradient(45deg, #e17055, #fd79a8);
            color: white;
            padding: 6px 15px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
        
        .VP information Technology-role { 
            background: linear-gradient(45deg, #e74c3c, #c0392b); 
        }
        
        .VP Internal-role { 
            background: linear-gradient(45deg, #9b59b6, #8e44ad);
        }
        
        .VP External-role { 
            background: linear-gradient(45deg, #3498db, #2980b9);
        }
        
        .VP Production-role { 
            background: linear-gradient(45deg, #27ae60, #2ecc71);
        }
        
        .VP Marketing-role { 
            background: linear-gradient(45deg, #f39c12, #f1c40f);
        }
        
        .VP Sales-role { 
            background: linear-gradient(45deg, #8e44ad, #9b59b6);
        }
        
        .VP Human Resources-role { 
            background: linear-gradient(45deg, #d35400, #e67e22);
        }
        
        .VP Corporate Social Responsibility-role { 
            background: linear-gradient(45deg, #16a085, #1abc9c);
        }
        
        .VP Finance-role { 
            background: linear-gradient(45deg, #c0392b, #e74c3c);
        }
        
        .VP Environment-role { 
            background: linear-gradient(45deg, #27ae60, #2ecc71);
        }
        
        .VP Health & Safety-role { 
            background: linear-gradient(45deg, #e74c3c, #c0392b);
        }
        
        .Head of Video Production & Special Events-role { 
            background: linear-gradient(45deg, #8e44ad, #9b59b6);
        }
        
        .member-card:hover {
            border-color: #e17055;
            transform: scale(1.02);
        }
        
        .designs-container {
            display: flex;
            justify-content: center;
            gap: 25px;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        
        .design-box {
            background: rgba(255, 255, 255, 0.9);
            padding: 25px;
            border-radius: 15px;
            width: 280px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
            transition: all 0.3s ease;
            border: 3px solid transparent;
        }
        
        .design-box:hover {
            transform: translateY(-8px);
            border-color: #e17055;
        }
        
        .design-title {
            color: #2c3e50;
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 15px;
            text-align: center;
            padding-bottom: 10px;
            border-bottom: 2px solid rgba(0,0,0,0.1);
        }
        
        .design-description {
            color: #7f8c8d;
            text-align: center;
            line-height: 1.6;
            margin-bottom: 15px;
            font-size: 16px;
        }
        
        .animal-image {
            width: 100%;
            height: 180px;
            border-radius: 10px;
            margin-bottom: 15px;
            overflow: hidden;
            border: 2px solid #dee2e6;
        }
        
        .animal-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .help-message {
            background: rgba(46, 204, 113, 0.2);
            padding: 12px;
            border-radius: 8px;
            margin-top: 15px;
            text-align: center;
            font-weight: bold;
            color: #27ae60;
            border: 1px solid #27ae60;
        }
        
        .help-button {
            background: linear-gradient(45deg, #3498db, #2980b9);
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 14px;
            border-radius: 20px;
            cursor: pointer;
            margin-top: 10px;
            transition: all 0.3s ease;
            font-weight: bold;
        }
        
        .help-button:hover {
            transform: scale(1.05);
            background: linear-gradient(45deg, #2980b9, #3498db);
        }
        
        /* Quiz Styles */
        .quiz-info {
            background: rgba(255, 255, 255, 0.3);
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
        }
        
        .quiz-question {
            background: rgba(255, 255, 255, 0.9);
            padding: 25px;
            margin: 20px 0;
            border-radius: 15px;
            text-align: center;
        }
        
        .quiz-option {
            background: #3498db;
            color: white;
            border: none;
            padding: 15px 25px;
            margin: 10px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            transition: all 0.3s ease;
            display: block;
            width: 80%;
            margin-left: auto;
            margin-right: auto;
        }
        
        .quiz-option:hover {
            background: #2980b9;
            transform: scale(1.05);
        }
        
        .quiz-result {
            background: rgba(255, 255, 255, 0.9);
            padding: 30px;
            border-radius: 15px;
            margin: 20px 0;
            text-align: center;
        }
        
        .result-buttons {
            margin-top: 20px;
        }
        
        .result-button {
            background: #f39c12;
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 20px;
            cursor: pointer;
            margin: 10px;
            font-size: 16px;
            font-weight: bold;
        }
        
        .back-button {
            background: #e74c3c;
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 20px;
            cursor: pointer;
            margin: 10px;
            font-size: 16px;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .team-title {
            color: #2c3e50;
            font-size: 26px;
            margin-bottom: 20px;
            text-align: center;
            font-weight: bold;
        }
        
        p {
            font-size: 18px;
            line-height: 1.6;
            color: #2c3e50;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1 class="main-title">EcoPins</h1>
        <div class="subtitle">Velcro Pins - JA Company Program</div>
    </div>

    <div class="container">
        <div class="card about-card">
            <h2>About Our Product</h2>
            <p>EcoPins are versatile reusable velcro pins that can be attached to various accessories. We create them with attention to environmental sustainability.</p>
            <p>Each pin represents a commitment to eco-friendly fashion while allowing personal expression.</p>
        </div>

        <div class="card designs-card">
            <h2>Nova Scotia Wildlife Collection</h2>
            <p>Support local endangered species through our special Nova Scotia designs</p>
            
            <div class="designs-container">
                <div class="design-box">
                    <div class="animal-image">
                        <img src="https://i.natgeofe.com/n/cc3fd12b-35f2-410c-894b-dd02112e9d69/right-whales_thumb_4x3.jpg" alt="North Atlantic Right Whale">
                    </div>
                    <div class="design-title">North Atlantic Right Whale</div>
                    <div class="design-description">The North Atlantic Right Whale is one of the world's most endangered large whale species.</div>
                    <div class="help-message">By purchasing this pin, you help fund whale conservation research.</div>
                    
                    <div style="text-align: center;">
                        <button class="animal-button" onclick="toggleAnimalInfo('whale')">
                            Learn More About Whales
                        </button>
                    </div>
                    
                    <div id="whaleInfo" class="animal-info-container">
                        <div class="animal-info-card">
                            <strong>Population:</strong> Only about 350 remaining worldwide
                        </div>
                        <div class="animal-info-card">
                            <strong>Habitat:</strong> Nova Scotia waters during summer months
                        </div>
                        <div class="animal-info-card">
                            <strong>Threats:</strong> Ship strikes, fishing gear entanglement, ocean noise
                        </div>
                        <div class="animal-info-card">
                            <strong>Conservation Status:</strong> Critically Endangered
                        </div>
                    </div>
                    
                    <button class="help-button" onclick="showHelpInfo('whale')">How can I help save whales?</button>
                </div>
                
                <div class="design-box">
                    <div class="animal-image">
                        <img src="https://www.ecowatch.com/wp-content/uploads/2022/04/canada-lynx-1024x576.jpg" alt="Canada Lynx">
                    </div>
                    <div class="design-title">Canada Lynx</div>
                    <div class="design-description">The Canada Lynx is a threatened species in Nova Scotia forests.</div>
                    <div class="help-message">Your purchase supports forest conservation programs.</div>
                    
                    <div style="text-align: center;">
                        <button class="animal-button" onclick="toggleAnimalInfo('lynx')">
                            Learn More About Lynx
                        </button>
                    </div>
                    
                    <div id="lynxInfo" class="animal-info-container">
                        <div class="animal-info-card">
                            <strong>Habitat:</strong> Cape Breton Highlands and forested areas
                        </div>
                        <div class="animal-info-card">
                            <strong>Diet:</strong> Primarily snowshoe hares
                        </div>
                        <div class="animal-info-card">
                            <strong>Features:</strong> Large paws for walking on snow, tufted ears
                        </div>
                        <div class="animal-info-card">
                            <strong>Conservation Status:</strong> Threatened in Nova Scotia
                        </div>
                    </div>
                    
                    <button class="help-button" onclick="showHelpInfo('lynx')">How can I help save lynx?</button>
                </div>
                
                <div class="design-box">
                    <div class="animal-image">
                        <img src="https://cdn.provincetownindependent.org/2025/10/Hakimi-leatherback-sea-turtles-photo-1-alive-1.jpeg" alt="Leatherback Sea Turtle">
                    </div>
                    <div class="design-title">Leatherback Sea Turtle</div>
                    <div class="design-description">Leatherback Sea turtles are endangered ocean travelers.</div>
                    <div class="help-message">Buying this pin contributes to sea turtle rescue organizations.</div>
                    
                    <div style="text-align: center;">
                        <button class="animal-button" onclick="toggleAnimalInfo('turtle')">
                            Learn More About Turtles
                        </button>
                    </div>
                    
                    <div id="turtleInfo" class="animal-info-container">
                        <div class="animal-info-card">
                            <strong>Size:</strong> Largest sea turtle, up to 2,000 pounds
                        </div>
                        <div class="animal-info-card">
                            <strong>Migration:</strong> Travel thousands of miles across oceans
                        </div>
                        <div class="animal-info-card">
                            <strong>Diet:</strong> Mainly jellyfish
                        </div>
                        <div class="animal-info-card">
                            <strong>Conservation Status:</strong> Endangered worldwide
                        </div>
                    </div>
                    
                    <button class="help-button" onclick="showHelpInfo('turtle')">How can I help save turtles?</button>
                </div>
            </div>
        </div>

        <div class="card features-card">
            <h2>Product Features</h2>
            <ul class="feature-list">
                <li>Made from recycled and eco-friendly materials</li>
                <li>Easy to switch between different designs</li>
                <li>Multiple design options available</li>
                <li>Supports environmental conservation efforts</li>
                <li>Suitable as gifts</li>
                <li>Created by students learning business skills</li>
            </ul>
        </div>

        <!-- QUIZ SECTION -->
        <div class="card quiz-card">
            <h2>Personality Quiz</h2>
            <p>Which animal matches your personality? Take our quick quiz to find out!</p>

        <!-- Signature Section -->
        <div class="card signature">
            <h3>Website Developer:</h3>
            <div class="creator-name">Avin P. Langroodi</div>
            <div class="contact-info">
                <a href="https://www.linkedin.com/in/avin-langroodi-85ab50287" class="contact-link" target="_blank">LinkedIn Profile</a>
                <a href="mailto:avinlangroodi4@gmail.com" class="email-link">avinlangroodi4@gmail.com</a>
            </div>
            <div class="contact-info">
                <h3>Company Email:</h3>
                <a href="mailto:pinpointpatches1@gmail.com" class="company-email-link">pinpointpatches1@gmail.com</a>
            </div>
            <p>JA Company Program Participant</p>
            <p>Python Programming Project</p>
        </div>
    </div>

    <script>
        // JavaScript functions would go here
        function toggleAnimalInfo(animal) {
            // Function implementation
        }
        
        function showHelpInfo(animal) {
            // Function implementation
        }
    </script>
</body>
</html>
"""
