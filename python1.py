from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

service_prices = {
    "Essay": 50,
    "Research Paper": 75,
    "Critical Writing": 50,
    "Report": 20,
    "Annotated Bibliography": 30,
    "Article": 25,
    "Assessment": 65,
    "Book Review": 65,
    "Business Letter": 55,
    "Case Study": 69,
    "Course Work": 25,
    "Discussion Board Post": 70,
    "Dissertation": 25,
    "Editing": 65,
    "Extended Outline": 100,
    "Movie Review": 20,
    "Nursing Paper": 30,
    "Online Test": 99,
    "Paraphrasing": 27,
    "Personal Statement": 65,
    "Poster": 30,
    "Power point presentation": 80,
    "Proposal": 10,
    "Q & A": 60,
    "Quiz": 55,
    "Reading Diary": 10,
    "Speech": 30,
    "Summarizing": 25,
    "Term Paper": 90,
    "Thesis": 30,
    "Literature Review": 22,
    "Original Research Paper": 33,
    "Term paper writing": 11,
    "Blog post writing": 22,
    "Resume/CV writing": 44,
    "Cover letter writing": 55,
    "Proofreading and editing": 99,
    "Ghostwriting": 77,
    "Grant proposal writing": 66,
    "White paper writing": 44,
    "Press release writing": 88,
    "Product description writing": 77,
    "Social media content writing": 44,
    "Landing page writing": 33,
    "Website content writing": 77,
    "SEO content writing": 35,
    "Brochure and pamphlet writing": 74,
    "Software documentation writing": 66,
    "Historical writing": 77,
    "Political writing": 29,
    "Real estate writing": 30,
    "Book publishing": 33,
    "Magazine publishing": 22,
    "Newspaper publishing": 44,
    "Academic journal publishing": 66,
    "Research paper publishing": 87,
    "Brochure publishing": 42,
    "Catalog publishing": 26,
    "Annual report publishing": 54,
    "Comic book publishing": 30,
    "Graphic novel publishing": 55,
    "Zine publishing": 41,
    "Audiobook publishing": 20,
    "White paper publishing": 65,
    "Technical manual publishing": 51,
    "Trade publication publishing": 19,
    "Literary journal publishing": 33,
    "Poetry chapbook publishing": 55,
    "Self-publishing services": 44,
    "Poetry journal publishing": 55,
    "Financial magazine publishing": 88,
    "Science fiction magazine publishing": 45,
    "Fashion catalog publishing": 65,
    "Travelogue publishing": 55,
    "Sports blog publishing": 45,
    "Gaming magazine publishing": 55,
    "Gardening magazine publishing": 42,
    "Pet care magazine publishing": 20,
    "DIY and craft magazine publishing": 80,
    "Art critique publication publishing": 20,
    "Political opinion publication publishing": 65,
    "Scientific research article publishing": 20,
    "Food blog publishing": 22,
    "Technology blog publishing": 40,
    "Lifestyle blog publishing": 20,
    "Horror book publishing": 22,
    "Thesis and dissertation publishing": 30,
    "Primary Data Collection": 20,
    "Market Analysis": 30,
    "Consumer Insights": 25,
    "Competitive Analysis": 22,
    "Brand Research": 99,
    "Market Segmentation": 52,
    "Product Testing and Development": 32,
    "Trend Analysis": 52,
    "Data Analytics and Visualization": 50,
    "Market Research Design and Planning": 25,
    "Customer Segmentation and Profiling": 95,
    "Brand Research and Positioning": 25,
    "Market Opportunity Assessment": 55,
    "Custom Market Research and Consulting": 20, 
    "Market Entry Strategy": 30,
    "Innovation and idea testing": 55,
    "Brand loyalty and advocacy measurement": 30,
    "Industry and market analysis reports": 25,
    "Market research training and workshops": 55,
    "Product performance tracking": 35,
    "Market entry barriers analysis": 52,
    "Brand awareness and perception studies": 25,
    "Consumer sentiment analysis": 50,
    "Competitive landscape analysis": 20,
    "Market share analysis": 55,
    "Cross-cultural research and international studies": 20, 
    "Geographical and demographic studies": 77,
    "Concept and idea generation": 22,
    "Data mining and analytics": 30,
    "Usability testing and user experience research": 20,
    "Focus groups and in-depth interviews": 10,
    "Performance Marketing": 21, 
    "Influencer Marketing": 23,
    "Marketing Automation": 25,
    "Marketplaces Promotions": 84,
    "Account-Based Marketing": 95,
    "Brand Architecture": 94,
    "Brand Guidelines Development": 27,
    "Brand Positioning and Differentiation": 37,
    "Brand Experience Design": 65,
    "Brand Training and Internal Branding": 57,
    "Financial Management": 54,
    "Operations Optimization": 65,
    "Organizational Development": 61,
    "Change Management": 37,
    "Technology Consulting": 54,
    "Risk ManagementMarketing and Branding": 64,
    "Marketing and Branding": 27,
    "Sustainability and CSR Consulting": 34,
    "Manufacturing and Operations Consulting": 20,
    "Hospitality and Tourism Consulting": 94,
    "Healthcare Consulting": 64,
    "Nonprofit Consulting": 67,
    "Family Business Consulting": 54,
    "Small Business Consulting": 51,
    "Start-up Consulting and Support": 66,
    "Regulatory Compliance": 77,
    "Intellectual Property Strategy and Protection": 20,
    "Diversity and Inclusion Consulting": 28,
    "Succession Planning": 65,
    "Training and Development Programs": 77,
    "Leadership Development and Coaching": 60,
    "Cybersecurity Consulting": 22,
    "Sales and Channel Strategy": 28,
    "E-commerce Strategy and Implementation": 67,
    "Project Management": 51,
    "Business Performance Metrics and KPIs": 24,
    "Financial Analysis and Modeling": 22,
    "Business Planning and Forecasting": 20,
    "Investment Consulting for Businesses": 70,
    "Investment Consulting for Wealth Creation": 20,
    "Mutual Funds Investment Consulting": 55,
    "Portfolio Analysis and Optimization": 30,
    "Investment Strategy Development": 41,
    "Investment Performance Evaluation": 20,
    "Retirement Planning and Pension Advisory": 30,
    "Risk Management and Compliance": 54,
    "Sovereign Wealth Fund Consulting": 71,
    "Institutional Investor Consulting": 20,
    "Investment Outsourcing Solutions": 30,
    "Investment Reporting and Dashboards": 30,
    "Investment Governance Framework Design": 22,
    "Capital Market Assumptions and Forecasting": 98, 
    "Investment Due Diligence and Oversight": 75,
    "Investment Fee Analysis and Negotiation": 84,
    "Philanthropic Giving Strategies": 94,
    "Financial Planning and Goal Setting": 54,
    "Impact Investing Consulting": 69,
    "Hedge Fund Consulting": 64,
    "Risk Management and Mitigation": 55,
    "Pension Fund Consulting": 47,
    "Family Office Consulting": 78,
    "Wealth Management Consulting": 41,
    "IT Strategy and Roadmap Development": 20,
    "Digital Transformation": 25,
    "Technology Assessments and Audits": 55,
    "Software Development": 45,
    "Android App Development": 30,
    "Web App Development": 50,
    "Data Strategy and Analytics": 22,
    "Innovation and Emerging Technology Advisory": 55,
    "CMS development (Content Management System)": 32,
    "API development": 55,
    "UI/UX design and development": 44,
    "Cloud computing and deployment": 66,
    "Database development and management": 20,
    "Data analysis and visualization": 77,
    "Machine learning and AI development": 30,
    "Natural language processing (NLP)": 44,
    "Chatbot development": 22,
    "Blockchain development": 66,
    "Cryptocurrency development": 20,
    "IT Sourcing and Procurement Strategy": 30,
    "IT Resource Planning and Allocation": 55,
    "Software Selection and Implementation": 24,
    "Software Development Life Cycle (SDLC) Consulting": 30,
    "Custom Made Product": 41,
    "Network Design and Optimization": 30,
    "Data Center Optimization and Consolidation": 40,
    "Robotic Process Automation (RPA) Consulting": 33,
    "IT Risk Assessment and Mitigation": 15,
    "Artificial Intelligence (AI) and Machine Learning Consulting": 20,
    "Business Process Automation Consulting": 44,
    "IT Service Management and ITIL Consulting": 30,
    "Political campaign management": 25,
    "Election strategy consulting": 20,
    "Political branding and messaging": 65,
    "Political research and analysis": 20,
    "Grassroots organizing": 52,
    "Voter outreach and mobilization": 35,
    "Constituency profiling": 56,
    "Opinion polling": 41,
    "Political event planning and management": 23,
    "Political fundraising strategies": 52,
    "Digital marketing for political campaigns": 25,
    "Public relations for politicians": 25,
    "Political Endorsement Strategy": 22,
    "Political Speech Coaching": 55,
    "Ballot Access and Petition Management": 20,
    "Campaign Compliance and Reporting": 77,
    "Media Training for Candidates and Campaign Staff": 44,
    "Campaign Material Production": 52,
    "Strategic Alliances and Partnerships": 32,
    "Political Training and Education": 22,
    "Coalition Building and Management": 54,
    "Debate Preparation and Coaching": 41,
    "Opposition Research": 65,
    "Volunteer Management": 54,
    "Political Consulting for Corporations and Businesses": 41,
    "Digital Marketing": 20,
    "Logo Creation": 22,
    "Ads Campaign": 10,
    "Search Engine Optimization (SEO)": 30,
    "Marketing Automation": 55,
    "Account-Based Marketing": 30,
    "Brand Positioning": 22,
    "Brand Identity DesignBrand Messaging and Communication": 10,
    "Pay-Per-Click (PPC) Advertising": 30,
    "Social Media Marketing and Advertising": 15,
    "Content Marketing Strategy": 50,
    "Conversion Rate Optimization (CRO)": 30,
    "Web Analytics and Data Analysis": 22,
    "Online Reputation Management": 21,
    "Influencer Marketing Strategy": 20,
    "Video Marketing and Advertising": 30,
    "App Store Optimization (ASO)": 10,
    "Programmatic Advertising": 30,
    "Affiliate Marketing": 33,
    "E-commerce Marketing": 20,
    "Lead Generation Strategy": 30, 
    "Marketing Automation Implementation": 11,
    "Customer Relationship Management (CRM) Integration": 51,
    "User Experience (UX) Design": 15,
    "Website Design and Development": 11,
    "Content Creation and Marketing": 22,
    "Blogging and Article Writing": 23,
    "Social Media Listening and Monitoring": 20,
    "Online Community Management": 22,
    "Influencer Outreach and Management": 10,
    "Online Advertising Campaign Management": 11,
    "Local Search Marketing": 20,
    "Online PR and Media Outreach": 30,
    "Branding and Visual Identity in Digital Channels": 10,
    "A/B Testing and Multivariate Testing": 22,
    "Voice Search Optimization": 23,
    "Chatbot Development and Implementation": 33,
    "Mobile App Marketing": 44,
    "Podcast Marketing and Advertising": 55, 
    "Webinar Marketing": 66,
    "Geo-targeting and Location-based Marketing": 77,
    "Event concept development and ideation": 22,
    "Budget planning and financial management": 20,
    "Venue selection and negotiation": 25,
    "Event logistics coordination": 56,
    "Vendor and supplier management": 55,
    "Event marketing and promotion strategies": 15,
    "Sponsorship and partnership acquisition": 35,
    "Program and agenda development": 20,
    "Speaker and talent management": 11,
    "Event registration and ticketing management": 32,
    "On-site event management and coordination": 22,
    "Event branding and visual identity": 44,
    "Event audio and visual production": 41,
    "Event transportation and logistics": 15,
    "Event database management and CRM integrationon 15": 15,
    "Event photography and videography": 10,
    "Event signage and branding materials": 52,
    "Social media and digital marketing for events": 22,
    "VIP and guest relations management": 52,
    "Sponsorship activation and fulfillment": 32,
    "Exhibitor and booth management": 52,
    "Accommodation and travel arrangements": 22,
    "Health and safety planning for events": 54,
    "Event licensing and permissions": 55,
    "Event merchandise and promotional items": 50,
}

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def form():
    if request.method == 'POST':
        selected_services = request.form.getlist('writing_services') + request.form.getlist('publishing_services') + request.form.getlist('marketing_services') + request.form.getlist('business_services') + request.form.getlist('investment_services') + request.form.getlist('technology_services') + request.form.getlist('political_services') + request.form.getlist('branding_services') + request.form.getlist('event_management_services')
        total_amount = sum([service_prices.get(service, 0) for service in selected_services])
        return render_template('form.html', total_amount=total_amount)

if __name__ == '__main__':
    app.run(debug=True)