<!DOCTYPE html>
<html>
<head>
    <title>Animal Designs - EcoPins</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #74b9ff, #0984e3);
        }
        
        .header {
            background: white;
            padding: 20px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .main-title {
            color: #2c3e50;
            font-size: 36px;
            margin: 0;
        }
        
        .subtitle {
            color: #7f8c8d;
            font-size: 18px;
            margin: 10px 0;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .card {
            background: white;
            padding: 25px;
            margin: 20px 0;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        h2 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 20px;
        }
        
        .designs-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-top: 20px;
        }
        
        .design-card {
            background: #f8f9fa;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            border: 3px solid transparent;
            transition: all 0.3s ease;
        }
        
        .design-card:hover {
            border-color: #3498db;
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        
        .animal-image {
            width: 100%;
            height: 200px;
            border-radius: 8px;
            margin-bottom: 15px;
            overflow: hidden;
        }
        
        .animal-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }
        
        .design-card:hover .animal-image img {
            transform: scale(1.05);
        }
        
        .animal-name {
            font-size: 22px;
            font-weight: bold;
            color: #2c3e50;
            margin: 10px 0;
        }
        
        .animal-description {
            color: #7f8c8d;
            line-height: 1.6;
            margin-bottom: 15px;
        }
        
        .info-button {
            background: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 5px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .info-button:hover {
            background: #2980b9;
            transform: scale(1.05);
        }
        
        .help-button {
            background: #e74c3c;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 5px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .help-button:hover {
            background: #c0392b;
            transform: scale(1.05);
        }
        
        .info-container {
            display: none;
            background: #ecf0f1;
            padding: 15px;
            margin: 15px 0;
            border-radius: 8px;
            text-align: left;
            border-left: 4px solid #3498db;
        }
        
        .help-container {
            display: none;
            background: #ffeaa7;
            padding: 15px;
            margin: 15px 0;
            border-radius: 8px;
            border-left: 4px solid #e74c3c;
        }
        
        .feature-list {
            text-align: left;
            margin: 10px 0;
        }
        
        .feature-list li {
            margin: 8px 0;
            padding-left: 10px;
        }
        
        .buy-highlight {
            font-weight: bold;
            color: #e74c3c;
            margin-top: 15px;
            padding: 10px;
            background: #ffeaa7;
            border-radius: 5px;
            text-align: center;
            font-size: 18px;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 15px 0;
        }
        
        .stat-item {
            background: white;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            border: 2px solid #bdc3c7;
        }
        
        .stat-value {
            font-size: 24px;
            font-weight: bold;
            color: #e74c3c;
            margin: 5px 0;
        }
        
        .stat-label {
            color: #7f8c8d;
            font-size: 14px;
        }
        
        .navigation {
            text-align: center;
            margin: 30px 0;
        }
        
        .nav-button {
            background: #2c3e50;
            color: white;
            border: none;
            padding: 12px 25px;
            margin: 0 10px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            text-decoration: none;
            display: inline-block;
            transition: all 0.3s ease;
        }
        
        .nav-button:hover {
            background: #34495e;
            transform: scale(1.05);
        }
        
        .contact-section {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            margin-top: 40px;
        }
        
        .contact-info {
            margin: 15px 0;
        }
        
        .contact-link {
            color: white;
            text-decoration: none;
            font-weight: bold;
            margin: 0 15px;
            padding: 10px 20px;
            border-radius: 25px;
            background: rgba(255,255,255,0.2);
            transition: all 0.3s ease;
            display: inline-block;
        }
        
        .contact-link:hover {
            background: rgba(255,255,255,0.3);
            transform: scale(1.05);
        }
        
        .email-link {
            color: #ffeaa7;
            text-decoration: none;
            font-weight: bold;
            margin: 0 15px;
            padding: 10px 20px;
            border-radius: 25px;
            background: rgba(255,255,255,0.1);
            transition: all 0.3s ease;
            display: inline-block;
        }
        
        .email-link:hover {
            background: rgba(255,255,255,0.2);
            transform: scale(1.05);
        }
        
        .status-critical {
            color: #e74c3c;
            font-weight: bold;
            font-size: 18px;
        }
        
        .status-threatened {
            color: #e67e22;
            font-weight: bold;
            font-size: 18px;
        }
        
        .status-endangered {
            color: #f39c12;
            font-weight: bold;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1 class="main-title">EcoPins Animal Designs</h1>
        <div class="subtitle">Support Endangered Species Through Our Velcro Pin Collection</div>
    </div>

    <div class="container">
        <!-- Introduction -->
        <div class="card">
            <h2>Nova Scotia Wildlife Collection</h2>
            <p style="text-align: center; font-size: 18px; line-height: 1.6;">
                Each EcoPin represents an endangered or threatened species from Nova Scotia. 
                By purchasing our pins, you directly support conservation efforts and help protect these amazing animals.
            </p>
        </div>

        <!-- Animal Designs Grid -->
        <div class="designs-grid">
            <!-- Whale Design -->
            <div class="design-card">
                <div class="animal-image">
                    <img src="https://i.natgeofe.com/n/cc3fd12b-35f2-410c-894b-dd02112e9d69/right-whales_thumb_4x3.jpg" alt="North Atlantic Right Whale">
                </div>
                <div class="animal-name">North Atlantic Right Whale</div>
                <div class="animal-description">
                    One of the world's most endangered large whale species, with only about 350 individuals remaining.
                </div>
                
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-value">~350</div>
                        <div class="stat-label">Remaining</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">Critically</div>
                        <div class="stat-label">Endangered</div>
                    </div>
                </div>
                
                <button class="info-button" onclick="toggleInfo('whaleDetails')">Species Information</button>
                <button class="help-button" onclick="toggleInfo('whaleHelp')">How to Help</button>
                
                <div id="whaleDetails" class="info-container">
                    <h4>About North Atlantic Right Whales:</h4>
                    <ul class="feature-list">
                        <li><strong>Scientific Name:</strong> Eubalaena glacialis</li>
                        <li><strong>Habitat:</strong> Atlantic coastal waters, including Nova Scotia</li>
                        <li><strong>Size:</strong> Up to 52 feet long, weighing up to 70 tons</li>
                        <li><strong>Diet:</strong> Tiny crustaceans called copepods</li>
                        <li><strong>Lifespan:</strong> Up to 70 years</li>
                        <li><strong>Threats:</strong> Ship strikes, fishing gear entanglement, ocean noise</li>
                    </ul>
                    <p class="status-critical">CRITICALLY ENDANGERED - URGENT ACTION NEEDED</p>
                </div>
                
                <div id="whaleHelp" class="help-container">
                    <h4>How You Can Help Save Right Whales:</h4>
                    <ul class="feature-list">
                        <li>Support organizations working on whale conservation</li>
                        <li>Choose sustainable seafood to reduce fishing pressure</li>
                        <li>Reduce plastic use to prevent ocean pollution</li>
                        <li>Report whale sightings to marine authorities</li>
                        <li>Advocate for ship speed restrictions in whale habitats</li>
                    </ul>
                    <div class="buy-highlight">BUY A WHALE PIN TO SUPPORT CONSERVATION!</div>
                </div>
            </div>
            
            <!-- Lynx Design -->
            <div class="design-card">
                <div class="animal-image">
                    <img src="https://www.ecowatch.com/wp-content/uploads/2022/04/canada-lynx-1024x576.jpg" alt="Canada Lynx">
                </div>
                <div class="animal-name">Canada Lynx</div>
                <div class="animal-description">
                    A threatened species in Nova Scotia, primarily found in the Cape Breton Highlands.
                </div>
                
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-value">&lt;50</div>
                        <div class="stat-label">In Nova Scotia</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">Threatened</div>
                        <div class="stat-label">Status</div>
                    </div>
                </div>
                
                <button class="info-button" onclick="toggleInfo('lynxDetails')">Species Information</button>
                <button class="help-button" onclick="toggleInfo('lynxHelp')">How to Help</button>
                
                <div id="lynxDetails" class="info-container">
                    <h4>About Canada Lynx:</h4>
                    <ul class="feature-list">
                        <li><strong>Scientific Name:</strong> Lynx canadensis</li>
                        <li><strong>Habitat:</strong> Boreal forests, Cape Breton Highlands</li>
                        <li><strong>Size:</strong> 18-24 pounds, about 3 feet long</li>
                        <li><strong>Diet:</strong> Primarily snowshoe hares (90% of diet)</li>
                        <li><strong>Lifespan:</strong> Up to 15 years in the wild</li>
                        <li><strong>Threats:</strong> Habitat loss, climate change, reduced prey</li>
                    </ul>
                    <p class="status-threatened">THREATENED - PROTECTION NEEDED</p>
                </div>
                
                <div id="lynxHelp" class="help-container">
                    <h4>How You Can Help Protect Lynx:</h4>
                    <ul class="feature-list">
                        <li>Support forest conservation efforts</li>
                        <li>Respect wildlife habitats when hiking</li>
                        <li>Donate to lynx research and protection programs</li>
                        <li>Learn about coexistence with wildlife</li>
                        <li>Advocate for protected wilderness areas</li>
                    </ul>
                    <div class="buy-highlight">BUY A LYNX PIN TO SUPPORT FOREST CONSERVATION!</div>
                </div>
            </div>
            
            <!-- Turtle Design -->
            <div class="design-card">
                <div class="animal-image">
                    <img src="https://cdn.provincetownindependent.org/2025/10/Hakimi-leatherback-sea-turtles-photo-1-alive-1.jpeg" alt="Leatherback Sea Turtle">
                </div>
                <div class="animal-name">Leatherback Sea Turtle</div>
                <div class="animal-description">
                    The largest sea turtle species, endangered ocean travelers that visit Nova Scotia waters.
                </div>
                
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-value">2,000 lbs</div>
                        <div class="stat-label">Maximum Weight</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">Endangered</div>
                        <div class="stat-label">Status</div>
                    </div>
                </div>
                
                <button class="info-button" onclick="toggleInfo('turtleDetails')">Species Information</button>
                <button class="help-button" onclick="toggleInfo('turtleHelp')">How to Help</button>
                
                <div id="turtleDetails" class="info-container">
                    <h4>About Leatherback Sea Turtles:</h4>
                    <ul class="feature-list">
                        <li><strong>Scientific Name:</strong> Dermochelys coriacea</li>
                        <li><strong>Habitat:</strong> Open ocean, coastal waters during migration</li>
                        <li><strong>Size:</strong> Up to 7 feet long, weighing 2,000 pounds</li>
                        <li><strong>Diet:</strong> Jellyfish and other soft-bodied animals</li>
                        <li><strong>Lifespan:</strong> Up to 50 years</li>
                        <li><strong>Migration:</strong> Travel thousands of miles annually</li>
                        <li><strong>Threats:</strong> Plastic pollution, fishing gear, habitat loss</li>
                    </ul>
                    <p class="status-endangered">ENDANGERED - CONSERVATION CRITICAL</p>
                </div>
                
                <div id="turtleHelp" class="help-container">
                    <h4>How You Can Help Sea Turtles:</h4>
                    <ul class="feature-list">
                        <li>Reduce single-use plastic consumption</li>
                        <li>Participate in beach cleanups</li>
                        <li>Support sea turtle rescue and rehabilitation centers</li>
                        <li>Choose reef-safe sunscreen when swimming</li>
                        <li>Respect nesting beaches and keep lights low at night</li>
                    </ul>
                    <div class="buy-highlight">BUY A TURTLE PIN TO SUPPORT OCEAN CONSERVATION!</div>
                </div>
            </div>
        </div>

        <!-- Conservation Impact -->
        <div class="card">
            <h2>Our Conservation Impact</h2>
            <div style="text-align: center; font-size: 18px; line-height: 1.6;">
                <p>100% of profits from EcoPins sales go directly to environmental organizations working to protect these species.</p>
                <p>Your purchase makes a real difference in conservation efforts!</p>
            </div>
            
            <div class="stats-grid" style="margin-top: 30px;">
                <div class="stat-item">
                    <div class="stat-value">100%</div>
                    <div class="stat-label">Profits Donated</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">3</div>
                    <div class="stat-label">Species Supported</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">Local</div>
                    <div class="stat-label">Nova Scotia Focus</div>
                </div>
            </div>
        </div>

        <!-- Navigation -->
        <div class="navigation">
            <a href="index.html" class="nav-button">Back to Main Page</a>
            <a href="ecopins_website.html" class="nav-button">View Original Website</a>
        </div>

        <!-- Contact Section -->
        <div class="contact-section">
            <h2>Contact Us</h2>
            <p>Have questions about our animal designs or conservation efforts? Get in touch!</p>
            
            <div class="contact-info">
                <a href="https://www.linkedin.com/in/avin-langroodi-85ab50287" class="contact-link" target="_blank">LinkedIn</a>
                <a href="mailto:avinlangroodi4@gmail.com" class="email-link">avinlangroodi4@gmail.com</a>
            </div>
            <div class="contact-info">
                <strong>Company Email:</strong>
                <a href="mailto:pinpointpatches1@gmail.com" class="email-link">pinpointpatches1@gmail.com</a>
            </div>
        </div>
    </div>

    <script>
        // Toggle information sections
        function toggleInfo(elementId) {
            var element = document.getElementById(elementId);
            if (element.style.display === 'none' || element.style.display === '') {
                element.style.display = 'block';
            } else {
                element.style.display = 'none';
            }
        }
        
        // Close other info sections when one is opened
        document.addEventListener('DOMContentLoaded', function() {
            const infoButtons = document.querySelectorAll('.info-button, .help-button');
            infoButtons.forEach(button => {
                button.addEventListener('click', function() {
                    // You can add logic here to close other sections if needed
                });
            });
        });
    </script>
</body>
</html>
